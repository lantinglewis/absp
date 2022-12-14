stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):
    total_items = 0
    print('Inventory:')

    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        total_items += v

    print('Total number of items: ' + str(total_items))


display_inventory(stuff)
