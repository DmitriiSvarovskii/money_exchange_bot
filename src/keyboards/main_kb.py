from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
from aiogram.types import (
    InlineKeyboardButton,
)

from src.lexicons import button_text


def create_kb_admin_main(language_code: str) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    buttons = []

    for value in button_text.commands_dict.values():
        if language_code == 'ru':
            btn_text = value.get('text_ru', None)
        elif language_code == 'en':
            btn_text = value.get('text_en', None)
        else:
            btn_text = None

        if btn_text:
            buttons.append(InlineKeyboardButton(
                text=btn_text, callback_data=value['callback_data']))

    keyboard.row(*buttons, width=1)

    return keyboard.as_markup()
