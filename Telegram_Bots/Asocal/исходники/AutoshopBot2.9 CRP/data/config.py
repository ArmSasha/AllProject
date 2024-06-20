# - *- coding: utf- 8 - *-
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")
BOT_TOKEN = config["settings"]["token"]
admins = config["settings"]["admin_id"]
crystal_name = config["crystal"]["nickname"]
crystal_secret = config["crystal"]["secret_1"]
payments_enabled = config["payments"]["enabled"]

payments_enabled = payments_enabled.replace(" ", "").split(",")

if len(payments_enabled) == 0:
    print("❌ Вы не указали включенные платёжные системы! Укажите хотя бы одну!")

if "," in admins:
    admins = admins.replace(" ", "").split(",")
else:
    if len(admins) >= 1:
        admins = [admins]
    else:
        admins = []
        print("❌ Вы не указали администраторов бота!")

bot_version = "2.9"
bot_description = f"<b>♻ Bot created by @djimbox</b>\n" \
                  f"<b>⚜ Bot Version:</b> <code>{bot_version}</code>\n" \
                  f"<b>🔗 Topic Link:</b> <a href='https://lolz.guru/threads/1888814/'><b>Click me</b></a>\n" \
                  f"<b>🍩 Donate to the author:</b> <a href='https://yoomoney.ru/to/410012580032553'><b>Click me</b></a>" \
                  f"\n" \
                  f"\n⚙ Mod by jspring"
