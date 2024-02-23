"""Question5: Create a "Customer" class and an "Account" class. Let the "Account" class inherit from the "Customer" class and represent a customer's bank account information.
Customer Class Features:
"name" (customer name)
"surname" (customer surname)
"tc_identification" (customer TR ID number)
"phone_number" (customer phone number)
Account Class Features:
"customer" (a Customer object)
"account_number" (account number)
"balance" (account balance)
Customer Class Method:
"display_information()": Displays the customer's name, surname, TR ID number and telephone number.
Account Class Methods:
"deposit_money(self, amount)": A method that deposits a certain amount of money into the account.
"withdraw_money(self, amount)": A method that withdraws a certain amount of money from the account.
However, if there is not enough balance in the account, the transaction should not occur and a message should be displayed.
"display_balance()": A method that displays the account balance.
Create these two classes, then create a Customer object and an Account object,
Add customer information to the Account object and perform account operations and view the results."""


class Customer: #Customer class. General information about the customer is defined.
    def __init__(self, name, surname, id_number, phone):
        self.name = name
        self.surname = surname
        self.id_number = id_number
        self.phone = phone

    def display_info(self): #Function to display customer information.
        return "Customer Name: {}, Customer Surname: {}, ID: {}, Phone: {}".format(self.name, self.surname, self.id_number, self.phone)


class Account(Customer):  # In order for the Account class to be able to inherit from the Customer class, it is written as "Account(Customer)".
    def __init__(self, customer, account_no, balance=0):
        super().__init__(customer.name, customer.surname, customer.id_number, customer.phone)
        #The __init__ method of the Customer class is called using super().__init__, and the customer information is passed to this class.
        #We define the 'customer' argument to pass the information taken from the first class to this argument. Otherwise, it throws an error.
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount): #The deposit function adds a certain amount of money to the account.
        self.balance += amount
        print("A total of {} has been deposited to your account".format(amount))

    def withdraw(self, amount): #The withdraw function withdraws the requested amount of money from the account if there is sufficient balance.
        if self.balance >= amount:
            self.balance -= amount
            print("A withdrawal of {} has been made from your account".format(amount))
        else: #If the balance is insufficient, it cannot be withdrawn and prints a warning message.
            print("You do not have sufficient balance for this transaction.")

    def display_balance(self):
        return "Remaining balance: {}".format(self.balance)


customer = Customer("Beyza", "Dag", "123456789", "938923456")
print(customer.display_info())

account = Account(customer, "123456789", 1000)
account.deposit(1000)
account.withdraw(500)
print(account.display_balance())

customer2 = Customer("Nur", "Dag", "876545673", "437567488")
print(customer2.display_info())

account2 = Account(customer2, "108274626", 500)
account2.deposit(200)
account2.withdraw(5000)
print(account2.display_balance())
