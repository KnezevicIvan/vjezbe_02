from Food import Food
from Beverages import Beverages
from Table import Table

class Restoran:

    def __init__(self):
        self.food_list = [[], [], []]
        self.drinks_list = [[], []]
        self.table_list = []
        self.receipt_list = []

    def add_appetizer(self, appetizer: Food):
        self.food_list[0].append(appetizer)

    def add_main_course(self, main_course: Food):
        self.food_list[1].append(main_course)

    def add_dessert(self, dessert: Food):
        self.food_list[2].append(dessert)

    def print_food(self, n):            # 0 predjelo, 1 glavno jelo, 2 desert
        for h in self.food_list[n]:
            print(h)

    def add_non_alcohol_drink(self, beverage: Beverages):
        self.drinks_list[0].append(beverage)

    def add_alcohol_drink(self, beverage: Beverages):
        self.drinks_list[1].append(beverage)

    def print_drinks(self, n):             # 0 bezalkoholno, 1 alkoholno
        for p in self.drinks_list[n]:
            print(p)

    def add_table(self, stol: Table):
        self.table_list.append(stol)

    def print_tables(self):
        for s in self.table_list:
            print(s)