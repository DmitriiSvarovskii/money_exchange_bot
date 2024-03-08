from aiogram import Router, types, F
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

from src.lexicons import base_text
from src.utils import translation_utils
from src.keyboards import main_kb


router: Router = Router(name=__name__)


@router.message(
    F.text == base_text.base_text_dict['cancel_btn']['text_ru'] or
    F.text == base_text.base_text_dict['cancel_btn']['text_en'],
    ~StateFilter(default_state)
)
async def process_cancel_fsm_state(message: types.Message, state: FSMContext):
    await message.answer(
        text=translation_utils.get_translation(
            message.from_user.language_code,
            base_text.base_text_dict['cancel_text']
        ),
        reply_markup=types.ReplyKeyboardRemove()
    )
    await message.answer(
        text=translation_utils.get_translation(
            message.from_user.language_code,
            base_text.base_text_dict['main_text']
        ),
        reply_markup=main_kb.create_kb_admin_main(
            message.from_user.language_code
        )
    )
    await state.clear()
