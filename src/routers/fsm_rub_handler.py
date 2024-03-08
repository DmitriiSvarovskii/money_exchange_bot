from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from src.state import fsm_rub
from src.keyboards import cancel_kb, main_kb
from src.lexicons import fsm_text
from src.utils import (
    number_format_util as utils,
    CurrencyCalculator,
    stickers,
    currency_utils,
    translation_utils
)


router: Router = Router(name=__name__)


@router.callback_query(F.data == 'press_get_rates_exch_ruble')
async def start_fsm_rub(
    callback: types.CallbackQuery,
    state: FSMContext
):
    await callback.message.answer(
        text=translation_utils.get_translation(
            callback.from_user.language_code,
            fsm_text.fsm_dict['input_rub_amount']
        ),
        reply_markup=cancel_kb.create_cancel_kb(
            callback.from_user.language_code
        )
    )
    await state.set_state(fsm_rub.FSMExchangeRub.amount)


@router.message(fsm_rub.FSMExchangeRub.amount,
                lambda message: utils.is_numeric(message.text))
async def get_amount_change_rub(
    message: types.Message,
    state: FSMContext
):
    await state.update_data(amount=utils.process_user_input(message.text))
    await message.answer(
        text=translation_utils.get_translation(
            message.from_user.language_code,
            fsm_text.fsm_dict['input_commission']
        ),
        reply_markup=cancel_kb.create_cancel_kb(
            message.from_user.language_code
        )
    )
    await state.set_state(fsm_rub.FSMExchangeRub.percent)


@router.message(fsm_rub.FSMExchangeRub.amount)
async def warning_not_amount_rub(message: types.Message):
    await message.answer(
        text=translation_utils.get_translation(
            message.from_user.language_code,
            fsm_text.fsm_dict['input_error']
        ),
        reply_markup=cancel_kb.create_cancel_kb(
            message.from_user.language_code
        )
    )


@router.message(fsm_rub.FSMExchangeRub.percent,
                lambda message: utils.is_numeric(message.text))
async def get_percent_rub(message: types.Message, state: FSMContext):
    await message.answer(
        text=translation_utils.get_translation(
            message.from_user.language_code,
            fsm_text.fsm_dict['wait_message']
        ),
        reply_markup=types.ReplyKeyboardRemove()
    )
    await state.update_data(percent=utils.process_user_input(message.text))
    data = await state.get_data()
    usdt_to_rub, usdt_to_inr = await currency_utils.get_currency_rates(
        data['amount']
    )

    calculator = CurrencyCalculator(usdt_to_rub, usdt_to_inr)

    coefficient = calculator.calculate_coefficient_in_rub(
        data['percent'])

    message_text = await fsm_text.format_currency_message_rub(
        amount=data['amount'],
        coefficient=coefficient,
        language_code=message.from_user.language_code
    )
    await message.answer_sticker(sticker=stickers.stickers_dict['done'])
    await message.answer(
        text=message_text,
        reply_markup=main_kb.create_kb_admin_main(
            message.from_user.language_code
        )
    )
    await state.clear()


@router.message(fsm_rub.FSMExchangeRub.percent)
async def warning_not_percent_rub(message: types.Message):
    await message.answer(
        text=translation_utils.get_translation(
            message.from_user.language_code,
            fsm_text.fsm_dict['input_error']
        ),
        reply_markup=cancel_kb.create_cancel_kb(
            message.from_user.language_code
        )
    )
