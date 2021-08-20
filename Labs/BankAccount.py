from datetime import datetime


class Account:
    """
    Bank Account class that stores balance in cents to avoid
    floating point errors
    """

    def __init__(self, name, initial_balance: int = 0):
        """
        Constructor of Account class, initializes object with name
        and initial_balance values
        :param name: name of account owner
        :param initial_balance: balance the owner starts with
                                (defaults to 0)
        """
        self.name = name
        self.__balance = initial_balance
        self.__transactions = []
        print("Created account for {}".format(self.name))

    def deposit(self, amount: int):
        """
        Deposits a positive amount into balance, throws exception
        otherwise
        :param amount: amount to be deposited
        :return: the final balance amount
        """
        if amount > 0:
            self.__balance += amount
            print("Deposited ${0:.2f} into {1}'s account.".format(amount/100, self.name))

            # add to transaction list
            self.__transactions.append(("Deposit", amount/100, datetime.now()))
        else:
            # replace with exception
            try:
                raise NegativeAmount("Deposit amount must be positive.")
            except NegativeAmount as error:
                print(error)

        return self.__balance/100

    def withdraw(self, amount: int):
        """
        Deposits a positive amount into balance, throws exception
        otherwise
        :param amount: amount to be deposited
        :return: the final balance amount
        """
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrew ${0:.2f} from {1}'s account.".format(amount/100, self.name))

            # add to transaction list
            self.__transactions.append(("Withdraw", amount/100, datetime.now()))
        elif amount > self.__balance:
            # replace with exception
            try:
                raise NegativeBalance("Withdrawal amount must be less than the balance amount: ${:.2f}"
                                      .format(self.__balance))
            except NegativeBalance as error:
                print(error)
        else:
            try:
                raise NegativeAmount("Withdrawal amount must be positive.")
            except NegativeAmount as error:
                print(error)

        return self.__balance/100

    def show_balance(self):
        print("Balance: ${:.2f}".format(self.__balance/100))

    def show_transactions(self):
        if len(self.__transactions) == 0:
            print("No transaction to show.")
        else:
            print("{:20}{:12}{:50}".format("Transaction Type", "Amount", "Date/Time"))
            for transaction in self.__transactions:
                print("{:20}${:<11.2f}{:50}".format(transaction[0], transaction[1],
                                                    transaction[2].strftime("%d %B %Y %H:%M:%S")))


# exceptions needed for Account to work
class NegativeAmount(Exception):
    def __init__(self, value):
        """
        Constructor for when amount withdrawn/deposited is negative
        :param value: message to be print
        """
        self.value = value

    def __str__(self):
        """
        To string of exception
        :return: message to be print
        """
        return self.value


class NegativeBalance(Exception):
    def __init__(self, value):
        """
        Constructor for when amount withdrawn exceed balance
        :param value: message to be print
        """
        self.value = value

    def __str__(self):
        """
        To string of exception
        :return: message to be print
        """
        return self.value


"""
testing class 

if __name__ == "__main__":
    mickey = Account("Mickey", 1010)
    mickey.show_balance()

    mickey.deposit(10)
    mickey.deposit(10)

    mickey.show_balance()

    try:
        mickey.withdraw("hello")
    except TypeError as e:
        print("Must be number!")


    mickey.withdraw(-20)

    mickey.show_balance()

    mickey.show_transactions()
"""
