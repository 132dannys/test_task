import aiohttp
import asyncio
import openpyxl

from .dataclasses import Product


def create_api_url(code):
    volume = int(code)//10**5
    part = int(code)//10**3

    def create_host(volume):
        if 0 <= volume <= 143:
            return '//basket-01.wb.ru'
        elif 144 <= volume <= 287:
            return '//basket-02.wb.ru'
        elif 288 <= volume <= 431:
            return '//basket-03.wb.ru'
        elif 432 <= volume <= 719:
            return '//basket-04.wb.ru'
        elif 720 <= volume <= 1007:
            return '//basket-05.wb.ru'
        elif 1008 <= volume <= 1061:
            return '//basket-06.wb.ru'
        elif 1062 <= volume <= 1115:
            return '//basket-07.wb.ru'
        elif 1116 <= volume <= 1169:
            return '//basket-08.wb.ru'
        elif 1170 <= volume <= 1313:
            return '//basket-09.wb.ru'
        elif 1314 <= volume <= 1601:
            return '//basket-10.wb.ru'
        elif 1602 <= volume <= 1655:
            return '//basket-11.wb.ru'
        else:
            return '//basket-12.wb.ru'
    
    return f'https:{create_host(volume)}/vol{volume}/part{part}/{code}/info/ru/card.json'

async def get_api_info(code, session):
    try:
        async with session.get(create_api_url(code)) as response:
            result = Product.parse_obj(await response.json()).dict()
    except Exception as e:
        result = {'Error': 'Its just error message'}
    return result

def parse_xlsx(file):
    book = openpyxl.open(file, read_only=True)
    sheet = book.active
    codes = []

    for row in range(1, sheet.max_row+1):
        codes.append(sheet[row][0].value)

    return codes    

async def get_api_info_codes(codes):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for code in codes:
            task = asyncio.create_task(get_api_info(code, session))
            tasks.append(task)

        results = await asyncio.gather(*tasks)

    return results        
