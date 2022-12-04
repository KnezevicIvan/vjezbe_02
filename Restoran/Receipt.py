import random
from datetime import datetime as dt
from json import dumps


class Receipt:
    def __init__(self, id, table, order: list, total, payment, jir):
        self.id = id
        self.table = table
        self.order_list = order
        self.total = total
        self.payment = payment
        self.jir = jir

    # def __repr__(self):
    #     return dumps(self.__dict__, indent=4)

    def __repr__(self):
        receipt = {
            " Broj racuna": self.id,
            " Broj stola ": self.table,
            " Narudzba ": self.order_list,
            " Za platiti ": self.total,
            " JIR ": self.jir
        }
        return str(receipt)

    @staticmethod
    def jir(self):
        time = str(dt.now().timestamp())
        time_list = []
        for t in time:
            time_list.append(t)
        random.shuffle(time_list)
        jir = ""
        for i in  time_list:
            jir += i
        print(jir)
        return jir
