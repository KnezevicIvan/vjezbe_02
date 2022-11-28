from json import dumps

class Kupovina:

    def __int__(self, id, nazivProizvoda, cijenaProizvoda, kolicina):
        self.id = id
        self.naziv = nazivProizvoda
        self.cijena = cijenaProizvoda
        self.kolicina = kolicina
        self.ukupno = self.cijena * self.ukupno