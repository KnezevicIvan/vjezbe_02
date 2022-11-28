from json import dumps

class Hrana:
    def __init__(self, id, naziv, cijena):
        self.id = id
        self.naziv = naziv
        self.cijena = cijena

    def __repr__(self):
        return dumps(self.__dict__, indent=4)
