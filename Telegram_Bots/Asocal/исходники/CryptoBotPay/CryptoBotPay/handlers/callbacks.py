'''https://t.me/AGOMarketBot - Маркет в Telegram'''
from aiocryptopay import AioCryptoPay
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hlink

from data.config import CRYPTO_PAY_TOKEN, ADMINS_ID
from keyboards.inline.payments_kb import payment_methods_kb, back_to_add_balance_kb, crypto_bot_currencies_kb, \
    check_crypto_bot_kb
from keyboards.inline.start_kb import start_kb
from states import CryproBot
from utils.cryptobot_pay import get_crypto_bot_sum, check_crypto_bot_invoice
from utils.db_commands import DataBase


async def back_to_start(call: types.CallbackQuery):
    db = DataBase()
    await db.user.register_user(call.from_user.id)
    user = await db.user.select_user(call.from_user.id)

    await call.message.edit_text(
        f'<b>👋 Добро пожаловать в Shop Bot!</b>\n'
        f'<b>🆔:</b> <code>{call.from_user.id}</code>\n'
        f'<b>💵 Баланс:</b> <b>{user.balance} $</b>',
        reply_markup=start_kb
    )


async def add_balance(call: types.CallbackQuery):
    await call.message.edit_text(
        '<b>💳 Выберите способ пополнения:</b>',
        reply_markup=payment_methods_kb
    )


async def crypto_bot_pay(call: types.CallbackQuery):
    await call.message.edit_text(
        f'<b>{hlink("⚜️ CryptoBot", "https://t.me/CryptoBot")}</b>\n\n'
        '— Минимум: <b>0.1 $</b>\n\n'
        f'<b>💸 Введите сумму пополнения в долларах</b>',
        disable_web_page_preview=True,
        reply_markup=back_to_add_balance_kb
    )
    await CryproBot.sum.set()


async def crypto_bot_sum(message: types.Message, state: FSMContext):
    try:
        if float(message.text) >= 0.1:
            await message.answer(
                f'<b>{hlink("⚜️ CryptoBot", "https://t.me/CryptoBot")}</b>\n\n'
                f'— Сумма: <b>{message.text} $</b>\n\n'
                '<b>💸 Выберите валюту, которой хотите оплатить счёт</b>',
                disable_web_page_preview=True,
                reply_markup=crypto_bot_currencies_kb()
            )
            await state.update_data(crypto_bot_sum=float(message.text))
            await CryproBot.currency.set()
        else:
            await message.answer(
                '<b>⚠️ Минимум: 0.1 $!<b>'
            )
    except ValueError:
        await message.answer(
            '<b>❗️Сумма для пополнения должна быть в числовом формате!</b>'
        )


async def crypto_bot_currency(call: types.CallbackQuery, state: FSMContext):
    try:
        await call.message.delete()
        data = await state.get_data()
        db = DataBase()
        cryptopay = AioCryptoPay(CRYPTO_PAY_TOKEN)
        invoice = await cryptopay.create_invoice(
            asset=call.data.split('|')[1],
            amount=await get_crypto_bot_sum(
                data['crypto_bot_sum'],
                call.data.split('|')[1]
            )
        )
        await cryptopay.close()
        await state.update_data(crypto_bot_currency=call.data.split('|')[1])
        await db.payments.add_new_payment(invoice.invoice_id, data['crypto_bot_sum'])
        await call.message.answer(
            f'<b>💸 Отправьте {data["crypto_bot_sum"]} $ {hlink("по ссылке", invoice.pay_url)}</b>',
            reply_markup=check_crypto_bot_kb(invoice.pay_url, invoice.invoice_id)
        )
        await state.reset_state(with_data=False)
    except Exception:
        await call.message.answer(
            '<b>⚠️ Произошла ошибка!</b>'
        )


async def check_crypto_bot(call: types.CallbackQuery):
    db = DataBase()
    payment = await db.payments.select_payment(int(call.data.split('|')[1]))
    if payment:
        if await check_crypto_bot_invoice(int(call.data.split('|')[1])):
            await db.payments.delete_payment(int(call.data.split('|')[1]))
            await db.payments.update_balance(call.from_user.id, payment.summa)

            await call.answer(
                '✅ Оплата прошла успешно!',
                show_alert=True
            )
            await call.message.delete()
            await call.message.answer(
                f'<b>💸 Ваш баланс пополнен на сумму {payment.summa} $!</b>'
            )

            for admin in ADMINS_ID:
                await call.bot.send_message(
                    admin,
                    f'<b>{hlink("⚜️ CryptoBot", "https://t.me/CryptoBot")}</b>\n'
                    f'<b>💸 Обнаружено пополнение от @{call.from_user.username} [<code>{call.from_user.id}</code>] '
                    f'на сумму {payment.summa} $!</b>'
                )
        else:
            await call.answer(
                '❗️ Вы не оплатили счёт!',
                show_alert=True
            )


async def cancel_handler(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer('❌')
    await state.reset_state(with_data=False)


def register_callbacks(dp: Dispatcher):
    dp.register_callback_query_handler(back_to_start, Text('back_to_start'), state='*')
    dp.register_callback_query_handler(add_balance, Text('add_balance'), state='*')
    dp.register_callback_query_handler(crypto_bot_pay, Text('crypto_bot'), state='*')
    dp.register_message_handler(crypto_bot_sum, state=CryproBot.sum)
    dp.register_callback_query_handler(
        crypto_bot_currency, Text(startswith='crypto_bot_currency'), state=CryproBot.currency
    )
    dp.register_callback_query_handler(check_crypto_bot, Text(startswith='check_crypto_bot'), state='*')
    dp.register_callback_query_handler(cancel_handler, Text('cancel'), state='*')
