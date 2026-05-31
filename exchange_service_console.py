import asyncio
import aiohttp
from datetime import datetime, timedelta
import json
import sys


async def get_exchange_for_date(session, date, symbols):
    url = f"https://api.privatbank.ua/p24api/exchange_rates?json&date={date}"
    try:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                result = {date: {}}
                rates = data["exchangeRate"]
                for rate in rates:
                    if rate.get("currency") in symbols:
                        currency = rate["currency"]
                        sale = rate.get("saleRate", rate.get("saleRateNB"))
                        purchase = rate.get("purchaseRate", rate.get("purchaseRateNB"))
                        result[date][currency] = {"sale": sale, "purchase": purchase}
                return result
            else:
                return {date: {"error": f"HTTP error {response.status}"}}
    except aiohttp.ClientError as e:
        return {date: {"error": str(e)}}


def get_dates(days: int):
    dates = []
    today = datetime.today().date()
    for i in range(days):
        dates.append(today - timedelta(days=i))
    formated_dates = [date.strftime("%d.%m.%Y") for date in dates]
    return formated_dates


# This function is for the websockets realisation
async def get_exchange(days, currencies):
    dates = get_dates(days)
    tasks = []
    async with aiohttp.ClientSession() as session:
        for date in dates:
            tasks.append(get_exchange_for_date(session, date, currencies))
        results = await asyncio.gather(*tasks)
        return results


async def main():
    if len(sys.argv) < 2:
        print("The wrong number of arguments")
        return
    try:
        days = int(sys.argv[1])
    except ValueError:
        print("The wrong argument input")
        return
    if days < 1 or days > 10:
        print("Can't provide data for more than 10 days")
    else:
        symbols = ["USD", "EUR"]
        extra_symbols = [symbol.upper() for symbol in sys.argv[2:]]
        symbols.extend(extra_symbols)
        tasks = []
        dates = get_dates(days)
        async with aiohttp.ClientSession() as session:
            for date in dates:
                tasks.append(get_exchange_for_date(session, date, symbols))
            results = await asyncio.gather(*tasks)
            print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    asyncio.run(main())
