from bs4 import BeautifulSoup as BS
import requests
import csv


# HOST = "https://www.anekdot.ru/"
URL = "https://www.anekdot.ru/random/anekdot/"

HEADERS = {
	"accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	"user-agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0'
}

req = requests.get(URL, headers=HEADERS)
src= req.text
soup = BS(src, 'html.parser')

anek = []

all_anek = soup.find_all(class_='topicbox')
for item in all_anek:
	item_text = item.text
	print(f"{item_text}")

# print(src)



# def get_html(url):
# 	r = requests.get(url, headers=HEADERS)
# 	return r

# def get_content(html):
# 	soup = BS(html, 'html.parser')
# 	items = soup.find(class_='topicbox').find_all(class_='text')
# 	for item in items:
# 		print(item.text())
# 	# items = soup.find_all('div', class_ ='topicbox')
# 	# anek = []
# 	# for item in items:
# 	# 	anek.append(
# 	# 		{
# 	# 			'content':item.find('div', class_ = 'text').get_text()
# 	# 		}
# 	# 	)
# 	# return anek



# html = get_html(URL)
# print(get_content(html.text))