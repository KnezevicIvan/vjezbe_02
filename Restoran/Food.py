from json import dumps


class Food:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __repr__(self):
        return dumps(self.__dict__, indent=4)
