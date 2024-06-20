"""

██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░ ░██████╗░█████╗░███████╗████████╗
██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗ ██╔════╝██╔══██╗██╔════╝╚══██╔══╝
██║░░░░░███████║██╔██╗██║█████╗░░██████╔╝ ╚█████╗░██║░░██║█████╗░░░░░██║░░░
██║░░░░░██╔══██║██║╚████║██╔══╝░░██╔══██╗ ░╚═══██╗██║░░██║██╔══╝░░░░░██║░░░
███████╗██║░░██║██║░╚███║███████╗██║░░██║ ██████╔╝╚█████╔╝██║░░░░░░░░██║░░░
╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝ ╚═════╝░░╚════╝░╚═╝░░░░░░░░╚═╝░░░

Работа с Crystal Pay

"""

import requests


class CrystalPay(object):

    def __init__(self,
                 login : str,
                 secret_key_1 : str):

        self.login = login
        self.secret_key_1 = secret_key_1

        response = requests.get('https://api.crystalpay.ru/v1/?s={}&n={}&o=balance'.format(
            self.secret_key_1,
            self.login
        )).json()

        if response['auth'] == 'error':
            raise ("Ошибка авторизации crystal pay, проверьте правильность введененых данных.")

    def get_balance(self):
        response = requests.get('https://api.crystalpay.ru/v1/?s={}&n={}&o=balance'.format(
            self.secret_key_1,
            self.login)).json()['balance']

        crystalpaybalances_result = ""
        for balance in response:
            crystalpaybalances_result += balance + " " + str(response[balance]) + "\n"

        return crystalpaybalances_result

    def generate_pay_link(self, amount):
        response = requests.get('https://api.crystalpay.ru/v1/?s={}&n={}&o=invoice-create&lifetime=3600&amount={}'.format(
            self.secret_key_1,
            self.login,
            amount)).json()

        return response['id'], response['url']

    def get_pay_status(self, pay_id):
        response = requests.get('https://api.crystalpay.ru/v1/?s={}&n={}&o=invoice-check&i={}'.format(
            self.secret_key_1,
            self.login,
            pay_id)).json()

        if response['state'] != 'payed':
            return False

        return pay_id, response['amount']