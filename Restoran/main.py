"""menu podjeliti na segmente:
jela,alkoholna,bezalkoholna pića(dodatne podvrste po želji)

omoguciti unos u meni (svaki od segmenata)
omoguciti narucivanje - vise stvari
izrada racuna prema narudzbi
placanje - keš/kartica
dostupni stolovi - rezervacija

restoran mora cuvati sve racune

sve zamisli za prosirenje aplikacije po izboru.
Rijesavati sa klasama.
osmisliti metodu za fiskalizaciju racuna (neki kod po želji, polu nasumican), racun se fiskalizira kod placanja """

from RestoranService import RestoranService
from Utils import Utils



if __name__ == '__main__':
    service = RestoranService()
    idPredjelo = 1
    idGlavnoJelo = 1
    idDesert = 1
    idBezalkoholno = 1
    idAlkoholno = 1

    while True:
        idPredjelo = service.dodajPredjelo(idPredjelo)
        idGlavnoJelo = service.dodajGlavnoJelo(idGlavnoJelo)
        idDesert = service.dodajDesert(idDesert)

        service.ispisHrane()