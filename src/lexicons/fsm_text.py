from src.utils import time_utils

fsm_dict: dict[str, dict[str, str]] = {
    "wait_message": {
        "text_ru": "Ожидайте, подсчёт займет не больше 30 секунд ⏱",
        "text_en": "Please wait, "
                   "calculation will take no more than 30 seconds ⏱"
    },
    "input_inr_amount": {
        "text_ru": "Введите сумму обмена в рупиях (₹):",
        "text_en": "Enter the amount of exchange in rupees (₹):"
    },
    "input_rub_amount": {
        "text_ru": "Введите сумму обмена в рублях (₽):",
        "text_en": "Enter the amount of exchange in rubles (₽):"
    },
    "input_usdt_amount": {
        "text_ru": "Введите сумму обмена в USDT (₮):",
        "text_en": "Enter the amount of exchange in USDT (₮):"
    },
    "input_commission": {
        "text_ru": "Введи свою комиссию в процентах (%)\n\n"
                   "<i>Просто укажите число, без знака процента)</i>",
        "text_en": "Enter your commission in percentage (%)\n\n"
                   "<i>Just specify the number, without the percent sign)</i>"
    },
    "input_error": {
        "text_ru": "Похоже, в числе допущена ошибка.\n"
                   "Пожалуйста, отправьте число еще раз. "
                   "Вы можете использовать точку или запятую в качестве "
                   "разделителя дробной части.",
        "text_en": "It seems there was a mistake in the number.\n"
                   "Please, send the number again. "
                   "You can use either a dot or a comma as "
                   "the decimal separator."
    },
}


async def format_currency_message_inr(
    amount: float, coefficient: float, language_code: str
) -> str:
    if language_code == 'en':
        return (
            f'Currency exchange rate at {time_utils.current_time}:\n\n'
            f'Coefficient {coefficient:.3f}\n\n'
            f'{int(amount)} rupees = {int(amount * coefficient)} rubles\n'
        )
    else:
        return (
            f'Курс валют на {time_utils.current_time}:\n\n'
            f'Коэффициент {coefficient:.3f}\n\n'
            f'{int(amount)} рупий = {int(amount * coefficient)} рублей\n'
        )


async def format_currency_message_rub(
    amount: float, coefficient: float, language_code: str
) -> str:
    if language_code == 'en':
        return (
            f'Currency exchange rate at {time_utils.current_time}:\n\n'
            f'Coefficient {coefficient:.3f}\n\n'
            f'{int(amount)} rubles = {int(amount * coefficient)} rupees\n'
        )
    else:
        return (
            f'Курс валют на {time_utils.current_time}:\n\n'
            f'Коэффициент {coefficient:.3f}\n\n'
            f'{int(amount)} рублей = {int(amount * coefficient)} рупий\n'
        )


async def format_currency_message_usdt_inr(
    amount: float, coefficient: float, language_code: str
) -> str:
    if language_code == 'en':
        return (
            f'Currency exchange rate at {time_utils.current_time}:\n\n'
            f'Coefficient {coefficient:.3f}\n\n'
            f'{int(amount)} rupees = {int(amount * coefficient)} usdt\n'
        )
    else:
        return (
            f'Курс валют на {time_utils.current_time}:\n\n'
            f'Коэффициент {coefficient:.3f}\n\n'
            f'{int(amount)} рупий = {int(amount * coefficient)} usdt\n'
        )


async def format_currency_message_inr_usdt(
    amount: float, coefficient: float, language_code: str
) -> str:
    if language_code == 'en':
        return (
            f'Currency exchange rate at {time_utils.current_time}:\n\n'
            f'Coefficient {coefficient:.3f}\n\n'
            f'{int(amount)} usdt = {int(amount * coefficient)} rupees\n'
        )
    else:
        return (
            f'Курс валют на {time_utils.current_time}:\n\n'
            f'Коэффициент {coefficient:.3f}\n\n'
            f'{int(amount)} usdt = {int(amount * coefficient)} рупий\n'
        )
