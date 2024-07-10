
global d
global customer_info


def stocks():
    '''Reads Stock txt and returns a list of stock items.'''

    global d
    d = []  # Initialize a global list to store stock data

    file = open("Stock.txt", "r")  # Open the Stock.txt file in read mode
    data = file.read()  # Read the entire content of the file
    file.close()  # Close the file
    data_split = data.split("\n")  # Split the data into lines

    itemid = 1  # Initialize an item ID counter

    # Loop through each line of data and extract stock item details
    for i in data_split:
        if i:
            a = i.strip().split(', ')
            if len(i) >= 4:
                name = a[0]
                brand = a[1]
                price = int(a[2])
                quantity = int(a[3])
                itmid = itemid
                d.append({'a': name, 'b': brand, 'c': price, 'd': quantity, 'e': itmid})
                itemid = itemid + 1  # Increment the item ID
    return d  # Return the list of stock items


def dis_play():
    '''Displays Stock in a detailed format.'''
    global d
    print("_" * 80)
    print('|' + " " * 30 + "Your Stocks" + " " * 37 + '|')
    print('|' + "_" * 78 + '|')
    for e in d:
        print("-" * 79)
        print(" " * 28 + "", "|" + e['a'] + "|")
        print("Brand:", e['b'])
        print("Price($):", e['c'])
        print("Stock amount:", e['d'])
        print(" " * 65 + "Item ID:", e['e'])
    print("-" * 79)
    print("_" * 80)


def display2():
    '''Displays Stock in a minimalist table format for later reference.'''
    global d
    print("_" * 72)
    print("|" + " " * 32 + "Stocks" + " " * 33 + "|")
    print("|" + "_" * 71 + "|")
    print("|{:7} | {:20} | {:15} | {:8} | {:8} |".format("Item ID", "Item", "Brand", "Price", "Stock"))
    print("|" + "-" * 8 + "|" + "-" * 22 + "|" + "-" * 17 + "|" + "-" * 10 + "|" + "-" * 10 + "|")
    for e in d:
        print("|{:7} | {:20} | {:15} | {:8} | {:8} |".format(e['e'], e['a'], e['b'], ("$" + str(e['c'])), e['d']))
    print("|" + "-" * 8 + "|" + "-" * 22 + "|" + "-" * 17 + "|" + "-" * 10 + "|" + "-" * 10 + "|")


def get_customer_info(cos_name):
    '''Gets customer information from a customer file.'''

    file_path = cos_name.replace(" ", "") + "_transaction.txt"
    with open(file_path, 'r') as file:
        lines = file.readlines()  # Read the lines of the file

    customer_info = {"phone_num": None, "address": None, "days": None}

    # Loop through each line of the file and extract customer details
    for line in lines:
        if 'Phone No' in line:
            customer_info["phone_num"] = line.strip().split(': ')[1]
        elif 'Address' in line:
            customer_info["address"] = line.strip().split(': ')[1]
        elif 'Days Rented' in line:
            customer_info["days"] = line.strip().split(': ')[1]

    # Set a default value for "days" if it's missing
    if customer_info["days"] is None:
        customer_info["days"] = 0

    return customer_info


'''Used for testing display '''
if __name__ == "__main__":
    stocks()
    dis_play()
    display2()