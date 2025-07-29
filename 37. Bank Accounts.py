class BankAccount:

    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.balance = balance


    # add money into the account and return the new balance
    def deposit(self, add):
        self.balance += add
        return self.balance

    # take money out by subtracting from balance and returning the withdrawn amount
    def withdraw(self, withdrawal):
        self.balance -= withdrawal
        return self.balance

    # print the current value of balance
    def display_balance(self):
        print(self.balance)


kevin = BankAccount('Kevin', 'Doe', 3100567, 'Savings', 4458, 100)

kevin.deposit(96)
kevin.display_balance()

kevin.withdraw(25)
kevin.display_balance()


