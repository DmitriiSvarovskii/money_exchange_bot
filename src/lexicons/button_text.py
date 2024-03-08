commands_dict: dict[str, dict[str, str]] = {
    '/get_rates': {
        'text_ru': 'Курс валют',
        'text_en': 'Currency rates',
        'callback_data': 'press_get_rates'
    },
    '/get_rates_exch_inr': {
        'text_ru': 'Обмен (рупии за рубли)',
        'text_en': 'Exchange (rupees for rubles)',
        'callback_data': 'press_get_rates_exch_inr'
    },
    '/get_rates_exch_ruble': {
        'text_ru': 'Обмен (рубли на рупии)',
        'text_en': 'Exchange (rubles for rupees)',
        'callback_data': 'press_get_rates_exch_ruble'
    },
    '/get_rates_exch_usdt_inr': {
        'text_ru': 'Обмен (рупии за usdt)',
        'text_en': 'Exchange (rupees for usdt)',
        'callback_data': 'press_get_rates_exch_usdt_inr'
    },
    '/get_rates_exch_inr_usdt': {
        'text_ru': 'Обмен (usdt на рупии)',
        'text_en': 'Exchange (usdt for rupees)',
        'callback_data': 'press_get_rates_exch_inr_usdt'
    },
    '/help': {
        'text_ru': 'Инструкция',
        'text_en': 'Instructions',
        'callback_data': 'press_help'
    },
}
