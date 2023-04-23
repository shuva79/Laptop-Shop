import inventory
import customer_actions
import receipt

def customer_orders():
    print('''
        =======================================================
                            Customer
        =======================================================
    ''')
    
    confirm  = "y"     # This is for the user to enter multiple orders while it is true
    company_name = input("Enter customer name: ")
    receipt_list_2d = []                            # An empty 2D list is created which will be used as parameter to pass to print_recepit() function

    while True:
        print("\nAvailable items:\n")
        inventory.show_inventory_readable()
        item_order = input("Enter the laptop model: ")
        item_qty = int(input("Enter the number of laptops: "))
        search_inventory = inventory.show_inventory()
        count = 0


        for search_name in search_inventory:                           # iterating over the 2D list
            #print(search_name[0])                                     # this for debugging purposes
            if search_name[0] == item_order:                           # condition if laptop model is found
                customer_actions.order_items(item_order, item_qty)       # also for debugging purposes
                receipt_list_1d = customer_actions.selected_items_table(item_order, item_qty)
                receipt_list_2d.append(receipt_list_1d)
                count += 1
        confirm  = input("Continue? (y/n): ").lower()

        if (confirm != "y"):
            break
    
    if count != 0:
        receipt_list_2d_final = []   # copy() ensures that manipulating one value wont result in changes in the other value
        repeated_items = []
        for index, receipt_list_1 in enumerate(receipt_list_2d):   
            for i in range(index+1, len(receipt_list_2d)):
                if receipt_list_1[0] == receipt_list_2d[i][0] and receipt_list_1[0] not in repeated_items:
                    repeated_items.append(receipt_list_1[0])
                    receipt_sum = receipt_list_1[3] + receipt_list_2d[i][3]
                    updated_receipt_data = customer_actions.selected_items_table(receipt_list_1[0], receipt_sum)
                    receipt_list_2d_final.append(updated_receipt_data) 
                    break       

            if receipt_list_1[0] not in repeated_items:
                receipt_list_2d_final.append(receipt_list_1)  
                 
        receipt.print_receipt(receipt_list_2d_final, company_name, "customer")      # Calling the function print_receipt() under receipt.py which prints the final receipt of the product ordered
        exit 

    else:
        print(f"\nItem not found try again")
        