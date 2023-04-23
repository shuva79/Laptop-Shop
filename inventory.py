import table

def show_inventory():
    '''Returns the entire inventory in a 2D array format'''
    file = open("inventory.txt", "r")                           # Opening inventory file in read mode
    list = []                                                   # Creating an empty list

    # The loop reads the file line by line and the value of each line is stored in 'line' variable
    for line in file:                                           # Reading through the file line by line
        trimmed_line = line.split(",")                          # This creates an array with a comma as the delimiter
        list.append(trimmed_line)                               # This adds the array to an empty array created above
    # NOTE: The trimmed_line creates a single dimensional array but when it is appended to list, 
    # it creates a 2D array which is eventually returned 

    file.close()

    return list

def show_inventory_readable():  # Prints info in a tabular format
    table_data = show_inventory()       # Pulls inventory data
    header = ["Laptop Model", "Brand Name", "Price", "Qty", "CPU", "GPU"]          # Header row for our table
    table.table(table_data, header, "")                        # Makes the actual table
    # the third parameter is empty because in case of a receipt it also writes into the file
    # table_data is the paramter for actual table data which is a 2D array
    # headers paramter takes parameter for the header row
    return 

def specific_search_items():
    item_list = show_inventory()
    item_set = []           # ik it is a list, I'll pass it through a set down

    print("\nChoose the column you want to view.\n1) Laptop Model\n2) Brand Name\n3) Price\n4) Quantity\n5) CPU\n6) GPU")
    try:
        choice = int(input("Enter here: "))
        
    except ValueError:
        print("Error, option doesn't exist. ")
    
    print("")
    
    if choice not in range(1,7):
        print("Error, please input a valid number")
        return 
    
    if choice == 2 or choice == 5 or choice == 6:
        for item in item_list:
            item_set.append(item[choice-1])

        for item in  list(set(item_set)):
            print(item)

        return 

    print("")

    for item in item_list:
        print(item[choice-1])
