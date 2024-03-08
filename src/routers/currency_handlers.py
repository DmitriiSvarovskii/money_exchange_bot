from aiogram import Router, types, F

from src.keyboards import main_kb
from src.lexicons import currency_text
from src.utils import currency_utils, stickers, translation_utils


router: Router = Router()


@router.callback_query(F.data == 'press_get_rates')
async def get_rates(callback: types.CallbackQuery):
    await callback.message.answer_sticker(
        sticker=stickers.stickers_dict['await']
    )
    await callback.message.answer(
        text=translation_utils.get_translation(
            callback.from_user.language_code,
            currency_text.currency_text_dict['await']
        )

    )
    usdt_to_rub, usdt_to_inr = await currency_utils.get_currency_rates()
    await callback.message.answer_sticker(
        sticker=stickers.stickers_dict['done']
    )
    await callback.message.answer(
        text=await currency_text.format_currency_rates(
            usdt_to_rub=usdt_to_rub,
            usdt_to_inr=usdt_to_inr,
            language_code=callback.from_user.language_code
        ),
        reply_markup=main_kb.create_kb_admin_main(
            callback.from_user.language_code
        )
    )
