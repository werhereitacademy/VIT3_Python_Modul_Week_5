""" Question1: Create a Python class called "Rectangle" that represents a rectangle. The Rectangle class must have the following properties and methods:
Features:
width (an integer)
height (an integer)
Methods:
area(self): A method that calculates and returns the area of the rectangle.
perimeter(self): A method that calculates and returns the perimeter of a rectangle.
Create an instance of the Rectangle class, set its width to 5 and height to 7, then print its area and perimeter. """
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
       
    def area(self):
        return f'Area = {self.width* self.height}'
    
    def perimeter(self):
        return f'Perimeter = {2 * (self.width + self.height)}'
    
print(Rectangle(5, 7).area())
print(Rectangle(5,7).perimeter())

""" Question2: Create a "School" class in Python. This class should have the following features and functionality:

Features:
"name"
"foundation_year"
"students"
"teachers"
Methods:
add_new_student(self, student_name, class): A method used to add a new student to the school. It takes the student's name and class and adds it to the "students" list.
add new_teacher(self, teacher_name, branch): A method used to add a new teacher to the school. It takes the teacher's name and major and adds it to the "teachers" dictionary.
view_student_list(self): A method used to display the list of students enrolled in the school. List student names and classes.
view_teacher_list(self): A method used to display the list of teachers working at the school. List teacher names and majors. """
class School:
    def __init__(self, school_name, founding_year):
        self.school_name = school_name
        self.founding_year = founding_year
        self.teachers = {}
        self.students = []

    def new_students(self,student_name,student_class):
        self.students.append((student_name,student_class))
        print(f"{student_name} Student System Added Successfully") 
     
    def new_teachers(self,teacher_name,teacher_branch):
        self.teachers[teacher_name] = teacher_branch
        print(f"{teacher_name} Teacher System Added Successfully") 
      
    def teachers_list(self):
        count = 1
        print(f'{10*"*"}LIST OF TEACHER{10*"*"}')
        for teacher,teacher_branch in self.teachers.items():
            print(f'{count}.{teacher},{teacher_branch}')
        count+=1

    def student_list(self):
        count = 1
        print(f'{10*"*"}LIST OF STUDENT{10*"*"}')
        for student, student_class in self.students:
            print( f'{count}.{student},{student_class}')
        count+=1

Wessem_Basis_School = School("Wessem", 1950) 

Wessem_Basis_School.new_students("Selcuk Kagan",5)
Wessem_Basis_School.new_students("Alperen",1)

Wessem_Basis_School.new_teachers("Roy Timmerman","Wiskunde")
Wessem_Basis_School.new_teachers("Margriet Wilders","Natuurkunde")

Wessem_Basis_School.student_list()
Wessem_Basis_School.teachers_list()
       
      """ Question3: Create a "Shape" class. Under this class, create two subclasses, the "Rectangle" and "Square" classes.
Let the "shape" class have two properties: "width" and "height."
Let the "Rectangle" class inherit from the "Shape" class and add an additional "calculate_area()" method.
Let the "Square" class inherit from the "Shape" class and calculate the area of the square using the same "area_calculate()" method.
Create a "Rectangle" and a "Square" instance, determine the width and height of each, and calculate the area of each and print the results. """
class Shape:
    def __init__(self,width, height):
        self.width = width
        self.height = height
        
class Rectangle(Shape):
    def rectangele_area(self):
        return self.height * self.width
  
class Square(Shape):
    def __init__(self, width):
        super().__init__(width, height = width)
    def square_area(self):
        return self.width**2

rectangle = Rectangle(5,8)
square = Square(5)


print(f'Rectangle Area = {rectangle.rectangele_area()}')
print(f'Square Area = {square.square_area()}')


""" Question4: Create a "Vehicle" class in Python. Make sure this class has the following properties:

Features:
"brand" (brand of the vehicle)
"model" (Model of vehicle)
"year" (Vehicle's production year)
Create a "Vehicle" class and create two derived subclasses, "Off-Road Vehicle" (SUV) and "SportsCar" classes.

Let the "All-Terrain Vehicle" class inherit from the "Vehicle" class and add an additional "four_wheel drive" feature.
Let the "SportCar" class inherit from the "Vehicle" class and add a "max_speed" property.
Create an instance of each class, determine its properties, and write a program to display these properties. """
class Car:
    def __init__(self, car_brand, car_model, production_year):
        self.car_brand = car_brand
        self.car_model =car_model
        self.production_year = production_year
class offroad_car(Car):
    def __init__(self, car_brand, car_model, production_year,four_wheel):
        super().__init__(car_brand, car_model, production_year)
        self.four_wheel = four_wheel
    
    
class sports_car(Car):
    def __init__(self, car_brand, car_model, production_year,max_speed):
        super().__init__(car_brand, car_model, production_year)
        self.max_speed = max_speed
    
car1 = offroad_car("Jeep Wrangler", "Rubicon", 2024,"four wheel")
car2 = sports_car("Bugatti","Divo", 2024, 380)
car3 = Car("BMW", "i7 M70 xDrive Sedan",2024)

print(f'{"*"*5} OFF-ROAD CARS {"*"*5}')
print(f'Car Brand:{car1.car_brand} \nCar Model:{car1.car_model} \nProduction Year:{car1.production_year} \nFour Wheel:{car1.four_wheel}')

print(f'{"*"*5} SPORT CARS {"*"*5}')
print(f'Car Brand:{car1.car_brand} \nCar Model:{car1.car_model} \nProduction Year:{car1.production_year} \nMax Speed:{car1.four_wheel}')

print(f'{"*"*5} SEDAN CARS {"*"*5}')
print(f'Car Brand:{car3.car_brand} \nCar Model:{car3.car_model} \nProduction Year:{car3.production_year}')

""" Question5: Create a "Customer" class and an "Account" class. Let the "Account" class inherit
 from the "Customer" class and represent a customer's bank account information.
Customer Class Features:
"name" (customer name)
"surname" (customer surname)
"tc_identification" (customer TR ID number)
"phone" (customer phone number)
Account Class Features:
"customer" (a Customer object)
"account_number" (account number)
"balance" (account balance)
Customer Class Method:
"display_information()": Displays the customer's name, surname, TR ID number and telephone number.
Account Class Methods:
"deposit_money(self, amount)": A method that deposits a certain amount of money into the account.
"money_check(self, amount)": A method that withdraws a certain amount of money from the account. 
However, if there is not enough balance in the account, the transaction should not occur and a message should be displayed.
"display_balance()": A method that displays the account balance.
Create these two classes, then create a Customer object and an Account object, add the customer information to the Account object, 
and perform account operations and view the results. """
class Customer:
    def __init__(self,name,surname,Id,phone):
        self.name = name
        self.surname = surname
        self.Id = Id
        self.phone = phone
        
    def customer_info(self):
        print(f'{"*"*5} Customer Information {"*"*5}')
        print(f'Name:{self.name}\nSurname:{self.surname}\nId:{self.Id}\nPhone:{self.phone}\nAccount Number:{account.account_number}\nBalance;{account.balance}')
                 
    
class costomer_account(Customer):
    def __init__(self, name, surname, Id, phone, account_number, balance):
        super().__init__(name, surname, Id, phone)
        self.account_number = account_number
        self.balance = balance

    def money_deposit(self,deposit):
        account.balance += deposit
        print(f'{deposit} has been deposited into your account number {self.account_number}.\nYour new balance:{account.balance}')
          
    def money_withdraw(self,withdraw):
        if account.balance >= withdraw:
            account.balance -= withdraw
            print(f'{withdraw} was withdrawn to your account number {self.account_number}.\nYour remaining balance:{account.balance}')
        else:
            print("The operation cannot be performed.Insufficient Balance.")   

    def balance_info(self):
        print(account.balance)
         

customer = Customer("Ali", "Veli", 78965432112, 5358976532)
account = costomer_account(customer.name, customer.surname, customer.Id, customer.phone, 23012024, 3000)

account.customer_info()
account.money_withdraw(3000)
account.money_deposit(5000)





  
