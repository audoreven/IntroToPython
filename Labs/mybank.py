"""
Program Descriptions: A small bank application that allows an user
    to open an account, deposit money, withdraw, and show balance.
Name: Audrey Zhu
Lab 4: My Small Bank Application
"""

from BankAccount import Account, NegativeBalance

# maps account ID to an Account object
user_accounts = {}


def show_options():
    """
    Displays all the options available for user
    :return: the option value
    """
    # print the options
    print("Please choose one of the following:")
    print("\t1. Open an account")
    print("\t2. Deposit")
    print("\t3. Withdraw")
    print("\t4. Show balance")
    print("\t5. Show transactions")
    print("\t6. Exit")

    # get option from user
    opt = input("\nEnter your option: ").strip()
    if opt == "":
        print("The amount must be a numeric value.")
        return -1

    try:
        return int(opt)
    except TypeError:
        print("The amount must be a numeric value.")
    return -1


# openning account
def open_account():
    """
    Opens an account for the user
    :return: string saying if the account has been created or not
    """
    name = input("Enter the owner's name: ")
    try:
        amt = int(input("Enter the initial balance: ")) * 100
        if amt < 0:
            try:
                raise NegativeBalance("Initial balance must be positive.")
                return "Failed to create account."
            except NegativeBalance as error:
                print(error)
                return "Failed to create account."
        account_id = input("Enter an account number: ")
        if not account_id.isnumeric():
            print("You must input a numeric value.")
            return "Failed to create account."
    except TypeError:
        print("You must input a numeric value.")
        return "Failed to create account."

    user_accounts[account_id] = Account(name, amt)
    return "Successfully created account for %s. " % name


# ---------- MAIN PROGRAM ----------

print("Welcome to my small bank.")

# when exit is has not been chosen, repeat the following
while True:
    action = show_options()

    # what to do with action
    if action == 1:
        # opens account
        print(open_account())

    elif action == 2:
        # deposits
        acc_id = input("Enter an account number to deposit: ")

        # see if user exists
        try:
            user = user_accounts[acc_id]
            # see if amount is numerical or not
            try:
                # access user account and withdraws amount
                user.deposit(int(input("Enter deposit amount: $")) * 100)
            except TypeError:
                print("Deposit amount must be a numeric value. ")
        except KeyError:
            print("This user does not exist.")

    elif action == 3:
        # withdraws
        acc_id = input("Please enter an account number to withdraw: ")

        # see if user exists
        try:
            user = user_accounts[acc_id]
            # see if amount is numerical or not
            try:
                # access user account and withdraws amount
                user.withdraw(int(input("Enter withdrawal amount: $")) * 100)
            except TypeError:
                print("Withdrawal amount must be a numeric value. ")
        except KeyError:
            print("This user does not exist.")

    elif action == 4:
        # shows user balance
        acc_id = input("Please enter an account number to view balance: ")

        # see if user exists
        try:
            # access user account and shows their balance
            user = user_accounts[acc_id]
            user.show_balance()
        except KeyError:
            print("This user does not exist.")

    elif action == 5:
        # shows all transactions
        acc_id = input("Please enter an account number to view transactions: ")

        # see if user exists
        try:
            # access user account and display transactions
            user = user_accounts[acc_id]
            user.show_transactions()
        except KeyError:
            print("This user does not exist.")

    elif action == 6:
        print("\nThank you for using my bank application.")
        exit(0)   # leave program
    else:
        print("\nInvalid Selection. Please try again.")

    print("\n")
