from classes import Warehouse
from classes import User
from classes import Employee
from data import stock, personnel
# from loader import *


# Get the username
user_name = input("Insert your user name: ")
verification = User.check_user(personnel, user_name)

if verification:
    user = Employee(verification['user_name'], verification['password'])
else:
    user = User(user_name.capitalize())
# Greet the user
print(user.greet())

# Create warehouses and add stock
Warehouse.total_stock(stock)

warehouse1 = Warehouse(1)
warehouse1.get_warehouse_stock(stock)

warehouse2 = Warehouse(2)
warehouse2.get_warehouse_stock(stock)

warehouse3 = Warehouse(3)
warehouse3.get_warehouse_stock(stock)

warehouse4 = Warehouse(4)
warehouse4.get_warehouse_stock(stock)

warehouse5 = Warehouse(5)
warehouse5.get_warehouse_stock(stock)

# Show the menu and ask to pick a choice
run_menu = True
log_in = True
logged_in = False
while run_menu:
    print('What would you like to do?')
    print('1. List the items by warehouse')
    print('2. Search an item and place an order')
    print('3. Browse by category')
    print('4. Quit')
    option = input('Type the number of the operation: ')
    # If they pick 1
    if option.isdigit():
        if int(option) == 1:
            while True:
                print(f"We have {len(Warehouse.warehouses_total_stock)} products in "
                      f"{len(Warehouse.warehouses_list)} warehouses")
                print('\n')
                print(f'{warehouse1} has {warehouse1.occupancy()} products')
                print(f'{warehouse2} has {warehouse2.occupancy()} products')
                print(f'{warehouse3} has {warehouse3.occupancy()} products')
                print(f'{warehouse4} has {warehouse4.occupancy()} products')
                print(f'{warehouse5} has {warehouse5.occupancy()} products')
                choice = input('\n Insert warehouse number to browse warehouse or type "e" to quit : ')
                if choice.isdigit() and 0 < int(choice) <= 5:
                    if int(choice) == 1:
                        warehouse1.display_warehouse(user)
                    elif int(choice) == 2:
                        warehouse2.display_warehouse(user)
                    elif int(choice) == 3:
                        warehouse3.display_warehouse(user)
                    elif int(choice) == 4:
                        warehouse4.display_warehouse(user)
                    elif int(choice) == 5:
                        warehouse5.display_warehouse(user)
                elif choice == 'e':
                    print('\n')
                    break
                else:
                    print('\n***Invalid warehouse number!***\n')

        # Else, if they pick 2
        elif int(option) == 2:
            run_search = True
            while run_search:
                search_for = input(' Insert product name to search for or "b" to go back: ')
                if search_for == 'b':
                    break
                matches1 = warehouse1.search(search_for, user)
                Warehouse.display_matches(warehouse1, matches1)

                matches2 = warehouse2.search(search_for, user)
                Warehouse.display_matches(warehouse2, matches2)

                matches3 = warehouse3.search(search_for, user)
                Warehouse.display_matches(warehouse3, matches3)

                matches4 = warehouse4.search(search_for, user)
                Warehouse.display_matches(warehouse4, matches4)

                matches5 = warehouse5.search(search_for, user)
                Warehouse.display_matches(warehouse5, matches5)

                if not matches1 and not matches2 and not matches3 and not matches4 and not matches5:
                    print('\n*** NO MATCHES FOUND! ***')
                    continue

                choice = input(' Would you like to order this product? (y/n) or e to quit: ').lower()
                if choice == 'n':
                    print('\n')
                    continue
                elif choice == 'e':
                    print('\n')
                    break
                elif choice != 'y':
                    print('\n*** Command not recognized! ***\n')
                    continue
                if not logged_in:
                    print('To continue you must log in!')
                    go_back = None
                    while log_in:
                        choice = input('Insert password or just press enter to go back:')
                        if choice == '':
                            go_back = True
                            break
                        elif "Employee" in str(type(user)):
                            ver = user.authenticate(choice)
                            if ver:
                                log_in = False
                                logged_in = True
                        else:
                            print('\n*** You are not allowed to take this action!***\n')
                            break
                    if go_back:
                        continue
                while True:
                    choice = input(' Insert number of warehouse from which you would like to order: ')
                    if choice.isdigit() and 0 < int(choice) <= len(Warehouse.warehouses_list):
                        if int(choice) == 1 and matches1:
                            ord_num = Warehouse.order(warehouse1, matches1, user)
                            for i in range(ord_num):
                                warehouse1.delete_item(matches1[0].get_product_name())
                            break
                        elif int(choice) == 2 and matches2:
                            ord_num = Warehouse.order(warehouse2, matches2, user)
                            for i in range(ord_num):
                                warehouse2.delete_item(matches2[0].get_product_name())
                            break
                        elif int(choice) == 3 and matches3:
                            ord_num = Warehouse.order(warehouse3, matches3, user)
                            for i in range(ord_num):
                                warehouse3.delete_item(matches3[0].get_product_name())
                            break

                        elif int(choice) == 4 and matches4:
                            ord_num = Warehouse.order(warehouse4, matches4, user)
                            for i in range(ord_num):
                                warehouse4.delete_item(matches4[0].get_product_name())
                            break

                        elif int(choice) == 5 and matches5:
                            ord_num = Warehouse.order(warehouse5, matches5, user)
                            for i in range(ord_num):
                                warehouse5.delete_item(matches5[0].get_product_name())
                            break

                        else:
                            print('\n*** Warehouse has no stock! ***\n')
                    else:
                        print('\n*** Invalid warehouse number! ***\n')
                        continue

        # If they pick 3
        elif int(option) == 3:
            while True:
                print(f"\nWe have {len(Warehouse.warehouses_total_stock)} products in "
                      f"{len(Warehouse.warehouses_list)} warehouses")
                print('\n')
                print(f'{warehouse1} has {warehouse1.occupancy()} products')
                print(f'{warehouse2} has {warehouse2.occupancy()} products')
                print(f'{warehouse3} has {warehouse3.occupancy()} products')
                print(f'{warehouse4} has {warehouse4.occupancy()} products')
                print(f'{warehouse5} has {warehouse5.occupancy()} products')
                choice = input('\n Insert warehouse index to browse warehouse categories or type "e" to quit : ')
                if choice.isdigit() and 0 < int(choice) <= 5:
                    if int(choice) == 1:
                        browse = True
                        while browse:
                            print('\n')
                            cats = warehouse1.display_categories()
                            print('\n')
                            res = Warehouse.browse_category(cats, warehouse1, user)
                            if res is False:
                                break
                        selected_wh = 1
                    elif int(choice) == 2:
                        browse = True
                        while browse:
                            print('\n')
                            cats = warehouse2.display_categories()
                            print('\n')
                            res = Warehouse.browse_category(cats, warehouse2, user)
                            if res is False:
                                break
                        selected_wh = 2
                    elif int(choice) == 3:
                        browse = True
                        while browse:
                            print('\n')
                            cats = warehouse3.display_categories()
                            print('\n')
                            res = Warehouse.browse_category(cats, warehouse3, user)
                            if res is False:
                                break
                        selected_wh = 3
                    elif int(choice) == 4:
                        browse = True
                        while browse:
                            print('\n')
                            cats = warehouse4.display_categories()
                            print('\n')
                            res = Warehouse.browse_category(cats, warehouse4, user)
                            if res is False:
                                break
                        selected_wh = 4
                    elif int(choice) == 5:
                        browse = True
                        while browse:
                            print('\n')
                            cats = warehouse5.display_categories()
                            print('\n')
                            res = Warehouse.browse_category(cats, warehouse5, user)
                            if res is False:
                                break
                        selected_wh = 5
                elif choice == 'e':
                    print('\n')
                    break
                else:
                    print('\n***Invalid warehouse number!***\n')

        # If they pick 4
        elif int(option) == 4:
            user.bye()
            run_menu = False

        # Else
        else:
            print(f'\n"{option}" option not recognized(hint:try options 1,2,3 or 4 to quit)\n')
    else:
        print(f'\n"{option}" option not recognized\n')



