from Osoba import Osoba

class Predavac(Osoba):

    def __init__(self, id, ime, prezime):
        super().__init__(id, ime, prezime)
        self.id_predavaca = None



predavac = Predavac(1, "Pero", "Peric")
predavac.unesiOib(12312312312)
print(predavac)