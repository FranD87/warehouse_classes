from collections import Counter

def get_user_name():
    return input('Insert your user name:')

def greet_user(name:str):
    return f'\nWelcome, {name}!'

def get_operation():
    return input('Type the number of the operation: ')

def get_stock_list(stock,key1,key2):
    for item in stock:
        print(f'{item[key1]} {item[key2]}')
    return None

def get_warehouse_stock(stock, warehouse):
    warehouses = []
    for i in stock:
        warehouses.append(i[warehouse])
    warehouses = set(warehouses)
    for i in warehouses:
        warehouse_stock = []
        for item in stock:
            if i == item[warehouse]:
                warehouse_stock.append(item)
        counter = 0
        for product in warehouse_stock:
            counter += 1
        print(f'Warehouse {i}: {counter}')

def search_product():
    return input('\nInsert item name to search in warehouses:')

def get_search_product(search:str,key1 ,key2, stock:list) -> list:
    matches = []
    for item in stock:
        match = f'{item[key1]} {item[key2]}'
        if search.lower() == match.lower():
            matches.append(item)
    return matches

def get_product_warehouse(matches, warehouse):
    per_warehouse = []
    for i in matches:
        per_warehouse.append(i[warehouse])
    return per_warehouse

def get_matches(matches,search):
    if matches:
        return f'Amount available: {matches}'
    else:
        return f'No matches found for "{search}"'


def get_max_availability(warehouses):
    if warehouses:
        max_stock_dict = dict()
        for wh, value in warehouses.items():
            max_stock_dict[wh] = value
        max_value = max(max_stock_dict.values())
        for k,v in max_stock_dict.items():
            if v == max_value:
                return f'Maximum stock in Warehouse {k} with quantity {v}'

    else:
        return f'not available'

def check_user_exists(personnel, username):
    for item in personnel:
        if item["user_name"] == username:
            return item
        elif "head_of" in item:
            user = check_user_exists(item["head_of"], username)
            if user:
                return user
    return None

def check_password(personnel, username):
    user = check_user_exists(personnel, username)
    while not user:
        print(f"User {username} not found, please try again.")
        username = input("Enter user name: ")
        user = check_user_exists(personnel, username)

    password = input(f"Please type in your password': ")
    while password != user["password"]:
        print("Incorrect password, please try again.")
        password = input(f"Type password again: ")
    print(f"Log in successful.")

def place_order(search, total_matches):
    run_order = True
    while run_order:
        order = input('How many would you like?: ')
        if order.isdigit():
            if int(order) <= total_matches:
                if int(order) > 1:
                    print(f'\n*{order} {search.capitalize()}s have been ordered')
                else:
                    print(f'\n*{order} {search.capitalize()} has been ordered')
                run_order = False
            elif int(order) > total_matches:
                print('*' * 100)
                print(f'There are not this many available. The maximum amount that can be ordered is {total_matches}')
                print('*' * 100)
                confirmation = input(f'Would you like to order {total_matches},which is the maximum available?(y/n):')
                if confirmation == 'y':
                    order = total_matches
                    if order > 1:
                        print(f'\n*Your order has been placed! {total_matches} {search.capitalize()}s have been ordered')
                    else:
                        print(f'\n*Your order has been placed! {total_matches} {search.capitalize()} has been ordered')
                    run_order = False
                elif confirmation == 'n':
                    print("Try another quantity?")
                else:
                    print("What do you mean?")

        else:
            print(f'Quantity "{order}" not recognized')

def display_categories(stock, key2):
    categories = []
    for item in stock:
        categories.append(item[key2])
    cat_counter = Counter(categories)
    category_dict = {}
    for index, (key, value) in enumerate(cat_counter.items(), 1):
        print(f'{index}. {key} ({value})')
        category_dict[index] = key
    return category_dict

def browse_category(stock, category_dict, key1, key2, key3, choice):
    if choice in category_dict:
        search = category_dict[choice]
        for item in stock:
            if item[key2] == search:
                print(f'{item[key1]} {item[key2]}, Warehouse {item[key3]}')
    else:
        print("*"*10, "Error 404! Category not found", "*"*10)