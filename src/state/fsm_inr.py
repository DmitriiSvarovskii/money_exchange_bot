from aiogram.filters.state import State, StatesGroup


class FSMExchangeInr(StatesGroup):
    amount = State()
    percent = State()
