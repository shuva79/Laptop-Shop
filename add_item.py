import inventory

def add_item():
    whole_inventory = inventory.show_inventory()    # a 2d list that stores inventory's value 
    
    # entering values for laptop
    laptop_model = input("Enter laptop model: ")    

    # checks if the model already exists or not
    if check_item_repeated(laptop_model) == "Repeated":
        print("Laptop model already exists. ")
        return 

    brand_name = input("Enter brand name: ")
    
    # exception handling for integer type values
    try:
        price = int(input("Enter price: "))
        qty = int(input("Enter quantity: "))
    
    except ValueError:
        print("Incorrect value entered. Returning to menu. ")
        return 

    cpu = input("Enter CPU: ")
    gpu = input("Enter GPU: ")

    list = [laptop_model, brand_name, price, qty, cpu, gpu]     # Creating a list to check an element is empty

    for item_value in list:             # This validates user input by iterating through each element of the list
        if validate_input(item_value) == False:         # Calls function validate_input() for input validation
            print(f"Empty value detected at {item_value}\nReturning to menu...")
            return 

    # the new list is then appended to the inventory 2d list
    whole_inventory.append(list)

        # the value of entire updated 2d list is overwritten to the file
    with open("inventory.txt", "w") as file:         # Write because we want to update the value by overwriting the file but appending the 2d list
        for record in whole_inventory:
                record[5] = record[5].replace('\n', '')     # removing the newline escape because one will be assigned when written to the file
                print(f"{record[0]}, {record[1]}, ${record[2]}, {record[3]}, {record[4]}, {record[5]}", file=file)

    print("Record has been successfully updated.")
    print(f"{laptop_model}, {brand_name}, ${price}, {qty}, {cpu}, {gpu}")
        

def check_item_repeated(item_name):                     # Checks if the input model is repeated with the one in the inventory
    items = inventory.show_inventory()

    for individual_item in items:           
        if individual_item[0] == item_name:
            return "Repeated"

def validate_input(value):          # Checks if the input value is empty or not
    if value != '':
        return True

    return False
