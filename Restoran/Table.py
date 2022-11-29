from json import dumps

class Table:
    def __init__(self, id, reservation = False):
        self.id = id
        self.reservation = reservation

    def __repr__(self):
        return dumps(self.__dict__, indent=4)