events = input().split('|')
energy = 100
coins = 100
factory_is_closed = False

for current_event in events:
    event, value = current_event.split('-')
    value = int(value)

    if event == 'rest':
        initial_energy = energy
        energy += value
        if energy > 100:
            energy = 100
        gained_energy = energy - initial_energy
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {energy}.')

    elif event == 'order':
        if energy >= 30:
            energy -= 30
            coins += value
            print(f'You earned {value} coins.')
        else:
            energy += 50
            print('You had to rest!')
            continue

    else:
        if coins >= value:
            coins -= value
            print(f'You bought {event}.')
        else:
            factory_is_closed = True
            print(f'Closed! Cannot afford {event}.')
            break

if not factory_is_closed:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
