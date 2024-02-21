# # Question 1
"""
Create a Python class named "Rectangle" representing a rectangle. The Rectangle class should have the following properties and methods:
##### Properties:
- width (an integer)
- height (an integer)
##### Methods:
- area(self): A method that calculates and returns the area of the rectangle.
- perimeter(self): A method that calculates and returns the perimeter of the rectangle.
Create an instance of the Rectangle class, set its width to 5 and height to 7, then print its area and perimeter.
"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rectangle = Rectangle(5, 7)

print(f"The Rectangle with dimensions {rectangle.width} cm and {rectangle.height} cm has an area of: {rectangle.area()} cm²")
print(f"The Rectangle with dimensions {rectangle.width} cm and {rectangle.height} cm has a perimeter of: {rectangle.perimeter()} cm")

########################
# # Question 2
"""
Create a class named "School" in Python. This class should have the following properties and functionalities:
##### Properties:
- "name"
- "establishment_year"
- "students"
- "teachers"
##### Methods:
- add_new_student(self, student_name, grade): A method used to add a new student to the school. It takes the student's name and grade, and adds them to the "students" list.
- add_new_teacher(self, teacher_name, subject): A method used to add a new teacher to the school. It takes the teacher's name and subject, and adds them to the "teachers" dictionary.
- display_student_list(self): A method used to display the list of enrolled students in the school. List the student names and their grades.
- display_teacher_list(self): A method used to display the list of teachers working at the school. List the teacher names and their subjects.
"""
import random

class School:
    def __init__(self, name, establishment_year):
        self.name = name
        self.establishment_year = establishment_year
        self.students = []
        self.teachers = {}

    def add_new_student(self, student_name, grade):
        self.students.append((student_name, grade))

    def add_new_teacher(self, teacher_name, subject):
        self.teachers[teacher_name] = subject

    def display_student_list(self):
        print("List of enrolled students:")
        for student in self.students:
            print(f"{student[0]} - Grade: {student[1]}")

    def display_teacher_list(self):
        print("List of teachers working at the school:")
        for teacher, subject in self.teachers.items():
            print(f"{teacher} - Subject: {subject}")

# Name List
names = ["John", "Emily", "Michael", "Jessica", "David", "Sarah"]

# List of Subjects
subjects = ["Mathematics", "Biology", "History", "English", "Physics"]

# Create an instance of the School class
school = School("Sample School", 1990)

# Add random students
for _ in range(5):
    student_name = random.choice(names)
    grade = random.randint(9, 12)
    school.add_new_student(student_name, f"{grade}th Grade")

# Add random teachers
for _ in range(3):
    teacher_name ="Teacher " + random.choice(names)
    subject = random.choice(subjects)
    school.add_new_teacher(teacher_name, subject)

# Display student and teacher lists
school.display_student_list()
print("")
school.display_teacher_list()

########################
# # Question 3
"""
Create a class named "Shape" in Python. Under this class, create two subclasses named "Rectangle" and "Square".

- The "Shape" class should have two attributes: "width" and "height."
- The "Rectangle" class should inherit from the "Shape" class and also have a method named "calculate_area()".
- The "Square" class should also inherit from the "Shape" class and calculate the area of the square using the same "calculate_area()" method.
- Create instances of a "Rectangle" and a "Square", specify their widths and heights, and print their areas.
"""
import random

class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Shape):
    def area_calculate(self):
        return self.width * self.height

class Square(Shape):
    def area_calculate(self):
        return self.width ** 2

# Example of a Rectangle
rectangle_width = random.randint(3, 10)
rectangle_height = random.randint(3, 10)
rectangle = Rectangle(rectangle_width, rectangle_height)
print(f"The Rectangle has a width of {rectangle.width} cm and a height of {rectangle.height} cm. Its area is: {rectangle.area_calculate()} cm²")

# Example of a Square
square_side = random.randint(3, 10)
square = Square(square_side, square_side)
print(f"The Square has a side length of {square.width} cm. Its area is: {square.area_calculate()} cm²")

########################
# # Question 4
"""
Create a Python class named "Vehicle". This class should have the following properties:

##### Properties:
- "brand" (The brand of the vehicle)
- "model" (The model of the vehicle)
- "year" (The year the vehicle was manufactured)

Create a "Vehicle" class and two subclasses derived from it, named "SUV" and "SportsCar".

- The "SUV" class should inherit from the "Vehicle" class and additionally have a property named "four_wheel_drive".
- The "SportsCar" class should also inherit from the "Vehicle" class and additionally have a property named "maximum_speed".

Create an instance of each class, set their properties, and write a program to display these properties.
"""
class Vehicle():
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

class Suv(Vehicle):
  def __init__(self, brand, model, year, four_wheel_drive):
    super().__init__(brand, model, year)
    self.four_wheel_drive = four_wheel_drive

class SportsCar(Vehicle):
  def __init__(self, brand, model, year, max_speed):
    super().__init__(brand, model, year)
    self.max_speed = max_speed


vehicle = Vehicle("Toyota", "Auris", 2011)
print(f"\nVehicle Attributes \nBrand: {vehicle.brand} \nModel: {vehicle.model} \nYear: {vehicle.year} \n")

suv = Suv("Jeep", "Cherokee", 2019, True)
print(f"SUV Attributes \nBrand: {suv.brand} \nModel: {suv.model} \nYear: {suv.year} \nFour Wheel Drive: {suv.four_wheel_drive} \n")

sports_car = SportsCar("Ferrari", "488 GTB", 2020, 330)
print(f"Sports Car Attributes \nBrand: {sports_car.brand} \nModel: {sports_car.model} \nYear: {sports_car.year} \nMax Speed: {sports_car.max_speed} km/h \n")

########################
# # Question 5
"""
Create a class named "Customer" and a class named "Account" in Python. The "Account" class should inherit from the "Customer" class and represent a customer's bank account information.

##### Customer Class Properties:
- "first_name" (customer's first name)
- "last_name" (customer's last name)
- "national_id" (customer's national ID number)
- "phone" (customer's phone number)

##### Account Class Properties:
- "customer" (a Customer object)
- "account_number" (account number)
- "balance" (account balance)

##### Customer Class Method:
- "display_info()": Displays the customer's first name, last name, national ID, and phone number.
  
##### Account Class Methods:
- "deposit(self, amount)": A method used to deposit a certain amount of money into the account.
- "withdraw(self, amount)": A method used to withdraw a certain amount of money from the account. However, if there is insufficient balance in the account, the transaction should not go through and a message should be displayed.
- "display_balance()": A method used to display the account balance.
  
Create these two classes, then create an instance of a Customer object and an Account object, add the customer's information to the Account object, perform account transactions, and display the results.
"""
import random

class Customer:
    def __init__(self, first_name, last_name, national_id, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.national_id = national_id
        self.phone = phone

    def display_info(self):
        print(f"Customer First Name: {self.first_name}")
        print(f"Customer Last Name: {self.last_name}")
        print(f"National ID: {self.national_id}")
        print(f"Phone Number: {self.phone}")


class Account(Customer):
    def __init__(self, customer, account_number, balance):
        super().__init__(customer.first_name, customer.last_name, customer.national_id, customer.phone)
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} Euro deposited into the account. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient balance! Current balance: ${self.balance}")
        else:
            self.balance -= amount
            print(f"{amount} Euro withdrawn from the account. New balance: ${self.balance}")

    def display_balance(self):
        print(f"Account Balance: ${self.balance}")


# Example Usage
customer1 = Customer("John", "Doe", "123-45-6789", "+1-555-123-4567")
account1 = Account(customer1, "123456789", 1000)

account1.display_info()

# Random deposit and withdrawal
deposited_amount = random.randint(1, 500)
withdrawn_amount = random.randint(1, 1000)

account1.deposit(deposited_amount)
account1.withdraw(withdrawn_amount)

account1.display_balance()
