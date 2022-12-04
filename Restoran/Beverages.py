from json import dumps


class Beverages:
    def __init__(self, id, name, price, alcohol):
        self.id = id
        self.name = name
        self.price = price
        self.alcohol = alcohol

    def __repr__(self):
        return dumps(self.__dict__, indent=4)

    # def __repr__(self):
    #     model = {
    #         " ID pica ": self.id,
    #         " Naziv pica ": self.name,
    #         " Cijena pica ": self.price,
    #         " Vrsta ": self.alcohol
    #     }
    #     return model
