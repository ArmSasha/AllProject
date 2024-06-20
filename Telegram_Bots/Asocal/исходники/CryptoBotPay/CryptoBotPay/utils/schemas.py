'''https://t.me/AGOMarketBot - Маркет в Telegram'''
from sqlalchemy import Column, Integer, Float, String, BIGINT

from utils.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_id = Column(BIGINT, unique=True)
    balance = Column(Float, default=0.0)


class Payments(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    payment_id = Column(BIGINT)
    summa = Column(Float)
