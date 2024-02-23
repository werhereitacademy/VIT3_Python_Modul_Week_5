"""Question4: Create a "Vehicle" class in Python. Make sure this class has the following properties:

Features:
"brand" (brand of the vehicle)
"model" (Model of vehicle)
"year" (Vehicle's production year)
Create a class "Vehicle" and two derived subclasses, "Off-Road Vehicle" (SUV)
and create "SportsCar" classes.

Let the "Off-Road Vehicle" class inherit from the "Vehicle" class and add an additional "four_wheel drive" feature.
Let the "SportCar" class inherit from the "Vehicle" class and add a "max_speed" property.
Create an instance of each class, determine its properties, and write a program to display these properties."""

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


class OffRoadVehicle(Vehicle):
    def __init__(self, brand, model, year, four_wheel_drive):
        super().__init__(brand, model, year)
        self.four_wheel_drive = four_wheel_drive

    def toString(self):
        print("Your vehicle's specifications:")
        print(f"Brand: {self.brand}\n"
              f"Model: {self.model}\n"
              f"Year: {self.year}\n"
              f"Four-wheel Drive: {self.four_wheel_drive}\n")


class SportsCar(Vehicle):
    def __init__(self, brand, model, year, maximum_speed):
        super().__init__(brand, model, year)
        self.maximum_speed = maximum_speed

    def toString(self):
        print("Your vehicle's specifications:")
        print(f"Brand: {self.brand}\n"
              f"Model: {self.model}\n"
              f"Year: {self.year}\n"
              f"Maximum Speed: {self.maximum_speed}\n")


offroad_vehicle = OffRoadVehicle("Ford", "F150", "2024", "Yes")
sports_car = SportsCar("Honda", "CR-Z", "2014", "200 km/h")

offroad_vehicle.toString()
sports_car.toString()
