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
    id_appetizer = len(service.restoran.food_list[0]) + 1
    id_main_course = len(service.restoran.food_list[1]) + 1
    id_dessert = len(service.restoran.food_list[2]) + 1
    id_non_alcohol_drinks = len(service.restoran.drinks_list[0]) + 1
    id_alcohol_drinks = len(service.restoran.drinks_list[0]) + 1
    id_table = len(service.restoran.table_list) + 1

    while True:
        Utils.ispisiIzbornik(main_menu)
        user_input = input("Odaberi opciju: ")
        if user_input == 0:
            print("Izlazim iz programa.")
            break
        elif user_input == 1:           # order food
            pass
        elif user_input == 2:           # order drinks
            pass
        elif user_input == 3:           # tables
            pass
        elif user_input == 4:           # administration
            while True:
                user_input_2 = input("Odaberi opciju: ")
                if user_input_2 == 0:
                    break
                elif user_input_2 == 1:     # add appetizer
                    id_appetizer = service.add_appetizer(id_appetizer)
                elif user_input_2 == 2:     # add main course
                    id_main_course = service.add_main_course(id_main_course)
                elif user_input_2 == 3:     # add dessert
                    id_dessert = service.add_dessert(id_dessert)
                elif user_input_2 == 4:     # add non alcoholic drink
                    id_non_alcohol_drinks = service.add_non_alcohol_drink(id_non_alcohol_drinks)
                elif user_input_2 == 5:     # add alcoholic drink
                    id_alcohol_drinks = service.add_alcohol_drink(id_alcohol_drinks)
                elif user_input_2 == 6:     # add table
                    id_table = service.add_table(id_table)
                elif user_input_2 == 7:     # print receipts
                    pass
        else:
            print("Krivi unos!")

