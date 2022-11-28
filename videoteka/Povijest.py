from json import dumps
from datetime import datetime as dt
from enum import Enum


class PovijestAkcija(Enum):
    posudi = "POSUDEN"
    vrati = "VRACEN"


class Povijest:

    def __init__(self, korisnikId, filmId, akcija):
        self.korisnikId = korisnikId
        self.filmId = filmId
        self.akcija = akcija
        self.datum = f"{dt.now().year}-{dt.now().month}-{dt.now().day}"


    def __repr__(self):
        return dumps(self.__dict__, indent=4)