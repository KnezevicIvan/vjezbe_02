from Restoran import Restoran
from Utils import Utils
from Food import Food
from Beverages import Beverages
from Table import Table
from Receipt import Receipt


class RestoranService:

    def __init__(self):
        self.restoran = Restoran()

    def add_appetizer(self, id_appetizer):
        appetizer: Food = Food(Utils.dodajZnamenke(id_appetizer, 2),
                               input(" -- Naziv predjela: "),
                               Utils.unesiCijeliBroj(" -- Cijena: "))
        self.restoran.add_appetizer(appetizer)
        return id_appetizer + 1

    def add_main_course(self, id_main_course):
        main_course: Food = Food(Utils.dodajZnamenke(id_main_course, 2),
                                 input(" -- Naziv jela:"),
                                 Utils.unesiCijeliBroj(" -- Cijena: "))
        self.restoran.add_main_course(main_course)
        return id_main_course + 1

    def add_dessert(self, id_dessert):
        dessert: Food = Food(Utils.dodajZnamenke(id_dessert, 2),
                             input(" -- Naziv deserta: "),
                             Utils.unesiCijeliBroj(" -- Cijena: "))
        self.restoran.add_dessert(dessert)
        return id_dessert + 1

    def print_food(self):
        print("-------Predjelo-------")
        self.restoran.print_food(0)
        print("-------Glavno jelo-------")
        self.restoran.print_food(1)
        print("-------Desert-------")
        self.restoran.print_food(2)

    def order_food(self):
        order_list = []
        while True:
            menu_choice = Utils.unesiCijeliBroj("-- 1 predjelo, 2 glavno jelo, 3 desert, 0 povratak: ")
            if menu_choice == 1:            # appetizer
                while True:
                    self.restoran.print_food(0)
                    id_input = input(" -- Upisi id predjela: ")
                    if id_input == "0":
                        break
                    else:
                        appetizer = self.restoran.get_appetizer(id_input)
                        if appetizer:
                            order_list.append(appetizer)
                        else:
                            print(" # # Krivi unos ili ne postoji # # ")
            elif menu_choice == 2:          # main course
                while True:
                    self.restoran.print_food(1)
                    id_input = input(" -- Upisi id glavnog jela: ")
                    if id_input == "0":
                        break
                    else:
                        main = self.restoran.get_main_course(id_input)
                        if main:
                            order_list.append(main)
                        else:
                            print(" # # Krivi unos ili ne postoji # # ")
            elif menu_choice == 3:          # dessert
                while True:
                    self.restoran.print_food(2)
                    id_input = input(" -- Upisi id deserta: ")
                    if id_input == "0":
                        break
                    else:
                        main = self.restoran.get_dessert(id_input)
                        if main:
                            order_list.append(main)
                        else:
                            print(" # # Krivi unos ili ne postoji # # ")
            elif menu_choice == 0:
                if order_list:
                    return order_list
                else:
                    return None

    def add_drink(self, id_drinks):
        beverage: Beverages = Beverages(Utils.dodajZnamenke(id_drinks, 2),
                                        input(" -- Naziv pica: "),
                                        Utils.unesiCijeliBroj(" -- Cijena: "),
                                        Utils.unesiCijeliBroj(" -- Odaberi (bezalkoholno 0, alkoholno 1): "))
        self.restoran.add_drinks(beverage)
        return id_drinks + 1

    def print_drinks(self):
        print("------- Pica -------")
        self.restoran.print_drinks()

    def order_drink(self):
        order_list = []
        while True:
            menu_choice = Utils.unesiCijeliBroj(" -- 1 bezalkoholno, 2 alkoholno, 0 povratak: ")
            if menu_choice == 1:            # non alcohol drinks
                while True:
                    self.restoran.print_drinks()
                    id_input = input(" -- Upisi id pica: ")
                    if id_input == "0":
                        break
                    else:
                        drink = self.restoran.get_drink(id_input)
                        if drink:
                            order_list.append(drink)
                        else:
                            print(" # # Krivi unos ili ne postoji # # ")
            elif menu_choice == 2:          # alcohol drinks
                while True:
                    self.restoran.print_drinks()
                    id_input = input(" -- Upisi id pica: ")
                    if id_input == "0":
                        break
                    else:
                        drink = self.restoran.get_drink(id_input)
                        if drink:
                            order_list.append(drink)
                        else:
                            print(" # # Krivi unos ili ne postoji # # ")
            elif menu_choice == 0:          # return
                if order_list:
                    return order_list
                else:
                    return None

    def add_table(self, id_table):
        table: Table = Table(Utils.dodajZnamenke(id_table, 2))
        self.restoran.add_table(table)
        print(f" -- Stol broj {id_table} je dodan -- ")
        return id_table + 1

    def print_tables(self):
        self.restoran.print_tables()

    def make_table_reservation(self):
        self.restoran.print_tables()
        self.restoran.get_table_reserved(input(" -- Upisi id stola za rezervaciju: "))

    def cancel_table_reservation(self):
        self.restoran.print_tables()
        self.restoran.get_table_canceled(input(" -- Upisi id stola za otkazati: "))

    def make_order(self, receipt_id):
        table = self.restoran.get_table(input(" -- Upisi broj stola: "))
        order = []
        drinks_price = 0
        food_price = 0
        total = 0
        drinks_order = self.order_drink()
        if drinks_order:
            order.append(drinks_order)
            for drinks in drinks_order:
                drinks_price += drinks.price
            print(order)
            print(drinks_price)
        else:
            print(" - Narudzba bez pica - ")

        food_order = self.order_food()
        if food_order:
            order.append(food_order)
            for food in food_order:
                food_price += food.price
            print(order)
            print(food_price)
        else:
            print(" - Narudzba bez jela -")

        total = drinks_price + food_price

        payment_method = input(" -- Odaberi plaćanje; 0 - gotovina, 1 - kartica: ")
        if payment_method == "0":
            payment = "Placanje novcanice"
        else:
            payment = "Placanje kartica"

        receipt: Receipt = Receipt(Utils.dodajZnamenke(receipt_id),
                                   table, order, total, payment,
                                   jir=Receipt.jir(self))
        #print(receipt)
        self.restoran.add_receipt(receipt)
        print("racun dodan")
        return receipt_id + 1

    def print_receipts(self):
        self.restoran.print_receipts()

    def save_files(self):
        self.restoran.save_data()

    def load_files(self):
        self.restoran.load_data()
