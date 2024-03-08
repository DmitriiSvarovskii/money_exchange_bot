from src.utils import time_utils

currency_text_dict: dict[str, dict[str, str]] = {
    'await': {
        'text_ru': 'Ожидайте, подсчёт займет не больше 30 секунд ⏱',
        'text_en': 'Please wait, calculation will take no more '
                   'than 30 seconds ⏱'
    },
}


async def format_currency_rates(
    usdt_to_rub: float,
    usdt_to_inr: float,
    language_code: str
) -> str:
    if language_code == 'en':
        return (
            f'Currency exchange rates at {time_utils.current_time}:\n\n'
            f'Buying usdt for rubles (₽): {usdt_to_rub}\n\n'
            f'Selling usdt for rupees (₹): {usdt_to_inr}\n\n'
            f'Coefficient: {round(usdt_to_rub / usdt_to_inr, 3)}'
        )
    else:
        return (
            f'Курс валют на {time_utils.current_time}:\n\n'
            f'Покупка usdt за рубли (₽): {usdt_to_rub}\n\n'
            f'Продажа usdt за рупии (₹): {usdt_to_inr}\n\n'
            f'Коэффициент: {round(usdt_to_rub / usdt_to_inr, 3)}'
        )
