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
    def __init__(self, brand, model, year, maximum_speed):
        super().__init__(brand, model, year)
        self.maximum_speed = maximum_speed

# Create instances for Vehicle, OffRoadVehicle, and SportsCar
vehicle1 = Vehicle(brand="Toyota", model="Corolla", year=2022)
offroad_vehicle1 = OffRoadVehicle(brand="Jeep", model="Cherokee", year=2021, four_wheel_drive=True)
sports_car1 = SportsCar(brand="Ferrari", model="488 GTB", year=2020, maximum_speed=330)

# Display the properties
print(f"Vehicle: {vehicle1.brand} {vehicle1.model} ({vehicle1.year})")
print(f"Off-Road Vehicle: {offroad_vehicle1.brand} {offroad_vehicle1.model} ({offroad_vehicle1.year}), Four-Wheel Drive: {offroad_vehicle1.four_wheel_drive}")
print(f"Sports Car: {sports_car1.brand} {sports_car1.model} ({sports_car1.year}), Maximum Speed: {sports_car1.maximum_speed} km/h")
