from Restoran import Restoran
from Utils import Utils
from Hrana import Hrana
from Pice import Pice
from Stol import Stol


class RestoranService:

    def __init__(self):
        self.restoran = Restoran()

    def dodajPredjelo(self, idPredjelo):
        predjelo: Hrana = Hrana(Utils.dodajZnamenke(idPredjelo, 2), input("Naziv predjela:"), Utils.unesiCijeliBroj("Cijena: "))
        self.restoran.dodajPredjelo(predjelo)
        return idPredjelo + 1

    def dodajGlavnoJelo(self, idGlavnoJelo):
        glavnoJelo: Hrana = Hrana(Utils.dodajZnamenke(idGlavnoJelo, 2), input("Naziv jela:"), Utils.unesiCijeliBroj("Cijena: "))
        self.restoran.dodajGlavoJelo(glavnoJelo)
        return idGlavnoJelo + 1

    def dodajDesert(self, idDesert):
        desert: Hrana = Hrana(Utils.dodajZnamenke(idDesert, 2), input("Naziv deserta:"), Utils.unesiCijeliBroj("Cijena: "))
        self.restoran.dodajDesert(desert)
        return idDesert + 1

    def dodajBezalkoholnoPice(self, idBezalkoholno):
        bezalkoholno: Pice = Pice(Utils.dodajZnamenke(idBezalkoholno, 2), input("Naziv pica:"), Utils.unesiCijeliBroj("Cijena: "))
        self.restoran.dodajBezalkoholnoPice(bezalkoholno)
        return idBezalkoholno + 1

    def ispisHrane(self):
        print("-------Predjelo-------")
        self.restoran.ispisHrane(0)
        print("-------Glavno jelo-------")
        self.restoran.ispisHrane(1)
        print("-------Desert-------")
        self.restoran.ispisHrane(2)

    def dodajAlkoholnoPice(self, idAlkoholno):
        alkoholno: Pice = Pice(Utils.dodajZnamenke(idAlkoholno, 2), input("Naziv pica:"), Utils.unesiCijeliBroj("Cijena: "))
        self.restoran.dodajAlkoholnoPice(alkoholno)
        return idAlkoholno + 1

    def ispisPica(self):
        print("-------Bezalkoholna pica-------")
        self.restoran.ispisPica(0)
        print("-------Glavno jelo-------")
        self.restoran.ispisPica(1)

    def dodajStol(self, idStol):
        stol: Stol = Stol(Utils.dodajZnamenke(idStol, 2))
        self.restoran.dodajStol(stol)
        return idStol + 1

    def ispisStolova(self):
