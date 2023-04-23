from tabulate import tabulate       # this is for creating the table for invoice
import date_time                    # importing this file for date
import random                       # for generating random number
import table
def print_receipt(receipt_data, recipient_name, who_ordered):
    invoice_num = random.randint(1000, 9999)
    file_name = f"{recipient_name}_{date_time.local_time()}_{invoice_num}"  # An invoice number to avoid overwriting two files with same name
    file_name_ = f"{file_name}.txt".replace("/","")              # Remove '/' because when creating a file python treats the date's slash as a directory escape sequence
    
    if (who_ordered == "manufacturer"):                 # Data is stored in separate files for easier reference
        file = open("receipts/manufacturer/" + file_name_, "w")     
    elif (who_ordered == "customer"):
        file = open("receipts/customer/" + file_name_, "w")

    # the file = file is used after each print statement to write the console output into the file
    # The print statements have been repeated to print in console
    
    print('''
        =======================================================
                            Invoice
        =======================================================
    ''', file=file)
    
    print('''
        =======================================================
                            Invoice
        =======================================================
    ''')

    # Prints top half of information of the client
    
    # Name acc to whether we are selling/buying
    if (who_ordered == "manufacturer"):
        print(f"Sold by: {recipient_name}", file=file)
        print(f"Sold by: {recipient_name}")
    elif (who_ordered == "customer"):
        print(f"Customer name: {recipient_name}", file=file)
        print(f"Customer name: {recipient_name}")

    print(f"Invoice number: {invoice_num}", file=file)
    print(f"Date of purchase: {date_time.local_time()}\n\n", file=file)    # Gives local date from date_time.py file
    print(f"Date of purchase: {date_time.local_time()}\n\n")    

    file.close()    # Closing file because it is opened in table.py and opening the same file simultaneously causes writing problems

    # Prints the table of all the items purchased
    header = ["Laptop Model", "Brand Name", "Price", "Qty", "Total"]    
    if (who_ordered == "manufacturer"):   
        print(table.table(receipt_data, header, "receipt", "manufacturer", file_name_))       
    elif (who_ordered == "customer"):
        print(table.table(receipt_data, header,  "receipt", "customer", file_name_))       

    # opening file again in append more because we need to update data on the same file
    if (who_ordered == "manufacturer"):                 # Data is stored in separate files for easier reference
        file = open("receipts/manufacturer/" + file_name_, "a")     
    elif (who_ordered == "customer"):
        file = open("receipts/customer/" + file_name_, "a")

    # receipt_date is the paramter for the 2D list which holds the purchased item info
    # headers paramter takes parameter for the header row
    # tablefmt parameter takes in the format to be displayed.

    sub_total = get_sub_total(receipt_data)             # This pulls the sum of data from the Total column of the table to give a subtotal
    print("{:<45}Sub total:  ${:<1}".format(" ", sub_total), file=file)    # Prints the total below the table
    print("{:<45}Sub total:  ${:<1}".format(" ", sub_total))    
    # :< inside the quotes represents the left spacing with the int representing no of columns
    # the " " and sub_total are values which will be placed in the placeholders respectively, kinda like printf in C
    print(" {:<50}VAT:\t  {:<5}".format(" ", "13%"), file=file)
    print(" {:<50}VAT:\t  {:<5}".format(" ", "13%"))
    print("{:<39}Delivery charge:   {:<1}".format(" ", "2%"), file=file)
    print("{:<39}Delivery charge:   {:<1}".format(" ", "2%"))
    grand_total = (sub_total + (sub_total + (sub_total*0.13))*0.02)
    print("{:<43}Grand total:  ${:<1}".format(" ", grand_total), file=file)
    print("{:<43}Grand total:  ${:<1}".format(" ", grand_total))

    
    print(f"\n\nThank you for your purchase.\nIn case of any problem, track your order using {file_name}", file=file)
    print(f"\n\nThank you for your purchase.\nIn case of any problem, track your order using {file_name}")
    file.close()

def get_sub_total(receipt_data):            # For calculating grand total for all the items purchased (excl taxes and service charge)
    sum = 0
    for total_row in receipt_data:                  # Iterates over each list within the 2D list
        row_value = total_row[-1].strip(" $")       # Finds the last value (Total in this case) and removes the $ for operation
        sum += int(row_value)                       # Sum is added over each iteration
    
    return sum
