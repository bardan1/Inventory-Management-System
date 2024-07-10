
def genrent(cos_name, cos_details, item_details, total_amount, current_date, current_time, daysrented):
    '''Creating rent txt file'''
    # Generate the filename by replacing spaces with underscores
    filename = cos_name.replace(" ", "") + "_transaction.txt"
    # Open the file in write mode and use 'rental' as a file object
    with open(filename, 'w') as rental:
        # Writing the header and customer information
        rental.write("*******************************************************" + "\n")
        rental.write("*                                                     *" + "\n")
        rental.write("*             BLACK WATER RENTAL SHOP                 *" + "\n")
        rental.write("*                                       -Durbar Marg  *" + "\n")
        rental.write("*******************************************************" + "\n")
        rental.write("|                         Rent!!                       |\n")
        rental.write("|------------------------------------------------------|\n")
        rental.write("|                      Customer Info                   |\n")
        rental.write(" *******************************************************\n")
        rental.write("Customer Name: " + str(cos_name) + " " * (26 - len(cos_name)) + "Date:" + str(current_date) + "\n")
        rental.write("Phone No: " + str(cos_details[0]) + "\n" + "Address: " + cos_details[1] + "\n")
        rental.write("Days Rented: " + str(daysrented) + "\n" + "Time:" + str(current_time) + "\n")
        rental.write("========================================================\n")
        rental.write("                       Item Rented\n")
        rental.write("========================================================")
        rental.write("\n")
        # Writing rented items details
        for i in item_details:
            rental.write("Item name:" + i['item_name'] + " " * (22 - len(i['item_name'])) + "Brand:" + i['brand_name'] + "\n")
            rental.write("\nPrice per day: " + "$" + str(i['price']) + "\n")
            rental.write("\nQuantity Rented: " + str(i['quantity']) + "\n")
            rental.write("                                   Sub Total: " + "$" + str(i['amount1']) + "\n")
            rental.write("--------------------------------------------------------" + "\n")
        rental.write("Total Charge: " + "$" + str(total_amount) + "\n")
        rental.write("========================================================")



def genreturn(cos_name,cos_details,item_details, total_amount ,current_date, current_time,delaysdays):
    '''creating return txt file'''
    filename = cos_name.replace(" ","") + "_transaction.txt"
    with open(filename,'w') as rental:
        # Writing the header and customer information
        rental.write("*******************************************************" + "\n")
        rental.write("*                                                     *" + "\n")
        rental.write("*             BLACK WATER RENTAL SHOP                 *" + "\n")
        rental.write("*                                       -Durbar Marg  *" + "\n")
        rental.write("*******************************************************" + "\n")
        rental.write("|                         Return!!                       |\n")
        rental.write("|------------------------------------------------------|\n")
        rental.write("|                      Customer Info                   |\n")
        rental.write(" *******************************************************\n")
        rental.write(
            "Customer Name: " + str(cos_name) + " " * (26 - len(cos_name)) + "Date:" + str(current_date) + "\n")
        rental.write("Phone No: " + str(cos_details[0]) + "\n" + "Address: " + cos_details[1]+"\n")
        rental.write("Days Delay: " + str(delaysdays) + "\n" + "Time:" + str(current_time) + "\n")
        rental.write("========================================================\n")
        rental.write("                       Item Returned\n")
        rental.write("========================================================")
        rental.write("\n")
        for i in item_details:# Writing returned items details
            rental.write(
                "Item name:" + i['item_name'] + " " * (22 - len(i['item_name'])) + "Brand:" + i['brand_name'] + "\n")
            rental.write("\nPrice per day: " + "$" + str(i['price']) + "\n")
            rental.write("\nQuantity Returned: " + str(i['quantity']) + "\n")
            rental.write("                                   Fine: " + "$" + str(i['amount1']) + "\n")
            rental.write("--------------------------------------------------------" + "\n")
        rental.write("Total Fine: " + "$" + str(total_amount) + "\n")
        rental.write("========================================================")


def genaddmorerent(cos_name,item_details, total_amount,current_date, current_time,daysrented):
    '''append new rent'''
    filename = cos_name.replace(" ", "") + "_transaction.txt"
    with open(filename, 'a') as rental:
        rental.write("\n")
        rental.write("|                         Rent!!                       |\n")
        rental.write("|------------------------------------------------------|\n")
        rental.write("Date:" + str(current_date) + " " * 16 + "Time:" + str(current_time) + "\n"+"DayRented: " + str(daysrented) + "\n")
        rental.write("--------------------------------------------------------" + "\n")
        rental.write("\n")
        for i in item_details:
            rental.write("Item name:" + i['item_name'] + " " * (22 - len(i['item_name'])) + "Brand:" + i['brand_name'] + "\n")
            rental.write("\nPrice per day: " + "$" + str(i['price']) + "\n")
            rental.write("\nQuantity Rented: " + str(i['quantity']) + "\n")
            rental.write("                                   Sub Total: " + "$" + str(i['amount1']) + "\n")
            rental.write("--------------------------------------------------------" + "\n")
        rental.write("Total Charge: " + "$" + str(total_amount) + "\n")
        rental.write("========================================================")


def genaddmorereturn(cos_name ,cos_details, item_details, total_amount, current_date, current_time,delaysdays):
    '''append new return'''
    filename = cos_name.replace(" ", "") + "_transaction.txt"
    with open(filename, 'a') as rental:# Writing date, time, days rented, and item details for additional rental
        rental.write("\n")
        rental.write("|                       Return!!                       |\n")
        rental.write("|------------------------------------------------------|\n")
        rental.write("Date:" + str(current_date) + " " * 16 + "Time:" + str(current_time) + "\n"+"DayRented: " +
                     str(cos_details[2])+" "*16 +"Days Late: "+str(delaysdays) + "\n")
        rental.write("--------------------------------------------------------" + "\n")
        rental.write("\n")
        for i in item_details:
            rental.write("Item name:" + i['item_name'] + " " * (22 - len(i['item_name'])) + "Brand:" + i['brand_name'] + "\n")
            rental.write("\nPrice per day: " + "$" + str(i['price']) + "\n")
            rental.write("\nQuantity Returned: " + str(i['quantity']) + "\n")
            rental.write("                                   Fine: " + "$" + str(i['amount1']) + "\n")
            rental.write("--------------------------------------------------------" + "\n")
        rental.write("Total Fine: " + "$" + str(total_amount) + "\n")
        rental.write("========================================================")


def stock_update(updated_stock):
    '''Update Stock txt'''
    with open("Stock.txt", "w") as sub_stock:
        for item in updated_stock:
            sub_stock.write(item['a']+', '+item['b']+', '+str(item['c'])+', '+str(item['d'])+" \n")




