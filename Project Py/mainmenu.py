import read  # Importing Functions from read
import operation  # Importing Functions from operation
import time


def main():
    """Main function of the Programme"""
    while True:  # Starting an infinite loop
        try:  # Adding Exception handling to prevent Crash
            time.sleep(0.5)

            # Displaying main menu options
            print("_" * 80)
            print("|" + "-" * 33 + ">>>Press<<<" + "-" * 33 + "|")
            print("_" * 80)
            print("1. Display Available Stocks")
            print("2. Rent or Return Items")
            print("3. Exit program")
            print("=" * 80)
            print("|" + "-" * 26 + "|Waiting for user input|" + "-" * 26 + "|")
            print("=" * 80)

            user_input = int(input("What would you like to do?:"))  # Asking for user input
            print("=" * 80)

            # Handling user choices
            if user_input == 1:  # For displaying Stocks
                print("Available Stocks......")
                read.stocks()
                read.dis_play()

                # Displaying submenu options
                print("|" + "-" * 33 + ">>>Press<<<" + "-" * 33 + "|")
                print("_" * 80)
                print("1. Rent or Return Items")
                print("3. Exit program")
                print("=" * 80)

                user_input1 = int(input("What would you like to do?:"))

                # Handling submenu choices
                if user_input1 == 1 or user_input1 == 2:
                    operation.rent_receive()

                elif user_input1 == 3:
                    print("exit")
                    break
                else:
                    print("-" * 80)
                    print("Invalid Input...")
                    print("-" * 80)

            elif user_input == 2:  # For Operation Rent or Return
                operation.rent_receive()  # Calling Function rent_receive
                print("Operation Successful")
                print("=" * 80)
                continue
            elif user_input == 3:  # To Exit program
                print("Exiting program...........")
                print("Thank you for using our service.....")
                break

            else:  # Restart Loop for invalid input
                print("-" * 80)
                print("Invalid Input...")
                print("-" * 80)

        except:  # Displaying Error message
            print("--" * 30)
            print("An Error Occurred, please try again")
            print("--" * 30)
            print("=" * 80)


def Welcome():
    """Displaying Controls and Welcome message"""
    print("  " + "_" * 78)
    print("|" + " " * 27 + " WELCOME TO BLACK WATER " + " " * 28 + "|")
    print("|" + " " * 33 + " RENTAL SHOP " + " " * 33 + "|")
    print("  " + "_" * 78)
    print(" " * 25 + "      User Controls!!")
    print(" " * 25 + "=============================")
    time.sleep(0.5)
    print(" " * 25 + "|" + "Press 1-3 on selection Menu|")
    print(" " * 25 + "|" + "---------------------------|")
    time.sleep(0.4)
    print(" " * 25 + "|" + "  Type (yes/1/y) for Yes   |")
    print(" " * 25 + "|" + "  and   (no/2/n) for No.   |")
    print(" " * 25 + "=============================")


if __name__ == "__main__":  # For running this main program
    Welcome()
    main()
