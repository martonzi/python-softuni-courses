items_collection = input().split('|')
budget = float(input())

current_budget = budget
ticket = 150

sold_items = []

for current_item in items_collection:
    item, price = current_item.split('->')
    price = float(price)

    if price > current_budget:
        continue

    if item == 'Accessories':
        if price <= 20.50:
            current_budget -= price
            sold_price = price * 1.40
            sold_items.append(sold_price)

    elif item == 'Shoes':
        if price <= 35:
            current_budget -= price
            sold_price = price * 1.40
            sold_items.append(sold_price)

    elif item == 'Clothes':
        if price <= 50:
            current_budget -= price
            sold_price = price * 1.40
            sold_items.append(sold_price)

profit = sum(sold_items) + current_budget - budget
list_of_sold_items_as_string = [str(num) for num in sold_items]

for item in list_of_sold_items_as_string:
    print(f'{float(item):.2f}', end=' ')

print(f'\nProfit: {profit:.2f}')

if sum(sold_items) + current_budget > ticket:
    print('Hello, France!')
else:
    print('Not enough money.')
