import inventory

def remove_item():
    item_list = inventory.show_inventory()
    with open("inventory.txt", "w") as file:
        item_to_remove = input("Enter the laptop model you would like to remove: ")
        removed_list = []
        final_list = []

        for item in item_list:
            if item[0] == item_to_remove:   
                continue
            
            removed_list.append(item)
        
        for new_item in removed_list:
            final_item = ','.join(new_item)
            final_list.append(final_item)

        file.write(str(''.join(final_list)))

