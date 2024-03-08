from aiogram.filters.state import State, StatesGroup


class FSMExchangeRub(StatesGroup):
    amount = State()
    percent = State()
