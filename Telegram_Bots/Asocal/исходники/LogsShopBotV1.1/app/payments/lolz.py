"""

██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░ ░██████╗░█████╗░███████╗████████╗
██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗ ██╔════╝██╔══██╗██╔════╝╚══██╔══╝
██║░░░░░███████║██╔██╗██║█████╗░░██████╔╝ ╚█████╗░██║░░██║█████╗░░░░░██║░░░
██║░░░░░██╔══██║██║╚████║██╔══╝░░██╔══██╗ ░╚═══██╗██║░░██║██╔══╝░░░░░██║░░░
███████╗██║░░██║██║░╚███║███████╗██║░░██║ ██████╔╝╚█████╔╝██║░░░░░░░░██║░░░
╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝ ╚═════╝░░╚════╝░╚═╝░░░░░░░░╚═╝░░░

Работа с Lolz Market.

"""

import requests


class LolzPayment(object):

    def __init__(self, token : str, host = "https://api.lolz.guru/"):
        self.token = token
        self.host = host
        self.session = requests.session()
        self.session.headers = {
            'Authorization': f'Bearer {self.token}'
        }

        response = self.session.get(self.host + f'market/me').json()
        if 'user' not in response:
            raise("Ошибка авторизации lolz, проверьте правильность введененых данных.")

    def me(self):
        response = self.session.get(self.host + f'market/me').json()['user']
        self.user_id = response['user_id']
        return response

    def check_payment(self, comment : str, amount : str):
        data = {
            'type' : 'receiving_money',
            'is_hold' : 'no',
            'comment' : comment,
            'pmin' : amount
        }

        response = self.session.get(self.host + f'market/user/{self.user_id}/payments', params=data).json()
        for payment in response['payments']:

            info = response['payments'][payment]

            if info['operation_type'] != 'receiving_money':
                continue

            if info['incoming_sum'] != int(amount):
                continue

            if info['is_hold'] != 0:
                continue

            if info['is_finished'] != 1:
                continue

            if info['data']['comment'] != comment:
                continue

            return comment, amount

        return False
