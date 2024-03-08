from aiogram.filters.state import State, StatesGroup


class FSMExchangeUsdtInr(StatesGroup):
    amount = State()
    percent = State()
