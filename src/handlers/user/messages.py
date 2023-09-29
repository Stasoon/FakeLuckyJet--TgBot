import random


class Messages:
    """Источник фоток: https://telegra.ph/Fotki-dlya-LuckyJet-bota-09-29"""

    @staticmethod
    def ask_for_locale() -> str:
        return 'Выберите язык ⤵️\n' \
               'What is your language? ⤵'

    @staticmethod
    def get_start_sticker() -> str:
        return "CAACAgIAAxkBAAI2VmTL4n1mqPBYjA4Nq849fl0AAQWpgwAC0wUAAj-VzAqfWrvSXUfHMS8E"

    @staticmethod
    def get_welcome_photo() -> str:
        return 'https://telegra.ph/file/6f35bc3a41fa1ad717816.png'

    @staticmethod
    def get_ru_welcome(user_name: str = 'незнакомец') -> str:
        return (f'<b>Приветствую тебя в нашей команде, {user_name}! </b> \n\n'
                'Этот бот даст возможность стабильно зарабатывать каждый день на игре <b>Лаки Джет</b> 🚀🍀 \n\n'
                'Все что нужно сделать, это зайти в игру и нажать кнопку ⤵️ <b>«СЛЕДУЮЩИЙ СИГНАЛ»</b> \n\n'
                'Бот выдаст коэффициент, а твоя задача сделать ставку и забрать свой первый выигрыш💰')

    @staticmethod
    def get_next_signal(onewin_id: int, coeff) -> str:
        return f'🆔 {onewin_id} \n🚀 ВЫВОДИ НА: <b>{coeff}</b>'

    @staticmethod
    def ask_for_code_word() -> str:
        return '🔐 Введите кодовое слово:'

    @staticmethod
    def get_code_word_incorrect():
        return '❗<b>Вы ввели неправильное кодовое слово!</b> \nПопробуйте ещё раз:'

    @staticmethod
    def ask_for_1win_id() -> str:
        return 'Замечательно! \nТеперь введите 🆔 от вашего аккаунта 1win: '

    @staticmethod
    def get_1win_id_incorrect_length() -> str:
        return '❗<b>ID не может содержать букв и символов, только цифры!</b> \nПопробуйте ещё раз:'

    @staticmethod
    def get_1win_id_have_forbidden_symbols() -> str:
        return '❗<b>ID должно иметь длину в 8 цифр</b> \nПопробуйте снова:'

    @staticmethod
    def get_before_game_start() -> str:
        return ("Перед тем как, начать ⤵️\n\n"
                "Минимальная сумма депозита в игре с ботом <b>500-1000₽</b> либо <b>5-15$</b> \n\n"
                "Если вдруг бот выдает не верные коэффициенты, скорее всего ваш аккаунт <b>не активирован</b>. \n"
                "Нужно сделать депозит еще раз, чтобы ваш аккаунт активировался❗")

    @staticmethod
    def get_before_start_photo() -> str:
        return 'AgACAgIAAxkBAAEB_TtkzMl5s-HsM8JstC6FO4PRc4b6SAAC3cYxG5rOaErWm2hpoDD2pQEAAwIAA3kAAy8E'
