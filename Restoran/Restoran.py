from Food import Food
from Beverages import Beverages
from Table import Table
from Receipt import Receipt
import pickle
from pathlib import Path


class Restoran:

    def __init__(self):
        self.food_list = [[], [], []]
        self.drinks_list = []
        self.table_list = []
        self.receipt_list = []
        self.food_file = None
        self.drinks_file = None
        self.tables_file = None
        self.receipt_file = None

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
            if d.alcohol == n:
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
            if not (t.reservation or not (t.id == input_id)):
                t.reservation = input(" Upisi ime rezervacije: ")
                print(f" -- Stol broj {t.id} je rezerviran. -- ")

    def get_table(self, input_id):
        for t in self.table_list:
            if t.id == input_id:
                return t.id
            else:
                return None

    def get_table_canceled(self, input_id):
        for t in self.table_list:
            if t.id == input_id:
                t.reservation = None
                print(f" -- Stol broj {t.id} je otkazan. -- ")

    def add_receipt(self, receipt: Receipt):
        self.receipt_list.append(receipt)

    def print_receipts(self):
        for r in self.receipt_list:
            print(r)

    def save_data(self):
        root = Path(".")
        my_path = root / "datasource"
        self.food_file = my_path / 'foodList.pkl'
        self.drinks_file = my_path / 'drinksList.pkl'
        self.tables_file = my_path / 'tablesList.pkl'
        self.receipt_file = my_path / 'receiptList.pkl'
        with open(self.food_file, 'wb') as food:
            pickle.dump(self.food_list, food)
        with open(self.drinks_file, 'wb') as drinks:
            pickle.dump(self.drinks_list, drinks)
        with open(self.tables_file, 'wb') as tables:
            pickle.dump(self.table_list, tables)
        with open(self.receipt_file, 'wb') as receipts:
            pickle.dump(self.receipt_list, receipts)

    def load_data(self):
        root = Path(".")
        my_path = root / "datasource"
        food_file = my_path / 'foodList.pkl'
        drinks_file = my_path / 'drinksList.pkl'
        tables_file = my_path / 'tablesList.pkl'
        receipt_file = my_path / 'receiptList.pkl'
        with open(food_file, 'rb') as food:
            f = pickle.load(food)
            print(f)
            for i in f[0]:
                self.food_list[0].append(i)
            for j in f[1]:
                self.food_list[1].append(j)
            for k in f[2]:
                self.food_list[2].append(k)
        with open(drinks_file, 'rb') as drinks:
            d = pickle.load(drinks)
            print(d)
            for i in d:
                self.food_list.append(i)
        with open(tables_file, 'rb') as tables:
            t = pickle.load(tables)
            print(t)
            for i in t:
                self.food_list.append(i)
        with open(receipt_file, 'rb') as receipts:
            r = pickle.load(receipts)
            print(r)
            for i in r:
                self.food_list.append(i)
