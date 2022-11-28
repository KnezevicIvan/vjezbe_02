from json import dumps

class Racun:

    def __init__(self):
        self.total = 0

    def __int__(self, idKupca, imeKupca, kupovina):
        self.idKupca = idKupca
        self.imeKupca = imeKupca
        self.kupovina = kupovina
        self.total = self.total + self.kupovina.ukupno