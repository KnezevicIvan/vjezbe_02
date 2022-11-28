from json import dumps

class Film:

    def __init__(self, id, naziv, godina):
        self.id = id
        self.naziv = naziv
        self.godina = godina
        self.posuden = False
        self.idKorisnika = None

    # def kreirajFilm(self, id, naziv, godina):
    #     self.id = id
    #     self.naziv = naziv
    #     self.godina = godina

    def __repr__(self):
        return dumps(self.__dict__, indent=4)
        #return str(self.__dict__)
        #return f"{self.id};{self.naziv};{self.godina}"