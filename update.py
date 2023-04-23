import inventory
import add_item
import inventory
import remove_item

def update_inventory():
    print("Would you like to:\n1) Add items\n2) Remove items\n3) Show items ")
    option = int(input("Enter here: "))

    if option == 1:
        add_item.add_item()
        
    elif option == 2:           
        remove_item.remove_item()
        
    elif option == 3:
        inventory.show_inventory_readable()


