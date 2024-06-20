"""

██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░ ░██████╗░█████╗░███████╗████████╗
██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗ ██╔════╝██╔══██╗██╔════╝╚══██╔══╝
██║░░░░░███████║██╔██╗██║█████╗░░██████╔╝ ╚█████╗░██║░░██║█████╗░░░░░██║░░░
██║░░░░░██╔══██║██║╚████║██╔══╝░░██╔══██╗ ░╚═══██╗██║░░██║██╔══╝░░░░░██║░░░
███████╗██║░░██║██║░╚███║███████╗██║░░██║ ██████╔╝╚█████╔╝██║░░░░░░░░██║░░░
╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝ ╚═════╝░░╚════╝░╚═╝░░░░░░░░╚═╝░░░

Работа с чтением конфига.

"""

import configparser

class Config():

    def __init__(self):
        self.cfg = configparser.ConfigParser()
        self.cfg.read('config.ini', encoding='utf8')

        self.telegram_settings = self.cfg['TELEGRAM SETTINGS']
        self.telegram_settings_token = self.telegram_settings['token']
        self.telegram_settings_admin_id = self.telegram_settings['admin_id']
        self.telegram_settings_parse_mode = self.telegram_settings['parse_mode']
        self.telegram_settings_channel_id = self.telegram_settings['channel_id']

        self.payment_settings = self.cfg['PAYMENT SETTINGS']
        self.payment_settings_qiwi_p2p_token = self.payment_settings['qiwi_p2p_token']
        self.payment_settings_crystal_pay_login = self.payment_settings['crystal_pay_login']
        self.payment_settings_crystal_pay_secret_1 = self.payment_settings['crystal_pay_secret_1']
        self.payment_settings_lava_token = self.payment_settings['lava_token']
        self.payment_settings_lolz_token = self.payment_settings['lolz_token']
        self.payment_settings_minimal_amount  = self.payment_settings['minimal_amount']
