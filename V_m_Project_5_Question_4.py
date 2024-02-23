"""
Question 4: Create a "Vehicle" class in Python with the following properties:

Properties:
"brand" (Brand of the vehicle)
"model" (Model of the vehicle)
"year" (Year of manufacture of the vehicle)

Create a class "Vehicle" and two subclasses derived from it: "SUV" (OffRoadVehicle) and "SportsCar".

The "SUV" class should inherit from the "Vehicle" class and additionally add a "four_wheel_drive" property.
The "SportsCar" class should also inherit from the "Vehicle" class and additionally add a "maximum_speed" property.
Create one instance from each class, specify their properties, and write a program to display these properties."""

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

class SUV(Vehicle):
    def __init__(self, brand, model, year, four_wheel_drive):
        super().__init__(brand, model, year)
        self.four_wheel_drive = four_wheel_drive

class SportsCar(Vehicle):
    def __init__(self, brand, model, year, maximum_speed):
        super().__init__(brand, model, year)
        self.maximum_speed = maximum_speed


suv_instance = SUV("Toyota", "Land Cruiser", 2023, True)
sports_car_instance = SportsCar("Ferrari", "488 GTB", 2022, 330)


print("SUV Details:")
print("Brand:", suv_instance.brand)
print("Model:", suv_instance.model)
print("Year:", suv_instance.year)
print("Four Wheel Drive:", suv_instance.four_wheel_drive)

print("\nSports Car Details:")
print("Brand:", sports_car_instance.brand)
print("Model:", sports_car_instance.model)
print("Year:", sports_car_instance.year)
print("Maximum Speed:", sports_car_instance.maximum_speed, "km/h")
