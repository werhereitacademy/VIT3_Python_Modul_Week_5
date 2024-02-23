class Customer:
    def __init__(self, name, surname, tckn, phone):
        self.name = name
        self.surname = surname
        self.tckn = tckn
        self.phone = phone

    # def __str__(self):
    #     self.var = (f"Customer Information\n"
    #                 f"--------------------\n"
    #                 f"Name    : {self.name}\n"
    #                 f"Surname : {self.surname}\n"
    #                 f"TCKN    : {self.tckn}\n"
    #                 f"Phone   : {self.phone}\n")
    #     return self.var

    def show_info(self):
        return (f"Customer Information\n"
                f"--------------------\n"
                f"Name    : {self.name}\n"
                f"Surname : {self.surname}\n"
                f"TCKN    : {self.tckn}\n"
                f"Phone   : {self.phone}\n")


class Account(Customer):
    def __init__(self, name, surname, tckn, phone, customer, account_number, balance):
        super().__init__(name, surname, tckn, phone)
        self.customer = customer
        self.account_number = account_number
        self.balance = balance

    # def __str__(self):
    #     super().__str__()
    #     return self.var + (f"Customer      : {self.customer}\n"
    #                        f"Account Number: {self.account_number}\n"
    #                        f"Balance       : {self.balance}\n")

    def deposit(self, amount):
        if not amount < 0:
            self.balance += amount
            return self.balance
        else:
            return ('Process: Withdraw process is unsuccessful!\n'
                    'Reason : You can\'t add negative amount!!!')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return ('Process: Withdraw process is unsuccessful!\n'
                    'Reason : There is not enough balance.')

    def show_balance(self):
        return self.balance


if __name__ == '__main__':
    customer1 = Customer('Fatih', 'BUYUKAKCALI', '12345678910', '+906982919295')
    account1 = Account(customer1.name, customer1.surname, customer1.tckn, customer1.phone, customer1, 'NL123456', 1000)

    # Show customer information
    print(account1.show_info())

    # Starting balance
    print(f'Starting balance is: €{account1.show_balance()}\n\n')

    # Deposit money to the account
    print('Deposit €300 to the account:\n'
          '-----------------------------')
    account1.deposit(300)
    print(f'Balance after deposit process: €{account1.show_balance()}\n\n')

    # Try to withdraw more money from the account than the balance.
    print('Try to withdraw more money(€1400) from the account than the balance:\n'
          '-------------------------------------------------------------')
    print(account1.withdraw(1400))
    print('\n\n')

    # Withdraw money from the account
    print('Withdraw €500 from the account:\n'
          '--------------------------------')
    account1.withdraw(500)
    print(f'Balance after withdraw process: €{account1.show_balance()}\n\n')

    # Try to deposit negative amount to the account
    print('Try to deposit negative amount(-€200) to the account:\n'
          '----------------------------------------------')
    print(account1.deposit(-200))
