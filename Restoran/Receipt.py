import random
from datetime import datetime as dt
from json import dumps
class Receipt():

    def __init__(self, id, table, order, total, payment, jir):
        self.id = id
        self.table = table
        self.order_list = order
        self.total = total
        self.payment = payment
        self.jir = jir


    def __repr__(self):
        return dumps(self.__dict__, indent=4)


    @staticmethod
    def jir(self):
        time = str(dt.now().timestamp())
        time_list = []
        for t in time:
            time_list.append(t)
        random.shuffle(time_list)
        jir = str(time_list)
        return jir

