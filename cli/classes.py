from datetime import datetime
from data import personnel
from data import stock


# ''' Stock classes'''

class Warehouse:

    stock = []
    def __init__(self, warehouse_id: int):
        self.warehouse_id = warehouse_id




    def occupancy(self):

        return len(self.stock)

    def add_item(self, item):

        self.stock.append(item)


    def search(self, search_item: str):
        pass


class Item:
    def __init__(self, state: str, category: str, warehouse: int, date_of_stock: datetime):
        self.state = state
        self.category = category
        self.warehouse = warehouse
        self.date_of_stock = date_of_stock

    def __str__(self):
        pass

# ''' Personnel Classes'''

class User:
    def __init__(self, user_name: str):
        self._user_name = user_name

    def authenticate(self, password: str):
        pass

    def  is_named(self, name: str):
        pass

    def greet(self):
        pass

    def bye(self, actions: list):
        pass

class Employee:
    def __init__(self, user_name: str, password: str, head_of: list):
        self.user_name = user_name
        self.__password = password
        self.head_of = head_of

    def authenticate(self, password: str):
        pass

    def order(self, item, amount: int):
        pass

    def greet(self):
        pass

    def bye(self, actions: list):
        pass
    





