import inventory
import manufacturer
import time
import customer
import update

# triple quotation mark helps to print multiline string
def select_option():
    print('''
        
    __  __                                        _______        _     
    |  \/  |                                      |__   __|      | |    
    | \  / | __ _  ___ __ _ _ __ ___ _ __   __ _     | | ___  ___| |__  
    | |\/| |/ _` |/ __/ _` | '__/ _ \ '_ \ / _` |    | |/ _ \/ __| '_ \ 
    | |  | | (_| | (_| (_| | | |  __/ | | | (_| |    | |  __/ (__| | | |
    |_|  |_|\__,_|\___\__,_|_|  \___|_| |_|\__,_|    |_|\___|\___|_| |_|
                                                                                                                                            
    ''')


    print(f"Choose your desired option:\n1) Place order (Manufacturer)\n2) Place order (Customer)\n3) Show inventory\n4) Edit inventory\n5) Exit")
    return int(input("Option: "))


while (True):
    try:            # In case an error is raised
        option = select_option()

        if option == 1:             # opens file which handles orders to manufacturers
            manufacturer.manufacturer_orders()
            

        elif option == 2:           # opens file which handles customer orders
            customer.customer_orders()
            
        elif option == 3:           # opens file which shows inventory text file
            choice = int(input("Do you want to search for:\n1) Specific item\n2) Inventory:\n "))
            
            if choice == 1:
                inventory.specific_search_items()
            
            elif choice == 2:
                inventory.show_inventory_readable()

        elif option == 4:           # updates inventory 
            update.update_inventory()

        elif option == 5:
            break
        
        else:
            print("Please enter a number between the range of 1 to 4")
        #time.sleep(2)               # The output comes out in a more human readable timing I guess

    except ValueError:             # In case the user inputs a different data type value
        print("Please enter a valid input number.")
        continue