import asyncio

import aiohttp
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent

BASE_URL = "https://www.wildberries.ru/catalog/obuv/muzhskaya/kedy-i-krossovki"
HEADERS = {"User-Agent": UserAgent().random}

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, headers=HEADERS) as response:
            r = await aiohttp.StreamReader.read(response.content)
            soup = BS(r, "html.parser")

            items = soup.find_all("article", {"class": "product-card product-card--hoverable j-card-item"})
            for item in items:
                title = item.find("h2", {"class": "product-card__brand-wrap"}).text.strip()
                print(title)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())