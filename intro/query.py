"""Command line interface to query the stock.
To iterate the source data you can use the following structure:
for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

# from data import warehouse1, warehouse2
#
# # YOUR CODE STARTS HERE
# def remove_ordered(quantity:int,product,product_list):
#     for item in product_list:
#         if product.capitalize() == item and quantity:
#             product_list.remove(item)
#             quantity -= 1
#     remaining = quantity
#     return remaining
#
# # Get the user name
# name = input('Insert your user name:').capitalize()
# # Greet the user
# print(f'\nHello, {name}!')
#
# # Show the menu and ask to pick a choice
# run_menu = True
# while run_menu:
#     print('\nWhat would you like to do?\n1. List the items by warehouse\n2. Search an item and place an order\n3. Quit')
#     option = input('Type the number of the operation: ')
#
# # If they pick 1
# if option.isdigit():
#     if int(option) == 1:
#         print('\nItems in warehouse 1:')
#         for item in warehouse1:
#             print(item)
#         print('\nItems in warehouse 2:')
#         for item in warehouse2:
#             print(item)
#
# # Else, if they pick 2
#     elif int(option) == 2:
#             run_op2 = True
# while run_op2:
#     search = input('\nInsert item name to search in warehouses:')
#     match_w1 = 0
#     for item in warehouse1:
#         if search.lower() == item.lower():
#             match_w1 += 1
#     match_w2 = 0
#     for item in warehouse2:
#         if search.lower() == item.lower():
#             match_w2 +=1
#     total_matches = match_w1 + match_w2
#     if total_matches:
#         print(f'Amount available: {total_matches}')
#     else:
#         print(f'No matches found for {search}')
#         break
#
# if match_w1 and match_w2:
#     location = 'Both warehouses'
# elif match_w1 and match_w2 == False:
#     location = 'Warehouse 1'
# elif match_w1 == False and match_w2:
#     location = 'Warehouse 2'
# else:
#     location = 'Not in stock'
# print(f'Location: {location}')
#
# if match_w1 > match_w2:
#     max_stock = f'{match_w1} in Warehouse 1'
# elif match_w1 < match_w2:
#     max_stock = f'{match_w2} in Warehouse 2'
# elif match_w1 == 0 and match_w2 ==0:
#     max_stock = 'not available'
# else:
#     max_stock = f'{match_w1} in each warehouse'
# print(f'Maximum availability: {max_stock}')
#
# confirmation = input('\nWould you like to order this item?(y/n): ')
# if confirmation.lower() == 'n':
#         break
#
# elif confirmation.lower() != 'y':
# print(f'Option "{confirmation}" not recognized! Try again?')
# break
# order = input('How many would you like?: ')
# if order.isdigit():
#     if int(order) <= total_matches:
#         print(f'\n*{order} {search} have been ordered')
#         remaining = remove_ordered(int(order),search,warehouse1)
#         if remaining:
#             remove_ordered(remaining, search, warehouse2)
#             print(warehouse1)
#             print(warehouse2)
#             # order completed , items removed from inventory
#
# elif int(order) > total_matches:
# print('*' * 100)
# print(f'There are not this many available. The maximum amount that can be ordered is {total_matches}')
# print('*' * 100)
# confirmation = input(f'Would you like to order {total_matches},which is the maximum available?(y/n):')
# if confirmation == 'y':
#     print(f'\n*Order has been placed! {total_matches} {search.capitalize()} have been ordered')
#     remaining = remove_ordered(int(order), search, warehouse1)
#     if remaining:
#         remove_ordered(remaining, search, warehouse2)
#         print(warehouse1)
#         print(warehouse2)
#         # order complete item removed from inventory
#
# else:
# pass
# else:
# print(f'Quantity "{order}" not recognized')
# # Else, if they pick 3
# elif int(option) == 3:
# print(f'Goodbye, {name}! Thanks for passing by!')
# run_menu = False
# # Else
# else:
# print(f'\n"{option}" option not recognized(hint:try options 1,2 or 3 to quit)\n')
# else:
# print(f'\n"{option}" option not recognized\n')
# Thank the user for the visit