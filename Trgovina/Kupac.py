from json import dumps

class Kupac:

    def __int__(self, id, ime, prezime):
        self.id = id
        self.ime = ime
        self.prezime = prezime

    def __repr__(self):
        return dumps(self, indent=4)