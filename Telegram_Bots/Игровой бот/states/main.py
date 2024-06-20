from aiogram.dispatcher.filters.state import State, StatesGroup
class Rass(StatesGroup):

  post = State()
  kb = State()
  time = State()

class solve():
  nameCaptcha = ''

class dialog(StatesGroup):
  captcha = State()

class Srez(StatesGroup):
  bank = State()
  balance = State()
  rating = State()
  fantom = State()
  kazna = State()

class razzdacha(StatesGroup):
  post = State()
  summ = State()
  kb = State()
