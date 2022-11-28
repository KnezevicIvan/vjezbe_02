from json import dumps

class Stol:
    def __init__(self, id, rezervacija = False):
        self.id = id
        self.rezervacija = rezervacija

    def __repr__(self):
        return dumps(self.__dict__, indent=4)