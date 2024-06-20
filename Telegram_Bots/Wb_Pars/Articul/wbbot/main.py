import logging
import re
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests

logging.basicConfig(level=logging.INFO)

bot_token = '123456'
bot = Bot(token=bot_token, parse_mode='HTML')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    reply_text = "Привет! Я телеграм-бот, который поможет тебе найти товар на Wildberries. Для начала работы отправь мне артикул товара."
    await message.answer(reply_text)

async def search_product(product_code):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    search_url = f'https://www.wildberries.ru/catalog/{product_code}/detail.aspx'
    driver.get(search_url)
    wait = WebDriverWait(driver, 10)
    price_elem = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'price-block__final-price')))
    
    product_price = price_elem.text.split()[0]
    product_name_elem = driver.find_element(By.CLASS_NAME, 'product-page__header')
    desc_elem = driver.find_element(By.CLASS_NAME, 'collapsable__text')
    product_name = product_name_elem.text.strip()
    product_desc =desc_elem.text
    product_url = driver.current_url
    message_texts = f"""
<b> 🛍 Товар:</b> {product_name}

<b>💰 Цена:</b> {product_price}₽

<b>📖 Описание</b>
<i>{product_desc}</i>

<b>🔗 Ссылка на товар:</b> <a href='{product_url}'>перейти</a>"""
    driver.quit()
    return message_texts

@dp.message_handler(content_types=['text'])
async def handle_text(message: types.Message):
    product_code = message.text
    message_texts = await search_product(product_code)
    await message.answer(message_texts)

if __name__ == '__main__':
    asyncio.run(dp.start_polling())
