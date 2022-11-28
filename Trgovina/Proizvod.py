from json import dumps


class Proizvod:

    def __int__(self, id, naziv, cijena, kolicina):
        self.id = id
        self.naziv = naziv
        self.cijenaKN = cijena
        self.cijenaEUR = self.cijenaKN * 7.5
        self.kolicina = kolicina

    def __repr__(self):
        return dumps(self.__dict__, indent=4)

