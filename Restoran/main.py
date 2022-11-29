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

main_menu = {
    0: " izlaz",
    1: " --- Naruci hranu ---",
    2: " --- Naruci pice ---",
    3: " --- Stolovi ---",
    4: " --- Administracija ---"
}

admin_menu = {
    0: " -- Povratak --",
    1: " -- Dodaj predjelo --",
    2: " -- Dodaj glavno jelo --",
    3: " -- Dodaj desert --",
    4: " -- Dodaj bezalkoholno pice --",
    5: " -- Dodaj alkoholno pice --",
    6: " -- Dodaj stol --",
    7: " -- Ispisi racune --"
}

if __name__ == '__main__':
    service = RestoranService()
    id_appetizer = 1
    id_main_course = 1
    id_dessert = 1
    id_non_alcohol_drinks = 1
    id_alcohol_drinks = 1
    id_table = 1

    while True:
        id_appetizer = service.add_appetizer(id_appetizer)
        id_main_course = service.add_main_course(id_main_course)
        id_dessert = service.add_dessert(id_dessert)

        service.print_food()

