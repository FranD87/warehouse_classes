
from data import stock, personnel
from collections import Counter
from datetime import datetime
from warehouse_classes.functions import functions

# YOUR CODE STARTS HERE


# Get the user name
user_name = functions.get_user_name().capitalize()
# Greet the user
print(functions.greet_user(user_name))

# Show the menu and ask to pick a choice
key1 = 'state'
key2 = 'category'
key3 = 'warehouse'
run_menu = True
log_in = True
while run_menu:
    print('\nWhat would you like to do?\n1. List the items by warehouse\n2. Search an item and place an order\n3. Browse by category\n4. Quit')
    option = functions.get_operation()

    # If they pick 1
    if option.isdigit():
        if int(option) == 1:
            functions.get_stock_list(stock, key1, key2)
            functions.get_warehouse_stock(stock, key3)

        # Else, if they pick 2
        elif int(option) == 2:
            run_search = True
            while run_search:
                search = functions.search_product()
                matches = functions.get_search_product(search, key1, key2, stock)
                per_warehouse = functions.get_product_warehouse(matches, key3)
                in_warehouse = Counter(per_warehouse)
                total_matches = in_warehouse.total()

                print(functions.get_matches(total_matches, search))

                if not matches:
                    print('Location: not in stock')
                else:
                    print('Location:')
                    by_warehouse = lambda stock: stock[key3]
                    sorted_matches = sorted(matches, key=by_warehouse)
                    for match in sorted_matches:
                        date_of_stock = datetime.strptime(match["date_of_stock"],"%Y-%m-%d %H:%M:%S")
                        last_stocked = datetime.today() - date_of_stock
                        print(f'-{match[key1]} {match[key2]} -> Warehouse: {match[key3]} (in stock for {last_stocked.days} days)')

                print(functions.get_max_availability(in_warehouse))

                if matches:
                    run_search = False
                    confirmation = input('\nWould you like to order this item?(y/n): ')
                    if confirmation.lower() == 'n':
                        print('Perhaps would you like to try something else!')
                        run_search = True
                    elif confirmation.lower() == 'exit':
                        print('Perhaps would you like to try something else!')
                        run_search = True
                    elif confirmation.lower() != 'y':
                        print(f'Option "{confirmation}" not recognized! Try again?')
                        run_search = True

            while log_in:

                if functions.check_user_exists(personnel, user_name):
                    print(f"Welcome, '{user_name}'!")
                    functions.check_password(personnel, user_name)
                    log_in = False
                else:
                    print(f"User '{user_name}' does not exist in the personnel list.")
                    user_name = input('Please log in with company username: ')
                    continue
            run_order = True
            functions.place_order(search, total_matches)

        # Else, if they pick 3
        elif int(option) == 3:
            run_op3 = True
            while run_op3:
                categories = functions.display_categories(stock, key2)
                cat_browse = True
                while cat_browse:
                    choice = input("Type the number of the category to browse or e to exit: ")
                    if choice.isnumeric():
                        functions.browse_category(stock, categories, key1, key2, key3, int(choice))
                    elif choice == 'e':
                        run_op3 = False
                        break
                    else:
                        print('Command not recognized')


        elif int(option) == 4:
            print(f'Thanks for passing by, {user_name}! Hope to see you soon!')
            run_menu = False

        else:
            print(f'\n"{option}" option not recognized(hint:try options 1,2,3 or 4 to quit)\n')
    else:
        print(f'\n"{option}" option not recognized\n')
    # Thank the user for the visit