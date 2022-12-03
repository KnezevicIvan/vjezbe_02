from Food import Food
from Beverages import Beverages
from Table import Table


class Restoran:

    def __init__(self):
        self.food_list = [[], [], []]
        self.drinks_list = []
        self.table_list = []
        self.receipt_list = []

    def add_appetizer(self, appetizer: Food):
        self.food_list[0].append(appetizer)

    def add_main_course(self, main_course: Food):
        self.food_list[1].append(main_course)

    def add_dessert(self, dessert: Food):
        self.food_list[2].append(dessert)

    def print_food(self, n):  # 0 predjelo, 1 glavno jelo, 2 desert
        for h in self.food_list[n]:
            print(h)

    def get_appetizer(self, input_id):
        for f in self.food_list[0]:
            print(self.food_list[0])
            if f.id == input_id:
                return f
            else:
                return None

    def get_main_course(self, input_id):
        for f in self.food_list[1]:
            if f.id == input_id:
                return f
            else:
                return None

    def get_dessert(self, input_id):
        for f in self.food_list[2]:
            if f.id == input_id:
                return f
            else:
                return None

    def add_drinks(self, beverage: Beverages):
        self.drinks_list.append(beverage)

    def print_drinks(self):  # 0 bezalkoholno, 1 alkoholno
        for p in self.drinks_list:
            print(p)

    def print_drinks_category(self, n):
        """parameter: 0 non alcohol, 1 alcohol"""
        for d in self.drinks_list:
            if d.alsohol == n:
                print(d)

    def get_drink(self, input_id):
        for d in self.drinks_list:
            if d.id == input_id:
                return d
            else:
                return None

    def add_table(self, stol: Table):
        self.table_list.append(stol)

    def print_tables(self):
        for s in self.table_list:
            print(s)

    def get_table_reserved(self, input_id):
        for t in self.table_list:
            if t.reservation == None and t.id == input_id:
                t.reservation = input(" Upisi ime rezervacije: ")


    def get_table(self, input_id):
        for t in self.table_list:
            if t.id == input_id:
                return t
            else:
                return None