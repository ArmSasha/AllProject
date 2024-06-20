"""

██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░ ░██████╗░█████╗░███████╗████████╗
██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗ ██╔════╝██╔══██╗██╔════╝╚══██╔══╝
██║░░░░░███████║██╔██╗██║█████╗░░██████╔╝ ╚█████╗░██║░░██║█████╗░░░░░██║░░░
██║░░░░░██╔══██║██║╚████║██╔══╝░░██╔══██╗ ░╚═══██╗██║░░██║██╔══╝░░░░░██║░░░
███████╗██║░░██║██║░╚███║███████╗██║░░██║ ██████╔╝╚█████╔╝██║░░░░░░░░██║░░░
╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝ ╚═════╝░░╚════╝░╚═╝░░░░░░░░╚═╝░░░

Работа с Lava.

"""

import requests

class LavaPayment(object):

    def __init__(self, token):
        self.token = token
        self.session = requests.session()
        self.session.headers.update({
            'Authorization' : self.token
        })


    def get_balance(self):
        response = self.session.get('https://api.lava.ru/wallet/list').json()

        result = ""

        for wallet in response:
            result += f"ID: {wallet['account']} {wallet['currency']} {wallet['balance']}\n"

        return result

    def check_payment(self, id : str):

        response = self.session.post('https://api.lava.ru/transactions/list',
                                     data={'type' : 'transfer', 'limit' : 1}
                                     ).json()

        for payment in response['items']:
            print(payment)

            if payment['id'] != id:
                continue

            if payment['transfer_type'] != 'transfer':
                continue

            if payment['type'] != 'in':
                continue

            return payment['id'], payment['amount']

        return False

    def create_payment(self, sum : float):
        response = self.session.get('https://api.lava.ru/wallet/list').json()

        for wallet in response:
            if wallet['currency'] != 'RUB':
                continue

            account = wallet['account']
            break

        data = {
            'wallet_to' : account,
            'sum' : sum,
            'expire' : 3600,
            'subtract' : '1'
        }
        response = self.session.post('https://api.lava.ru/invoice/create', data=data).json()

        return response['id'], response['url']
