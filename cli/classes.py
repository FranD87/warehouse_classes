from datetime import datetime
from abc import ABC, abstractmethod
from data import personnel
from data import stock
from collections import Counter


# ''' Stock classes''
class Item(ABC):
    def __init__(self, state: str, category: str, date_of_stock: str, warehouse = None):
        self.state = state
        self.category = category
        self.date_of_stock = date_of_stock
        # now = datetime.now()
        # self.date_of_stock = datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
        # self.date_of_stock = datetime.strptime('2023-02-15 21:49:20','%Y-%m-%d %H:%M:%S')

    def last_stocked(self):
        if type(self.date_of_stock) == str:
            return f'Last stocked: {(datetime.now() - datetime.strptime(self.date_of_stock, "%Y-%m-%d %H:%M:%S")).days} days ago'
        else:
            raise TypeError()

    def get_product_name(self):
        return f'{self.state} {self.category}'

    def __str__(self):
        return f'{self.state} {self.category}'

class Warehouse(Item):

    warehouses_total_stock = []
    warehouses_list = []
    history = []

    def __init__(self, warehouse_id: int = None):
        self.warehouse_id = warehouse_id
        self.stock = []

    def occupancy(self):
        return len(self.stock)

    def add_item(self, obj: Item):
        self.stock.append(obj)

    def search(self, search_term, user):
        matches = []
        for item in self.stock:
            if item.get_product_name().lower() == search_term.lower():
                matches.append(item)
        if matches:
            user.add_to_history(f'Searched for {search_term} in {matches[0]}')
            print(user.history)
        return matches

    @staticmethod
    def order(warehouse, matches, user):
        print(f'\n{warehouse}: ({len(matches)}) {matches[0]} available')
        while True:
            order_amount = int(input(' How many would you like to order? :'))
            if order_amount <= len(matches):
                print(f'* {order_amount} {matches[0].get_product_name()}(s) ordered! *')
                user.add_to_history(f'Ordered "{order_amount}" - "{matches[0].get_product_name()}(s)" from "{warehouse}"')
                return order_amount
            elif order_amount > len(matches):
                print(f"\n*** There aren't this many products in this warehouse! "
                      f"Maximum possible is {len(matches)} ***\n")

    def get_warehouse_stock(self, inventory):
        for item in inventory:
            if self.warehouse_id == item['warehouse']:
                self.stock.append(Item(item['state'], item['category'], item['date_of_stock']))

    def display_warehouse(self, user):
        print(f'\nProducts in warehouse {self.warehouse_id}:')
        counter = 0
        for item in self.stock:
            counter += 1
            print(f'{item} - {item.last_stocked()}')
        user.add_to_history(f'Browsed "{counter}" product(s) in "Warehouse {self.warehouse_id}"')
        print(user.history)

    @classmethod
    def total_stock(cls, inventory):
        warehouses = set()
        for product in inventory:
            cls.warehouses_total_stock.append(Item(**product))
            if product['warehouse'] not in warehouses:
                warehouses.add(product['warehouse'])
        cls.warehouses_list = list(warehouses)
        return warehouses

    @staticmethod
    def display_matches(warehouse, matches):
        if matches:
            print(f'\n{warehouse}\n'
                  f' Amount available: {len(matches)}')
            for i in matches:
                print(f'{i} - {i.last_stocked()}')

    def delete_item(self, name):
        index = 0
        for i in self.stock:
            if i.get_product_name().lower() == name.lower():
                del self.stock[index]
                break
            index += 1

    def display_categories(self):
        categories = []
        for item in self.stock:
            categories.append(item.category)
        cat_counter = Counter(categories)
        category_dict = {}
        for index, (key, value) in enumerate(cat_counter.items(), 1):
            print(f'{index}. {key} ({value})')
            category_dict[index] = key
        return category_dict

    @staticmethod
    def browse_category(categories, warehouse, user):
        while True:
            choice = input('Insert category index to browse or "b" to go back: ')
            if choice.isnumeric():
                if type(int(choice)) is int and int(choice) in categories:
                    search = categories[int(choice)]
                    print(f'{warehouse} has in category "{search}":')
                    for item in warehouse.stock:
                        if item.category == search:
                            print(f' - {item.state} {item.category}')
                    user.add_to_history(f'Browsed category "{search}" in "{warehouse}"')
                    return search
                else:
                    print("*" * 10, "Error 404! Category not found!", "*" * 10)
                    continue
            elif choice == 'b':
                return False
            else:
                print("*" * 10, "Only indexes are accepted as input!", "*" * 10)
                continue

    def __str__(self):
        return f'Warehouse {self.warehouse_id}'


class User(ABC):
    history = []
    def __init__(self, user_name: str = 'Anonymous', ):
        self._name = user_name

    def is_authenticated(self):
        return False

    def authenticate(self, password: str):
        return False

    def is_named(self, name: str):
        pass

    def get_user_name(self):
        return self._name

    def greet(self):
        return f'Hello, {self.get_user_name()}!\nWelcome to our Warehouse Database.\n' \
               f"If you don't find what you are looking for,please ask one of " \
               "our staff members to assist you."

    def bye(self):
        return f'Thank you for your visit, {self.get_user_name()}'

    @staticmethod
    def check_user(staff_db, username):
        for item in staff_db:
            if item["user_name"] == username:
                return item
            elif "head_of" in item:
                user_ho = User.check_user(item["head_of"], username)
                if user_ho:
                    return user_ho
        return False

    @classmethod
    def add_to_history(cls, string):
        print(string)
        cls.history.append(string)


# ''' Personnel Classes'''

class Employee(User):
    history = []

    def __init__(self, user_name: str, __password: str, head_of: list = None):
        User.__init__(self, user_name)
        self.__password = __password

    def authenticate(self, password: str):
        if password == self.__password:
            return True
        return False

    def greet(self):
        return f'Hello, {self.get_user_name()}!\n If you experience a problem ' \
               f'with the system, please contact technical support.'

    @classmethod
    def add_to_history(cls, string):
        print(string)
        cls.history.append(string)

    def bye(self):
        print(f'Thank you for your visit, {self.get_user_name()}!')
        print(' Actions taken:')
        self.history = list(set(self.history))
        for i in range(len(self.history)):
            print(f"{i + 1}. {self.history[i]}")





