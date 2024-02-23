# Class project1
# Creating a Python class called "Rectangle" that represents a rectangle. 
# The Rectangle class must have the following properties and methods: width (an integer) height (an integer)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area (self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
# Create an instance of the Rectangle class with width 5 and height 7
    
rectangle = Rectangle(5,7)

# printing area and perimeter

print("Area of the rectangle:", rectangle.area())
print("Perimeter of the rectangle:", rectangle.perimeter())
    
# Class project2
class School:
    def __init__(self, name, foundation_year):
        self.name = name
        self.foundation_year = foundation_year
        self.students = []
        self.teachers = {}

    def add_new_student(self, student_name, class_name):
        self.students.append((student_name, class_name))

    def add_new_teacher(self, teacher_name, branch):
        self.teachers[teacher_name] = branch

    def view_student_list(self):
        print("List of students enrolled in", self.name)
        for student_name, class_name in self.students:
            print("Student:", student_name, "I Class", class_name)

    def view_teacher_list(self):
        print("List of teachers working at", self.name)
        for teacher_name, branch in self.teachers.items():
            print("Teacher:", teacher_name, "I Branch:", branch)

# Example usage:
school = School("XYZ School", 1990)

# Adding students
school.add_new_student("Alice", "Grade 5")
school.add_new_student("Bob", "Grade 6")

# Adding teachers
school.add_new_teacher("Mr. Smith", "Mathematics")
school.add_new_teacher("Ms. Johnson", "Science")

# Viewing student list
school.view_student_list()

# Viewing teacher list
school.view_teacher_list()

# Class project3
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Shape):
    def __init__(self,width, height):
        super().__init__(width, height)

    def calculate_area(self):
        return self.width * self.height
    

class Square(Shape):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def calculate_area(self):
        return self.width * self.height
    

# Create instances of Rectangle and Square
rectangle = Rectangle(4, 7)
square = Square(6)

# Calculate and print area of Rectangle
rectangle_area = rectangle.calculate_area()
print("Area of Rectangle:", rectangle_area)

# Calculate and print area of Square
square_area = square.calculate_area()
print("Area of Square:", square_area)

# Class Project 4

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

class OffRoadVehicle(Vehicle):
    def __init__(self, brand, model, year, four_wheel_drive):
        super().__init__(brand, model, year)
        self.four_wheel_drive = four_wheel_drive

class SportsCar(Vehicle):
    def __init__(self, brand, model, year, max_speed):
        super().__init__(brand, model, year)
        self.max_speed = max_speed

# Create instances of each class
vehicle = Vehicle("Toyota", "Corolla", 2022)
off_road_vehicle = OffRoadVehicle("Jeep", "Wrangler", 2023, True)
sports_car = SportsCar("Ferrari", "458 Italia", 2024, 320)

# Display properties of each instance
print("Vehicle:")
print("Brand:", vehicle.brand)
print("Model:", vehicle.model)
print("Year:", vehicle.year)

print("\nOff-Road Vehicle:")
print("Brand:", off_road_vehicle.brand)
print("Model:", off_road_vehicle.model)
print("Year:", off_road_vehicle.year)
print("Four-Wheel Drive:", "Yes" if off_road_vehicle.four_wheel_drive else "No")

print("\nSports Car:")
print("Brand:", sports_car.brand)
print("Model:", sports_car.model)
print("Year:", sports_car.year)
print("Max Speed:", sports_car.max_speed, "km/h")

# Class Project 5

class Customer:
    def __init__(self, name, surname, nl_identification, phone):
        self.name = name
        self.surname = surname
        self.nl_identification = nl_identification
        self.phone = phone

    def display_information(self):
        print("Customer Information:")
        print("Name:", self.name)
        print("Surname:", self.surname)
        print("NL ID Number:", self.nl_identification)
        print("Phone Number:", self.phone)


class Account(Customer):
    def __init__(self, name, surname, nl_identification, phone, account_number, initial_balance=0):
        super().__init__(name, surname, nl_identification, phone)
        self.account_number = account_number
        self.balance = initial_balance

    def deposit_money(self, amount):
        self.balance += amount
        print(f"Deposited {amount} Euro. New balance: {self.balance} Euro")

    def money_check(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} Euro. New balance: {self.balance} Euro")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Account Balance: {self.balance} Euro")


# Create a Customer object
customer = Customer("John", "Doe", "1234567890", "555-123-4567")
customer.display_information()

# Create an Account object and add customer information
account = Account("John", "Doe", "1234567890", "555-123-4567", "123456789", initial_balance=1000)

# Perform account operations
account.deposit_money(500)
account.money_check(200)
account.money_check(2000)  # This should display "Insufficient funds."
account.display_balance()
