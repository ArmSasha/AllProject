'''https://t.me/AGOMarketBot - Маркет в Telegram'''
from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from utils.database import get_session
from utils.schemas import User, Payments


class DataBase:
    def __init__(self):
        self.user = DBUser()
        self.payments = DBPayments()


class DBUser:
    @staticmethod
    async def register_user(user_id: int):
        user = User(
            user_id=user_id
        )
        async with get_session() as session:
            session.add(user)
            try:
                await session.commit()
            except IntegrityError:
                await session.rollback()

    @staticmethod
    async def select_user(user_id: int):
        async with get_session() as session:
            user = await session.execute(select(User).where(User.user_id == user_id))
            return user.scalar()

    @staticmethod
    async def update_balance(user_id: int, balance: float):
        async with get_session() as session:
            user = update(User).where(User.user_id == user_id).values({User.balance: User.balance + balance})
            await session.execute(user)
            await session.commit()


class DBPayments:
    @staticmethod
    async def add_new_payment(payment_id: int, summa: float):
        payment = Payments(
            payment_id=payment_id,
            summa=summa
        )
        async with get_session() as session:
            session.add(payment)
            try:
                await session.commit()
            except IntegrityError:
                await session.rollback()

    @staticmethod
    async def select_payment(payment_id: int):
        async with get_session() as session:
            payment = await session.execute(select(Payments).where(Payments.payment_id == payment_id))
            return payment.scalar()

    @staticmethod
    async def delete_payment(payment_id: int):
        async with get_session() as session:
            payment = delete(Payments).where(Payments.payment_id == payment_id)
            await session.execute(payment)
            await session.commit()
