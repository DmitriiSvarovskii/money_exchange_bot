from aiogram import Router, types, F
from aiogram.filters import CommandStart

from src.keyboards import main_kb
from src.lexicons import base_text
from src.utils import stickers, translation_utils


router: Router = Router(name=__name__)


@router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer_sticker(sticker=stickers.stickers_dict['start'])
    await message.answer(
        text=base_text.create_start_text(
            message.chat.first_name,
            message.from_user.language_code
        ),
        reply_markup=main_kb.create_kb_admin_main(
            message.from_user.language_code
        )
    )
    await message.delete()


@router.callback_query(F.data == 'press_help')
async def help_info(callback: types.CallbackQuery):
    await callback.message.answer_sticker(
        sticker=stickers.stickers_dict['help']
    )
    await callback.message.answer(
        text=translation_utils.get_translation(
            callback.from_user.language_code,
            base_text.base_text_dict['help']
        ),
        reply_markup=main_kb.create_kb_admin_main(
            callback.from_user.language_code
        )
    )
