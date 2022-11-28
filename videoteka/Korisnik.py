from datetime import datetime as dt
from json import dumps

class Korisnik:

    def __init__(self, id, ime, prezime):
        self.id = id
        self.ime = ime
        self.prezime = prezime
        self.created = int(dt.now().timestamp())

    def __repr__(self):
        model = {
            "id": self.id,
            "ime": self.ime,
            "prezime": self.prezime,
            "created": self.timestampUredeno(self.created, "%Y-%m-%d")
        }
        return dumps(model, indent=4)
