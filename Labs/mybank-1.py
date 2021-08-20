"""
Program Descriptions: A small bank application that allows an user
    to open an account, deposit money, withdraw, and show balance.
Name: Audrey Zhu
Lab 1: My Small Bank Application
"""

# defining variables
opened = False      # turn true when account has been opened
leave = False       # turn true after 5 is pressed
name = ""           # set to something when opening an account
balance = 0         # set to a valid number when opening account


def showoptions():
    # print the options
    print("Please choose one of the following:")
    print("\t1. Open an account")
    print("\t2. Deposit")
    print("\t3. Withdraw")
    print("\t4. Show balance")
    print("\t5. Exit")

    # get option from user
    opt = input("\nEnter your option: ").strip()

    # check if user entered an invalid choice
    if opt == "" or not opt.isnumeric():
        return 0

    return int(opt)


# openning account
def openaccount():
    global name
    global balance
    global opened
    # check if account is initialized
    if not opened:
        name = input("Enter the owner's name: ").strip()
        # check if name is inputted properly
        if name == "":
            print("You need to input a name.")
        else:
            placeholder = input("Enter initial balance: $")
            # check if balance is a valid number
            if not isvalidamount(placeholder.strip()):
                pass
            else:
                balance = float(placeholder)
                opened = True
    else:
        print("This option is no longer available. Please try it again.")


# deposit money into balance
def deposit():
    global balance
    # check if account has been opened
    if not opened:
        print("This option is not available until you open an account. "
              "\nPlease select option 1 to open an account.")
    else:
        placeholder = input("Enter deposit amount: $")
        # check if amount is valid
        if not isvalidamount(placeholder.strip()):
            pass
        else:
            depositammount = float(placeholder)
            # check if amount is positive
            if depositammount >= 0:
                balance = balance + depositammount
            else:
                print("The deposit amount must be positive.")


# withdraw money from balance
def withdraw():
    global balance
    # check if account has been opened
    if not opened:
        print("This option is not available until you open an account. "
              "\nPlease select option 1 to open an account.")
    else:
        placeholder = input("Enter withdrawal amount: $")
        # check if amount is valid
        if not isvalidamount(placeholder.strip()):
            pass
        else:
            withdrawal = float(placeholder)
            # check if amount is less than balance
            if withdrawal > balance:
                print("You can not withdraw more than your balance of ${:.2f}".format(balance))
            else:
                balance = balance - withdrawal
                print("Please take your cash.")


# display account information
def showbalance():
    # check if account has been opened
    if not opened:
        print("This option is not available until you open an account. "
              "\nPlease select option 1 to open an account.")
    else:
        # print name and balance
        print("Name: ", name)
        print("Your balance: ${:.2f}".format(balance))


# check is amount is valid
def isvalidamount(amount):
    # check if amount is a number
    if amount == "" or (not amount.isnumeric()):
        # check if amount is positive or if it contains letters
        if amount == "":
            print("The amount must be a numeric value")
        elif amount[0] == "-":
            print("The amount must be positive")
        elif "." in amount:
            # check if amount is decimal
            return checkdecimal(amount)
        else:
            print("The amount must be a numeric value")
        return False
    return True


def checkdecimal(amount):
    # amount cannot end in a decimal
    if amount[len(amount) - 1] == '.':
        print("The amount must be a numeric value")
        return False
    # split string into parts without .'s
    decimal = amount.split(".")
    # should not be more than 2 items, otherwise would look like 127.0.0.1
    if not len(decimal) == 2:
        print("The amount must be a numeric value")
        return False
    # if starts with period, it should work
    if amount[0] == "." and decimal[1].isnumeric():
        return True
    # if both items are numerical, it is a number
    for i in decimal:
        if not i.isnumeric():
            print("The amount must be a numeric value")
            return False
    return True


# ---------- MAIN PROGRAM ----------

print("Welcome to my small bank.")

# when exit is has not been chosen, repeat the following
while not leave:
    action = showoptions()

    # what to do with action
    if action == 1:
        openaccount()
    elif action == 2:
        deposit()
    elif action == 3:
        withdraw()
    elif action == 4:
        showbalance()
    elif action == 5:
        print("\nThank you for using my bank application.")
        leave = True
    else:
        print("\nInvalid Selection. Please try it again.")

    print("\n")
