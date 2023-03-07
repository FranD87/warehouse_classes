"""Command line interface to query the stock.
To iterate the source data you can use the following structure:
for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""
from data import stock
import datetime as dt
# YOUR CODE STARTS HERE

warehouse1 = []
warehouse2 = []

for i in stock:
    if i['warehouse'] == 1:
        item_name = i['state'] + ' ' + i['category']
        warehouse1.append(item_name)
    else:
        item_name = i['state'] + ' ' + i['category']
        warehouse2.append(item_name)




name = input('Enter your name: ')
print('Hello ' + name)
print('1. List items by warehouse')
print('2. Search an item and place an order')
print('3. Browse by category')
print('4. Quit')
p = int(input('Pick any statement by its number: '))


if p == 1:
    print('Items from warehouse 1: ')
    for i in warehouse1:
        print(i)
    print('Items from warehouse 2: ')
    for j in warehouse2:
        print(j)

    print(f'Total items in warehouse 1: {len(warehouse1)}')
    print(f'Total items in warehouse 1: {len(warehouse1)}')

elif p == 2:
    item_name = input('Enter an item name: ').lower()
    w11 = []
    w22 = []
    for i in warehouse1:
        l1 = i.lower()
        w11.append(l1)

    for i in warehouse2:
        l2 = i.lower()
        w22.append(l2)

    w1 = w11.count(item_name)
    w2 = warehouse2.count(item_name)
    w3 = w1 + w2
    print(f'Total amount of items available: {w3}')
    print('Location:')

    for i in stock:
        s = (i['state'] + ' ' + i['category']).lower()
        if s == item_name:
            j = i['warehouse']
            d = i['date_of_stock']
            days = (dt.datetime.now() - dt.datetime.strptime(d, '%Y-%m-%d %H:%M:%S')).days

            print(f'Warehouse {j} (in stock for {days} days)')

    if w1 > 0 and w2 > 0:
        print('Location: Both warehouses')
        if w1 > w2:
            print(f'warehouse 1 has the highest number of items: {w1}')
        else:
            print(f'warehouse 2 has the highest number items: {w2}')
    elif w1 > 0 and w2 == 0:
        print('Location: warehouse 1')
    elif w1 == 0 and w2 > 0:
        print('Location: warehouse 2')
    else:
        print('Not in stock')
    ans = input('Do you want to place an order for this item?: ')
    if ans == 'yes':
        num = int(input('How many do you want?: '))
        if num <= w3:
            print(f'The order has been placed. Item name {item_name} and amount ordered {num}')
        elif num > w3:
            ans_max = input('Out of stock. Do you want to order the maximum available?: ')
            if ans_max == 'yes':
                print(f'The order has been placed. Item name {item_name} and amount ordered {w3}')
elif p == 3:
    c = []

    for i in stock:
        cat = i['category']
        c.append(cat)
    c1 = []
    for i in c:
        if i not in c1:
            c1.append(i)

    print(c1)


elif p == 4:

    pass
else:
    print('The operation entered is not valid')
print(f'{name}, thank you for the visit')


