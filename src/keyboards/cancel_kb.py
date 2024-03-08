from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from src.lexicons import base_text


def create_cancel_kb(language_code: str) -> ReplyKeyboardMarkup:
    for value in base_text.base_text_dict.values():
        if language_code == 'ru':
            btn_text = value.get('text_ru', None)
        elif language_code == 'en':
            btn_text = value.get('text_en', None)
        else:
            btn_text = None

        if btn_text:
            btn: KeyboardButton = KeyboardButton(
                text=btn_text
            )
    keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=[[btn]], resize_keyboard=True)
    return keyboard
