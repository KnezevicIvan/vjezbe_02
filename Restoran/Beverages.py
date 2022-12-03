from json import dumps

class Beverages:
    def __init__(self, id, name, price, alcohol: bool):
        self.id = id
        self.name = name
        self.price = price
        self.alcohol = alcohol

    def __repr__(self):
        return dumps(self.__dict__, indent=4)
