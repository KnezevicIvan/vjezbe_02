from Hrana import Hrana
from Pice import Pice
from Stol import Stol

class Restoran:

    def __init__(self):
        self.listaHrane = [[], [], []]
        self.listaPica = [[], []]
        self.listaStolova = []
        self.listaRacuna = []

    def dodajPredjelo(self, predjelo: Hrana):
        self.listaHrane[0].append(predjelo)

    def dodajGlavoJelo(self, glavnoJelo: Hrana):
        self.listaHrane[1].append(glavnoJelo)

    def dodajDesert(self, desert: Hrana):
        self.listaHrane[2].append(desert)

    def ispisHrane(self, n):            # 0 predjelo, 1 glavno jelo, 2 desert
        for h in self.listaHrane[n]:
            print(h)

    def dodajBezalkoholnoPice(self, bezalkoholno: Pice):
        self.listaPica[0].append(bezalkoholno)

    def dodajAlkoholnoPice(self, alkoholno: Pice):
        self.listaPica[1].append(alkoholno)

    def ispisPica(self, n):             # 0 bezalkoholno, 1 alkoholno
        for p in self.listaPica[n]:
            print(p)

    def dodajStol(self, stol: Stol):
        self.listaStolova.append(stol)

    def ispisStolova(self):
        for s in self.listaStolova:
            print(s)