import asyncio
import aiohttp

from typing import Union


async def get_currency_rates(min_amount: float = None) -> float:
    page = 1
    usdt_to_rub = None
    usdt_to_inr = None

    while usdt_to_rub is None or usdt_to_inr is None:
        rub_task = asyncio.create_task(get_rates_ruble(
            min_amount=min_amount, page=str(page)))
        inr_task = asyncio.create_task(get_rates_inr(
            min_amount=min_amount, page=str(page)))

        usdt_to_rub = await rub_task
        usdt_to_inr = await inr_task

        if usdt_to_rub is None or usdt_to_inr is None:
            page += 1

    return usdt_to_rub, usdt_to_inr


async def get_rates_ruble(
    page: str,
    min_amount: float = None,
) -> Union[float, None]:
    url = 'https://api2.bybit.com/fiat/otc/item/online'
    headers = {'Accept': '*/*'}
    params = {
        "userId": 102946275,
        "tokenId": "USDT",
        "currencyId": "RUB",
        "payment": ["581", "75"],
        "side": "1",
        "size": "50",
        "page": page,
        "amount": "",
        "authMaker": False,
        "canTrade": False
    }
    async with aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        async with session.post(url, headers=headers, json=params) as response:
            data = await response.json()
            matching_price = None
            for item in data['result']['items']:
                if (
                    item['recentExecuteRate'] > 90 and
                    item['recentOrderNum'] > 100
                ):
                    matching_price = item['price']
                    if (
                        not min_amount or
                        float(min_amount) > float(item['minAmount'])
                    ):
                        matching_price = item['price']
                        break
            return float(matching_price) if matching_price else None


async def get_rates_inr(
    page: str,
    min_amount: float = None,
) -> Union[float, None]:
    url = 'https://api2.bybit.com/fiat/otc/item/online'
    headers = {'Accept': '*/*'}
    params = {
        "userId": 102946275,
        "tokenId": "USDT",
        "currencyId": "INR",
        "payment": ["55", "82"],
        "side": "0",
        "size": "50",
        "page": page,
        "amount": "",
        "authMaker": False,
        "canTrade": False
    }
    async with aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        async with session.post(url, headers=headers, json=params) as response:
            matching_price = None
            data = await response.json()
            for item in data.get('result', {}).get('items', []):
                if (
                    item['recentExecuteRate'] > 90 and
                    item['recentOrderNum'] > 100 and
                    item['tradingPreferenceSet']['nationalLimit'] == ''
                ):
                    matching_price = item['price']
                    if (
                        not min_amount or
                        float(min_amount) > float(item['minAmount'])
                    ):
                        matching_price = item['price']
                        break
            return float(matching_price) if matching_price else None
