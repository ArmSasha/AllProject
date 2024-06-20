import telebot
import requests
from bs4 import BeautifulSoup as BS
import rich
from pprint import pprint
import datetime

#bot
bot = telebot.TeleBot('1739386190:AAHFRmJbHnCcE6NK1rMqOF9vMaiklw7PBP4')

open_weather_token = "6d7ca3dd357cb822c17e517f7fc2226d"

r = requests.get('https://sinoptik.ua/погода-ульяновск')
html = BS(r.content, 'html.parser')

Corona = 'https://www.worldometers.info/coronavirus/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

full_page = requests.get(Corona,headers=headers)
soup = BS(full_page.content,'html.parser')

convert = soup.findAll("div",{"class":"maincounter-number"})





#___________________________________________________________________________________________
#												WEATHER
#___________________________________________________________________________________________

def get_weather(city, open_weather_token):

    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что там за погода!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])
        @bot.message_handler(commands = ['weather'])
        def weather(message):
            bot.send_message(message.from_user.id, f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                  f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n"
                  f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
                  f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
                  f"Хорошего дня!"
                  )

    except Exception as ex:
        print(ex)
        print("Проверьте название города")
#___________________________________________________________________________________________



#___________________________________________________________________________________________
#                                               KORONA
#___________________________________________________________________________________________

    @bot.message_handler(commands = ['korona'])
    def korona(message):
        bot.send_message(message.from_user.id, f"Заражённых: {convert[0].tex} \n Умерших: {convert[1].text} \n Вылечиных: {convert[2].text}")
#___________________________________________________________________________________________



















#___________________________________________________________________________________________
#                                               STOP
#___________________________________________________________________________________________

    @bot.message_handler(commands = ['stop'])
    def stop(message):
        bot.send_message(message.from_user.id, 'Ok' )
        print("Stop")
        bot.stop_polling()
#___________________________________________________________________________________________






def main():
    city = 'Ульяновск'
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()



#polling
bot.polling(none_stop=False, interval=0)