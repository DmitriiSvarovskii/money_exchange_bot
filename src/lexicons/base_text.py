base_text_dict: dict[str, str] = {
    'main_text': {
        'text_ru': 'Вы в главном меню',
        'text_en': 'You are in the main menu'
    },
    'help': {
        'text_ru': 'С помощью данного боты ты можешь легко и быстро посчитать '
        'стоимость обмена валюты.\n\n'
        'Данные считаются на бирже "bybit", учитываются мерчанты у которых'
        ' более 100 сделок и процент выполнения сделок минимум 90%, также '
        'учитывается сумма обмена.\n'
        'Если во время расчёта курса, ты допустил ошибку или случайно '
        'выбрал не ту категорию, нажми кнопку "❌"\n\n'
        'Список кнопок:\n\n'
        '"Курс валют" - текущий курс валют, также считается коэфициент '
        'обмена без накрутки\n\n'
        '"Обмен (рупии за рубли)" - текущий курс обмена рублей на рупии '
        '(сумма обмена указывается в рупия)\n\n'
        '"Обмен (рубли на рупии)" - текущий курс обмена на рупии за рубли '
        '(сумма обмена указывается в рублях)\n\n'
        '"Обмен (рупии за usdt)" - текущий курс обмена usdt на рупии '
        '(сумма обмена указывается в usdt)\n\n'
        '"Обмен (usdt на рупии)" - текущий курс обмена на рупии за usdt'
        ' (сумма обмена указывается в рупия)\n\n'
        '"Инструкция" - Для получения информции о работе бота воспользуйтесь '
        'командой ',

        'text_en': 'With this bot, you can easily and quickly calculate the '
        'currency exchange rate.\n\n'
        'The data is calculated on the "bybit" exchange, '
        'taking into account merchants with more than 100 transactions and a '
        'transaction completion rate of at least 90%,'
        ' as well as the exchange amount.\n'
        'If you make a mistake during the rate calculation or '
        'accidentally select the wrong category, '
        'press the "❌" button.\n\n'
        'List of buttons:\n\n'
        '"Currency Rates" - current currency rates, also calculates the '
        'exchange coefficient without markup\n\n'
        '"Exchange (rupees for rubles)" - current exchange rate of rubles for '
        'rupees (exchange amount is specified in rupees)\n\n'
        '"Exchange (rubles for rupees)" - current exchange rate for rupees for'
        ' rubles (exchange amount is specified in rubles)\n\n'
        '"Exchange (rupees for USDT)" - current exchange rate of USDT for '
        'rupees (exchange amount is specified in USDT)\n\n'
        '"Exchange (USDT for rupees)" - current exchange rate for rupees for '
        'USDT (exchange amount is specified in rupees)\n\n'
        '"Instructions" - To get information about how the bot works, use the '
        'command',
    },
    'cancel_text': {
        'text_ru': 'Вы отменили ввод данных.',
        'text_en': 'You have cancelled data input.',
    },
    'cancel_btn': {
        'text_ru': '❌',
        'text_en': '❌',
    },
}


commands_text_dict: dict[str, str] = {
    '/start': 'Запуск бота (Launch the bot)',
}


def create_start_text(name: str, language_code: str) -> str:
    if language_code == 'en':
        return (
            f'Hello, {name}!\n'
            'I will help you easily and quickly calculate the current '
            'exchange rate of currencies '
            'on the "bybit" platform using the Tinkoff card'
        )
    else:
        return (
            f'Привет, {name}!\n'
            'Я помогу тебе легко и быстро посчитать текущий курс обмена валют '
            'на платформе "bybit" с использованием карты Tinkoff'
        )
