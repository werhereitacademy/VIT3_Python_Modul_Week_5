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

import random

class Customer:
    def __init__(self, name, surname, id_number, phone_number):
        self.name = name
        self.surname = surname
        self.id_number = id_number
        self.phone_number = phone_number

class Account(Customer):
    def __init__(self, name, surname, id_number, phone_number):
        super().__init__(name, surname, id_number, phone_number)
        self.customers = []
        self.account_number = self.create_account_number()
        self.balance = 0

    def create_account_number(self):
        # Generate a random 10-digit account number
        return ''.join([str(random.randint(0, 9)) for _ in range(10)])

    def add_new_customer(self):
        new_customer = {
            "name": self.name,
            "surname": self.surname,
            "id_number": self.id_number,
            "phone_number": self.phone_number,
            "account_number": self.account_number,
            "balance_amount": self.balance
        }
        self.customers.append(new_customer)

    def view_information(self, searched_name):
        for customer_info in self.customers:
            if customer_info["name"] == searched_name:
                print(customer_info)
                return
        print("No customer found with this name.")

    def view_balance(self):
        account_no = input("Please enter the account number you want to display balance:")
        for customer_info in self.customers:
            if customer_info["account_number"] == account_no:
                print(f"Balance: {customer_info['balance_amount']} TL")
                return
        print("No account number found.")

    def deposit(self, amount):
        account_no = input("Please enter the account number you want to deposit money into:")
        for customer_info in self.customers:
            if customer_info["account_number"] == account_no:
                customer_info["balance_amount"] += amount
                print(f"{amount} TL deposited. New balance: {customer_info['balance_amount']} TL")
                return
        print("No account number found.")

    def withdraw(self, amount):
        account_no = input("Please enter the account number you want to withdraw money from:")
        for customer_info in self.customers:
            if customer_info["account_number"] == account_no:
                if amount <= customer_info["balance_amount"]:
                    customer_info["balance_amount"] -= amount
                    print(f"{amount} TL withdrawn. New balance: {customer_info['balance_amount']} TL")
                else:
                    print("Insufficient balance!")
                return
        print("No account number found.")

name = "Furkan"
surname = "Altay"
id_number = "215786785"
phone_number = "689754567"

customer = Account(name, surname, id_number, phone_number)
customer.add_new_customer()
customer.view_information("Furkan")
#It will show you customer information. Enter the account number given to you to make a money transaction.
customer.deposit(800)
customer.deposit(300)
customer.view_balance()
customer.withdraw(500)

