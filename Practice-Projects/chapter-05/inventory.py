stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):
    print("Inventory:")
    
    item_total = 0  # set total number of items to 0
    
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
        
    print("Total number of items: " + str(item_total))


# Call the function with `stuff` as argument
display_inventory(stuff)
