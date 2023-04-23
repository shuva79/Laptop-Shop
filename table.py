def table(items_list, header, type_of_data, who_ordered = "", file_name = ""):   # the two arguments type_of_data and file_name are option arguments and if no argument is passed, the default value is passed
    
    col_width = []
    # the zip function joins the list of similar items into a single tuple eg, items_list[0] are bundled together
    for data_col in zip(*items_list): 
        length = 0          # * iterates over columns instead of rows in a 2d list
        for data_item in data_col:
            length = max(length,len(str(data_item))) 
            # the two arguments are first compared and the value returned is the maximum value possible of the two2
            # max returns the maximum value of the variable
            # data item is converted into string and then its length is calculated
        for header_item in header:
            length = max(length, len(str(header_item)))
            # the length of the header is also compared to see the maximum space each column may take 

    # entire loop effectively turns the table into rows and columns, grouping similar items into a tuple
    # then, the length of individual element is calculated for the width of column
        col_width.append(length)

    # The loop above first iterates over each column of the 2D array and then the 2nd loop determinds the maximum length
    # in the column which is then added to the column width array and then added to the col_width array
    
    # this provides spacing beween the headers of the table
    print(" | ".join(str(word).ljust(width) for word,width in zip(header, col_width)))
    
    # this provides the = thingy between data and header
    for col in col_width:
        print(("=" * (int(col)+2)).ljust(col), end="")
        # we use end = "" because it helps to prevent newline from being created
    print()

    # this provides spacing between elements in a column
    for row in items_list:
        print(' | '.join(str(word).ljust(width) for word, width in zip(row, col_width)))
    print()
    

    # effectively does the same thing done in terminal but writes into the file

    if type_of_data == "receipt":
        if (who_ordered == "manufacturer"):                 # Data is stored in separate files for easier reference
            file = open("receipts/manufacturer/" + file_name, "a")     
        elif (who_ordered == "customer"):
            file = open("receipts/customer/" + file_name, "a")
        print(" | ".join(str(word).ljust(width) for word,width in zip(header, col_width)), file=file)
        
        for col in col_width:
            print(("=" * (int(col)+2)).ljust(col), end="", file=file)
        
        print(file=file)
        for row in items_list:
            print(' | '.join(str(word).ljust(width) for word, width in zip(row, col_width)), file=file)
        print(file=file)
    
        file.close()
    return ""