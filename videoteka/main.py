from VideotekaService import VideotekaService
from Utils import Utils
from Povijest import PovijestAkcija

izbornik = {
    0: "Izlaz iz aplikacije",
    1: "Upis filma",
    2: "Upis korisnika",
    3: "Posudi film",
    4: "Vrati film",
    5: "Ispis videoteke"
}

if __name__ == '__main__':
    service = VideotekaService()
    idFilma = 1
    idKorisnika = 1
    while True:
        Utils.ispisiIzbornik(izbornik)

        unos = input("Unesite opciju: ")

        if unos == "0":
            print("Izlaz iz aplikacije...")
            break
        elif unos == "1":
            # Unos filma
            idFilma = service.dodajFilm(idFilma)
        elif unos == "2":
            # Unos korisnika
            idKorisnika = service.dodajKorisnika(idKorisnika)
        elif unos == "3":
            # Posudi film
            service.akcijaFilm(PovijestAkcija.posudi)
        elif unos == "4":
            # Vrati film
            service.akcijaFilm(PovijestAkcija.vrati)
        elif unos == "5":
            # Ispis
            service.ispisi()
        else:
            print("Opcija ne postoji")



