class Customer: #Customer class. General information about the customer is defined.
    def __init__(self, name, surname, id_number, phone):
        self.name = name
        self.surname = surname
        self.id_number = id_number
        self.phone = phone

    def view_info(self): #Function to display customer information.
        return "Customer Name: {}, Customer Surname: {}, ID: {}, Phone: {}".format(self.name, self.surname, self.id_number, self.phone)


class Account(Customer):  # To allow the Account class to inherit from the Customer class, it is written as "Account(Customer)".
    def __init__(self, customer, account_no, balance=0):
        super().__init__(customer.name, customer.surname, customer.id_number, customer.phone)
        ##The __init__ method of the Customer class is called using super().__init__, and customer information is transferred to this class.
        ##By defining the 'customer' argument in the function and assigning the information pulled from the first class to this argument, we avoid errors.
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount): #deposit function adds a certain amount of money to the account.
        self.balance += amount
        print("An amount of {} has been added to your account".format(amount))

    def withdraw(self, amount): #withdraw function withdraws the requested amount of money from the account if there is enough balance.
        if self.balance >= amount:
            self.balance -= amount
            print("An amount of {} has been withdrawn from your account".format(amount))
        else: #If the balance is insufficient, it cannot withdraw and displays a warning message.
            print("Your balance is not sufficient for this transaction.")

    def view_balance(self):
        return "Remaining amount: {}".format(self.balance)


customer = Customer("Beyza", "Dag", "123456789", "938923456")
print(customer.view_info())

account = Account(customer, "123456789", 1000)
account.deposit(1000)
account.withdraw(500)
print(account.view_balance())

customer2 = Customer("Nur", "Dag", "876545673", "437567488")
print(customer2.view_info())

account2 = Account(customer2, "108274626", 500)
account2.deposit(200)
account2.withdraw(5000)
print(account2.view_balance())