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
        if search_item in self.stock:
            print(self.stock)


class Item:
    def __init__(self, state: str, category: str, warehouse: int, date_of_stock: datetime):
        self.state = state
        self.category = category
        self.warehouse = warehouse
        self.date_of_stock = date_of_stock

    def __str__(self):
        item = self.state + " " + self.category
        print(f'Item: {item}')




# ''' Personnel Classes'''

class User:
    def __init__(self, user_name: str):

        self._name = user_name
        self.is_authenticated = False
        if user_name == "":
            self._name = "Anonymous"





    def authenticate(self, password):
        return False


    def is_named(self, name: str):
        if name == self._name:
            return True
        return False




    def greet(self):
        return f"Hello, {self._name}\nWelcome to our Warehouse Database.\nIf you don't find what you are looking for, please ask one of our staff members to assist you."

    def bye(self, actions: list):
        return f"Goodbye {self._name}"

class Employee(User):


    def __init__(self, password: str, head_of):
        employee_list = []
        self.__password = password
        self.head_of = head_of
        if self.head_of in employee_list:
            print(self.head_of)

        super().__init__(self._name)

    def authenticate(self, password: str):
        if password == self.__password:
            return True
        return False

    def order(self, item, amount: int):
        print(f"You have ordered {item}, and {amount} number of items")

    def greet(self):
        print(f"Hello, {self._name}!\nIf you experience a problem with the system, please contact technical support.")

    def bye(self, actions: list):
        print(f"Thank you {self._name}")
        return actions
    





