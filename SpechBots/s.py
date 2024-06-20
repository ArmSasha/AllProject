import bs4
import requests
z=''
s=requests.get('http://anekdot.ru/random')
b=bs4.BeautifulSoup(s.text, "html.parser")
p=b.select('.a_rnd')
for x in p:
    s=(x.getText().strip())

print(s)
