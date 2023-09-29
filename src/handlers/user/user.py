import asyncio
import random
from typing import Tuple, List, Union

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, InputMedia

from src.utils import send_typing_action, throttle
from src.misc import UserDataInputting
from .messages import Messages
from .kb import Keyboards
from config import CODE_WORD
from src.misc.admin_states import CoefficientsSetting


class CoefficientsLoop:
    """Класс обеспечивает бесконечную прокрутку заданных коэффициентов."""
    coefficients = (0,)
    __current_index = 0
    __end_index = 0

    @classmethod
    def get_next(cls):
        if cls.__current_index > cls.__end_index:
            cls.__current_index = 0
        next_coefficient = cls.coefficients[cls.__current_index]
        cls.__current_index += 1
        return next_coefficient

    @classmethod
    def set_new_coefficients(cls, new_coeffs: List | Tuple) -> None:
        cls.coefficients = new_coeffs
        cls.__current_index = 0
        cls.__end_index = len(new_coeffs) - 1


async def edit_to_new_signal(to_message: Message, user_id: int):
    onewin_id = 41374185
    new_text = Messages.get_next_signal(onewin_id, CoefficientsLoop.get_next())
    # if to_message.text == new_text:
    #     await edit_to_new_signal(to_message, user_id)

    # msg = await to_message.answer('1️⃣2️⃣3️⃣')
    # delay_seconds = 0.4
    #
    # for i in range(1, random.randint(2, 4+1)):
    #     await asyncio.sleep(delay_seconds)
    #     await msg.edit_text('1️⃣')
    #     await asyncio.sleep(delay_seconds)
    #     await msg.edit_text('1️⃣2️⃣')
    #     await asyncio.sleep(delay_seconds)
    #     await msg.edit_text('1️⃣2️⃣3️⃣')

    await to_message.answer(new_text, reply_markup=Keyboards.get_next_signal_markup())


# region Handlers

@throttle()
async def __handle_start_command(message: Message) -> None:
    await send_typing_action(message)

    await message.answer_sticker(sticker=Messages.get_start_sticker())
    await message.answer(text=Messages.ask_for_locale(), reply_markup=Keyboards.get_locale())


async def __handle_locale_callback(callback: CallbackQuery):
    await send_typing_action(callback.message)
    await callback.message.delete()

    await callback.message.answer_photo(
        photo=Messages.get_welcome_photo(),
        caption=Messages.get_ru_welcome(callback.from_user.first_name),
        reply_markup=Keyboards.get_welcome_menu()
    )

@throttle(rate=1.5)
async def __handle_start_callback(callback: CallbackQuery, state: FSMContext):
    await send_typing_action(callback.message)
    await callback.message.delete()
    await callback.message.answer_photo(
        caption=Messages.get_before_game_start(),
        photo=Messages.get_before_start_photo(),
        reply_markup=Keyboards.get_first_signal_markup()
    )



async def __handle_next_signal_callback(callback: CallbackQuery):
    await send_typing_action(callback.message)
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.answer()
    await edit_to_new_signal(callback.message, callback.from_user.id)

# endregion


async def __handle_change_coefficients_command(message: Message, state: FSMContext):
    await message.answer('✏ Введите новые коэффициенты через пробел: ')
    await state.set_state(await CoefficientsSetting.first())


async def __handle_new_coefficients_message(message: Message, state: FSMContext):
    try:
        coefficients = tuple(c for c in message.text.strip().replace('\n', ' ').split())
    except ValueError:
        await message.answer('❗Один из коэффициентов, которые вы ввели, не является числом')
        await state.finish()
        return

    CoefficientsLoop.set_new_coefficients(coefficients)
    msg = await message.answer('✅ Коэффициенты обновлены')
    await state.finish()
    await asyncio.sleep(2)
    await msg.delete()


def register_user_handlers(dp: Dispatcher) -> None:
    # обработка команды /start
    dp.register_message_handler(__handle_start_command, commands=['start'])

    # обработка команды /change
    dp.register_message_handler(__handle_change_coefficients_command, commands=['change'], state=None)
    dp.register_message_handler(__handle_new_coefficients_message, content_types=['text'],
                                state=CoefficientsSetting.wait_for_new_coefficients)

    # выбор языка
    dp.register_callback_query_handler(__handle_locale_callback, Keyboards.locale_callback_data.filter())

    # обработка кнопок приветственного меню
    dp.register_callback_query_handler(__handle_start_callback, text='welcome_menu', state=None)
    # dp.register_message_handler(__handle_user_id_message, state=UserDataInputting.wait_for_id)
    # dp.register_message_handler(__handle_user_password_message, state=UserDataInputting.wait_for_password)

    # обработка нажатия на Следующий сигнал
    dp.register_callback_query_handler(__handle_next_signal_callback, text='next_signal')
