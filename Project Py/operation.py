import read
import write
import datetime
import time

toggle = 0  # toggle 0 'off' used for writing old customer data in the bill


def rent_receive():
    '''Creating main function of operation'''
    while True:
        print("="*80)
        print(" "*32+"Customer information")
        print("-"*80)
        while True:
            try:
                # imported for file and variable scanning
                import os
                cos_name = input("Enter Name:")  # Customer name
                global bill_cos # Customer name for bill without using ID
                bill_cos = cos_name

                if not cos_name.strip() or cos_name.isdigit():  # checking if name contains String values or not
                    print("Name cannot be Empty or just Numbers!!!!")
                    print("-" * 80)
                    continue

                file_name = cos_name.replace(" ", "")+"_transaction.txt"
                cos_details = []  # Making dictionary for customer information

                if os.path.exists(file_name):  # Checking if duplicate name already exists
                    while True:
                        oldcosin = input("Old user with same name detected!!,Is this Previous Customer?(Yes,NO):")  # Asking if its new customer or old
                        oldcos=oldcosin.lower()
                        if oldcos in ['yes', 'y', '1']:  # If old customer
                            print("\n   Welcome Back " + cos_name)
                            print("------------------------------------")
                            global toggle
                            toggle = int(1)
                            customer_info = read.get_customer_info(cos_name)
                            cos_details.append(int(customer_info["phone_num"]))
                            cos_details.append(customer_info["address"])
                            cos_details.append(int(customer_info["days"]))
                            # asking if user have assigned ID given by the programme for having duplicate name
                            userhaveid1 = input("Does this user have system assigned ID(check ID in txt file)?(Yes/No):")
                            userhaveid=userhaveid1.lower()

                            if userhaveid in ['yes', 'y', '1']:  # If user have ID
                                userID = (input("Enter User assigned ID:"))
                                newcos_name = cos_name+" ID-"+userID  # Checking where if the ID exist or not
                                file_name1 = newcos_name.replace(" ", "") + "_transaction.txt"

                                if os.path.exists(file_name1):# checking if id exists
                                    cos_name += " ID-"+userID
                                    print("ID found!")
                                else:
                                    print("ID not Found!! Please recheck ID!")
                                    continue

                            elif userhaveid in ['no', 'n', '2']:
                                print("User with no ID")
                            else:
                                print("Invalid input!")
                                continue

                        elif oldcos in ['no', 'n', '2']:
                            print("adding new Customer to the database...")# assigning new ID to new customer with same name
                            import random
                            ran_id = random.randint(1000, 9999)
                            cos_name = cos_name + " ID-" + str(ran_id)
                            while True:
                                try:
                                    cos_details.append(int(input("Enter Phone.No:")))
                                    cos_details.append(input("Enter Address:"))
                                    cos_details.append(int(0))
                                    break

                                except:
                                    print("Please only user numbers while typing Phone number!!.")

                        else:
                            print("Invalid input!")
                            continue

                        break
                else:
                    while True:
                        try: # Getting customer Phone no and Address from user
                            cos_details.append(int(input("Enter Phone.No:")))
                            cos_details.append(input("Enter Address:"))
                            cos_details.append(int(0))
                            break
                        except:
                            print("Please only user numbers while typing Phone number!!.")


                print("_" * 80)
                print("|" + "-" * 33 + ">>>Press<<<" + "-" * 33 + "|")
                print("_" * 80)
                print("1. Rent to Items")
                print("2. Return to Items")
                print("3. Menu")

                while True:
                    user_inputop = input("What would you like to do?:")
                    if user_inputop == '1':
                        rent(cos_name, cos_details, toggle)
                        break
                    elif user_inputop == '2':
                        return_(cos_name, cos_details, toggle)
                        break
                    elif user_inputop == '3':
                        break
                    else:
                        print("Please enter 1 , 2 or 3")
            except:
                print("--" * 30)
                print("An Error Occurred, please try again!!")
                print("--" * 30)
                print("=" * 80)
            break
        break

def rent(cos_name, cos_details, toggle):
    '''Rent operation'''
    print("-" * 80)
    print(" "*32+"Renting Items")
    print("-" * 80)
    item_details = []
    total_amount = 0
    current_date = datetime.datetime.now().date()
    current_time = time.strftime("%H:%M:%S")
    while True:
        try:
            days = int(input("How many days would you like to rent??"))# no of days to rent
            if days>=1:
                daystorent = days
            else:
                print("You can't rent bellow 1 Day")
                continue
            break
        except:
            print(" Please Enter numeric values only ")
    loop = True
    while loop:
        try:
            read.stocks()
            read.display2()
            item_ID = int(input("Enter item ID:")) - 1
            if 0 <= item_ID < len(read.d):#  checking if its valid id
                quantity = int(input("How many would you like you like to rent?:"))
                if 0 <= quantity <= read.d[item_ID]['d']:    # if its valid quantity
                    item_name = read.d[item_ID]['a']
                    brand_name = read.d[item_ID]['b']
                    price = read.d[item_ID]['c']

                    if daystorent <= 5:  # Calculating on 5 days basics
                        amount1 = price * quantity * 5
                    elif daystorent % 5 == 0:
                        amount1 = price * quantity * daystorent
                    else:
                        amount1 = price * quantity * ((daystorent // 5) * 5 + 5)

                    total_amount+=amount1  # adding amount total amount
                    read.d[item_ID]['d'] -= quantity

                    item_details.append({  # storing item info for later use
                        'item_name': item_name,
                        'brand_name': brand_name,
                        'price': price,
                        'quantity': quantity,
                        'amount1': amount1
                    })
                    write.stock_update(read.d)    # Updating stock
                    print(">>>>Item added!<<<<")

                elif quantity <=0 :
                    print("Please Enter a Positive Number")
                    continue
                else:
                    print("Not sufficient amount!, Please recheck stocks")
                    print("Try again")
                    continue
            else:
                print("Invalid ID!!, Please Try again!")
                continue

            while True:
                loop_con = input("---------------------------------- \nDo you want to add another item? (Yes/No)")
                print("----------------------------------")
                loop_lower = loop_con.lower()

                if loop_lower in ['yes', 'y', '1']:
                    break  # Exit and continue with the next item

                elif loop_lower in ['no', 'n', '2']:
                    loop = False  # Exit loop
                    break
                else:
                    print("Invalid Input!!, Please try again!!")

        except:
            print("--" * 30)
            print("An Error Occurred!!, please try again!")
            print("--" * 30)
            print("=" * 80)

    if toggle == 1:  # calling functing to generate invoice
        write.genaddmorerent(cos_name, item_details, total_amount, current_date, current_time,daystorent)
    else:
        write.genrent(cos_name, cos_details, item_details, total_amount, current_date, current_time,daystorent)

    print("=" * 80)
    print("BILL")
    print("-" * 80)
    print("Customer Name:", cos_name + " "*(40-len(cos_name)) + "Date: " , current_date)
    print("Phone Number:", str(cos_details[0]) + " "*(43 - len(str(cos_details[0]))) +"Time: ", current_time)
    print("\n"+" " * 45+" Address:", cos_details[1])
    print("Days Rented:",daystorent)
    print("-" * 80)
    print("Item Names" + " " * 35 + "Quantity |" + " PriceperDay|" + " Total")
    print("-" * 80)
    for item in item_details:
        print(item['item_name'] + " (" + item['brand_name'] + ")" + " " * (45 - len(item['item_name']) -
                len(item['brand_name'])) +str(item['quantity']) + " " * (11 - len(str(item['quantity']))) +
              "$" + str(item['price']) + " " * (10 - len(str(item['price']))) +"$" + str(item['amount1']))
    print("-" * 80)
    print("Total Amount:"+"$"+str(total_amount))
    print("\nNote: If not returned within the frame 40% extra charge will be added each day")
    print("=" * 80)
    global bill_cos
    print(bill_cos + " Thank you for choosing Black Water Rentals.")
    print("-" * 80)
    print("Going to main menu...")


def return_(cos_name , cos_details ,toggle):
    '''Return Operation'''
    print("-" * 80)
    print(" " * 32 + "Return Items")
    print("-" * 80)
    current_date = datetime.datetime.now().date()
    current_time = time.strftime("%H:%M:%S")
    delaysdays = 0
    while True:
        delayin = input("Is the customer late?(Yes/No)")
        delay = delayin.lower()
        if delay in ['yes', 'y', '1']:
            delaysdays = int(input("By how many days?"))  # Numer of days late
            if delaysdays<=0:
                print("Error, Try again")
                continue
            else:
                print("Extra 40% will be charged in each item")
            break
        elif delay in ['no', 'n', '2']:
            print("On Time!")
            break
        else:
            print("Invalid Input!!, Please try again!!")
            continue
    if cos_details[2] == 0:   # If there is no data from rent
        daystorent = "N/A"
        returnedafter = "N/A"
    else:
        daystorent = cos_details[2]
        returnedafter = daystorent + delaysdays
    print("Please enter the ID of the Item you would like to return")
    total_amount = 0
    global fine
    fine = 0
    item_details = []
    loop = True
    read.stocks()
    read.display2()
    while loop:
        try:
            item_ID = int(input("Enter item ID:")) - 1
            if 0 <= item_ID < len(read.d):
                quantity = int(input("Enter the number of amount being returned:"))
                if quantity > 0:
                    price = read.d[item_ID]['c']
                    fine = int((((40 / 100) * price)+price) * delaysdays * quantity)  # calculating fine on per day bacis
                    total_amount += fine
                    item_name = read.d[item_ID]['a']
                    brand_name = read.d[item_ID]['b']
                    price = read.d[item_ID]['c']
                    read.d[item_ID]['d'] += quantity
                    item_details.append({
                        'item_name': item_name,
                        'brand_name': brand_name,
                        'price': price,
                        'quantity': quantity,
                        'amount1': fine})
                    write.stock_update(read.d)
                else:
                    print("Invalid Quantity")
                    continue
            else:
                print("Invalid ID!!, Please Enter Again!")
                continue

            while True:
                loop_con = input("----------------------------------\nDo you want to Return another item? (Yes/No):")
                print("----------------------------------")
                loop_lower = loop_con.lower()

                if loop_lower in ['yes', 'y', '1']:
                    break  # Exit inner loop and continue with the next item

                elif loop_lower in ['no', 'n', '2']:
                    loop = False  # Exit outer loop and stop returning items
                    break
                else:
                    print("Invalid Input!!, Please try again!!")
        except:
            print("--" * 30)
            print("An Error Occurred!!, please try again!")
            print("--" * 30)
            print("=" * 80)

    if toggle == 1:  # calling functing to generate invoice
        write.genaddmorereturn(cos_name ,cos_details, item_details, total_amount, current_date, current_time,delaysdays)
    else:
        write.genreturn(cos_name, cos_details, item_details, total_amount,current_date, current_time,delaysdays)

    print("=" * 80)
    print("BILL")
    print("-" * 80)
    print("Customer Name:", cos_name + " " * (40 - len(cos_name)) + "Date: ", current_date)
    print("Phone Number:", str(cos_details[0]) + " " * (43 - len(str(cos_details[0]))) + "Time: ", current_time)
    print("\n" + " " * 45 + " Address:", cos_details[1])
    print("Days Rented:", str(daystorent) + " " * 30 + "Returned After:", returnedafter)
    print("Days Delay:",delaysdays)
    print("-" * 80)
    print("Item Names" + " " * 35 + "Quantity |" + " PriceperDay|" + "Fine")
    print("-" * 80)
    for item in item_details:
        print(item['item_name'] + "(" + item['brand_name'] + ")" + " " * (45 - len(item['item_name']) -len(item['brand_name'])) + str(item['quantity']) + " " * (11 - len(str(item['quantity']))) +"$" + str(item['price']) + " " * (10 - len(str(item['price']))) + "$" + str(item['amount1']))
    print("-" * 80)
    print("Total Fine Amount:" + "$" + str(total_amount))
    global bill_cos
    print(bill_cos + " Thank you for choosing Black Water Rentals.")
    print("Please vist us again")
    print("-" * 80)
    print("Going to main menu...")




'''#for bug fixing
if __name__=="__main__":
    rent_receive()
'''
