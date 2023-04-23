import inventory


def selected_items_table(item_name, item_qty):         # This function helps us to create a table for receipt which takes a 1D array inventory_item as input along with item quantity    
        inventory_list = inventory.show_inventory()

        for inventory_item in inventory_list:
            if inventory_item[0] == item_name:          # Condition for checking item name
                stripped_price = inventory_item[2].strip(" $")          # Removes the $ sign from the variable for operation
                total_price = f" ${int(stripped_price) * item_qty}"     # Adds an additional $ sign to the variable
                receipt_list_1d = [inventory_item[0], inventory_item[1], inventory_item[2], item_qty, total_price]  # This array will be added to the 2D array above
                return receipt_list_1d


def order_items(item_name, item_qty):   # This function updates the value when we buy from the manufacturer into the file
    '''Checks if the item in question exists or not and updates inventory quantity'''

    
    flag = False                                    # In case of error             
    inventory_list = inventory.show_inventory()     # Pulls list of items from inventory.txt
    updated_value = open("inventory.txt", "w")      # Using write because overwriting the whole file will be easier than appending the value
    for inventory_item in inventory_list:           # Iterating over 2d list of tems
        updated_qty = int(inventory_item[3])        # Converting item quantity into int for operation and storing it in a variable

        if inventory_item[0] == item_name:          # Condition for checking item name
            updated_qty += int(item_qty)            
            inventory_item[3] = f" {str(updated_qty)}"      # Final quantity is stored updated in the array. 
                                                            # Formatting string used to add extra space to value. Concatinating string made the text file blank for some reason
                                                            # I added the extra space because it seems to be written out without the space for some reason idk

            print(f"Success. \n{' '.join(inventory_item)}")  # The join converts array into string
            flag = True

            
        
    if flag == False:                               # Result if no such name is found
        print("Error, please try again. ")

    else:                                           # Once all necessary operations have/not been done, we finally update the file again into plaintext
        for inventory_item in inventory_list:       # Iterating over the 2D array
            
            inv_str = ''                            # An empty string is created to store individual arrays at a time whe converted into string
            # The comma is a delimiter in the operation below (meaning it seperates each individual item of the array when we convert the list into string)
            
            inv_str +=  ','.join(inventory_item)    # The join function helps us to join each item in the array and uses the comma in between as a delimiter to create a string
            updated_value.write((inv_str))                   # The final line is then written into file in plaintext format

    updated_value.close()


