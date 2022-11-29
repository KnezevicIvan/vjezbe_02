from datetime import datetime

class Receipt():

    def __init__(self, id):
        self.id = id
        self.order_list = []
        self.jir = None



    # int(dt.now().timestamp())