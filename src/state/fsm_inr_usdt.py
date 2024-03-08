from aiogram.filters.state import State, StatesGroup


class FSMExchangeInrUsdt(StatesGroup):
    amount = State()
    percent = State()
