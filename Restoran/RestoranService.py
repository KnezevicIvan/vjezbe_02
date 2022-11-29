from Restoran import Restoran
from Utils import Utils
from Food import Food
from Beverages import Beverages
from Table import Table


class RestoranService:

    def __init__(self):
        self.restoran = Restoran()

    def add_appetizer(self, id_appetizer):
        appetizer: Food = Food(Utils.dodajZnamenke(id_appetizer, 2), input("Naziv predjela:"), Utils.unesiCijeliBroj("Cijena: "))
        self.restoran.add_appetizer(appetizer)
        return id_appetizer + 1

    def add_main_course(self, id_main_course):
        main_course: Food = Food(Utils.dodajZnamenke(id_main_course, 2), input("Naziv jela:"), Utils.unesiCijeliBroj("Cijena: "))
        self.restoran.add_main_course(main_course)
        return id_main_course + 1

    def add_dessert(self, id_dessert):
        dessert: Food = Food(Utils.dodajZnamenke(id_dessert, 2), input("Naziv deserta:"), Utils.unesiCijeliBroj("Cijena: "))
        self.restoran.add_dessert(dessert)
        return id_dessert + 1

    def print_food(self):
        print("-------Predjelo-------")
        self.restoran.print_food(0)
        print("-------Glavno jelo-------")
        self.restoran.print_food(1)
        print("-------Desert-------")
        self.restoran.print_food(2)

    def add_non_alcohol_drink(self, id_non_alcohol_drinks):
        beverage: Beverages = Beverages(Utils.dodajZnamenke(id_non_alcohol_drinks, 2), input("Naziv pica:"), Utils.unesiCijeliBroj("Cijena: "))
        self.restoran.add_non_alcohol_drink(beverage)
        return id_non_alcohol_drinks + 1

    def add_alcohol_drink(self, id_alcohol_drinks):
        beverage: Beverages = Beverages(Utils.dodajZnamenke(id_alcohol_drinks, 2), input("Naziv pica:"), Utils.unesiCijeliBroj("Cijena: "))
        self.restoran.add_alcohol_drink(beverage)
        return id_alcohol_drinks + 1

    def print_drinks(self):
        print("-------Bezalkoholna pica-------")
        self.restoran.print_drinks(0)
        print("-------Glavno jelo-------")
        self.restoran.print_drinks(1)

    def add_table(self, id_table):
        table: Table = Table(Utils.dodajZnamenke(id_table, 2))
        self.restoran.add_table(table)
        return id_table + 1

    def print_tables(self):
        self.restoran.print_tables()

    def order_food(self):
