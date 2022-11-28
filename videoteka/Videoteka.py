from json import dumps
from Film import Film
from Korisnik import Korisnik
from Povijest import Povijest

class Videoteka:

    # konstruktor klase
    def __init__(self):
        self.listaKorisnika = []
        self.listaFilmova = []
        self.listaPovijest = []

    def dodajFilm(self, film: Film):
        # u listu filmova dodaj film
        self.listaFilmova.append(film)

    def ispisiFilmove(self):
        for f in self.listaFilmova:
            print(f)

    def dodajKorisnika(self, korisnik: Korisnik):
        self.listaKorisnika.append(korisnik)

    def ispisiKorisnike(self):
        for k in self.listaKorisnika:
            print(k)

    def dodajPovijest(self, povijest: Povijest):
        self.listaPovijest.append(povijest)

    def ispisiPovijest(self):
        for p in self.listaPovijest:
            print(p)

    def dohvatiKorinikaPoIDu(self, id):
        for k in self.listaKorisnika:
            if k.id == id:
                return k
        return None

    def dohvatiFilmPoIDu(self, id):
        for f in self.listaFilmova:
            if f.id == id:
                return f
        return None




