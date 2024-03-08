from typing import Union


class CurrencyCalculator:
    def __init__(self, usdt_to_rub=None, usdt_to_inr=None):
        self.usdt_to_rub = usdt_to_rub
        self.usdt_to_inr = usdt_to_inr

    def calculate_coefficient_in_rub(
        self, commission
    ) -> Union[float, None]:
        try:
            return self.usdt_to_inr / self.usdt_to_rub * (1 - commission / 100)
        except ZeroDivisionError:
            return None
        except ValueError:
            return None

    def calculate_coefficient_in_inr(
        self, commission
    ) -> Union[float, None]:
        try:
            return self.usdt_to_rub / self.usdt_to_inr * (1 + commission / 100)
        except ZeroDivisionError:
            return None
        except ValueError:
            return None

    def calculate_coefficient_in_usdt_from_inr(
        self, commission
    ) -> Union[float, None]:
        try:
            return 1 / (self.usdt_to_inr / (1 - commission / 100))
        except ZeroDivisionError:
            return None
        except ValueError:
            return None

    def calculate_coefficient_in_usdt_from_usdt(
        self, commission
    ) -> Union[float, None]:
        try:
            return self.usdt_to_inr / (1 / (1 - commission / 100))
        except ValueError:
            return None
