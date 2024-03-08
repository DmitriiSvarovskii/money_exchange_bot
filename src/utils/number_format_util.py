from typing import Union


def process_user_input(user_input: str) -> Union[float, None]:
    user_input = user_input.replace(',', '.')
    try:
        value = float(user_input)
        return round(value, 2)
    except ValueError:
        return None


def is_numeric(text) -> bool:
    try:
        float(text.replace(',', '.'))
        return True
    except ValueError:
        return False
