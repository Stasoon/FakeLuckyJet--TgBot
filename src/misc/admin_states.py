from aiogram.dispatcher.filters.state import State, StatesGroup


class CoefficientsSetting(StatesGroup):
    wait_for_new_coefficients = State()
