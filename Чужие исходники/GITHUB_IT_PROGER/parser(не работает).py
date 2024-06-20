from bs4 import BeautifulSoup
import requests

url = 'https://www.avito.ru/ulyanovskaya_oblast/noutbuki?cd=1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
items = soup.findAll('div', class_='iva-item-body-KLUuy')

elements = []
try:
    for item in items:
        elements.append({
            'title': item.find('h3', class_='title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH text-text-LurtD text-size-s-BxGpL text-bold-SinUO ').get_text(strip=True),
            'price': item.find('span', class_='price-text-_YGDY text-text-LurtD text-size-s-BxGpL').get_text(strip=True),
            'link': item.find('a', class_='link-link-MbQDP link-design-default-_nSbv title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH ').get('href')
        })
        for element in elements:
            print(f'{element["title"]}\nЦена: {element["price"]}\nСсылка: {element["link"]}')
            print('=========' * 10)
except AttributeError:
    print("ERROR")