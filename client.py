class Customer:
    def __init__(self, first_name, last_name, national_id, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.national_id = national_id
        self.phone = phone

    def display_info(self):
        print(f"Customer Information:\nFirst Name: {self.first_name}\nLast Name: {self.last_name}\nNational ID: {self.national_id}\nPhone: {self.phone}")

class Account(Customer):
    def __init__(self, customer, account_number, balance=0):
        super().__init__(customer.first_name, customer.last_name, customer.national_id, customer.phone)
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} TL deposited. New balance: {self.balance} TL")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} TL withdrawn. New balance: {self.balance} TL")
        else:
            print("Insufficient balance. Operation cannot be completed.")

    def display_balance(self):
        print(f"Account Balance: {self.balance} TL")

# Create Customer and Account objects
customer1 = Customer(first_name="Ahmet", last_name="Yılmaz", national_id="12345678901", phone="5551234567")
account1 = Account(customer=customer1, account_number="123456", balance=1000)

# Perform Account operations
account1.deposit(500)
account1.withdraw(200)
account1.display_balance()

# Display Customer information
customer1.display_info()
