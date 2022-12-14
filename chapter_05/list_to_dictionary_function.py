def display_inventory(inventory):
    total_items = 0
    print('Inventory:')

    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        total_items += v

    print('Total number of items: ' + str(total_items))


def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] = inventory[item] + 1


inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
add_to_inventory(inv, dragon_loot)
display_inventory(inv)
