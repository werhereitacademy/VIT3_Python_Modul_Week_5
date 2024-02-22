class Vehicle:
    def __init__(self, trademark, serial_model, year):
        self.trademark = trademark
        self.serial_model = serial_model
        self.year = year

    def __str__(self):
        self.var = (f"Properties of this Vehicle\n"
                    f"--------------------------\n"
                    f"Trademark        : {self.trademark}\n"
                    f"Series and Model : {self.serial_model}\n"
                    f"Year             : {self.year}\n")
        return self.var


class SUV(Vehicle):
    def __init__(self, trademark, serial_model, year, fwd):
        super().__init__(trademark, serial_model, year)
        self.fwd = fwd

    def __str__(self):
        super().__str__()
        return self.var + f"FWD              : {self.fwd}\n"


class SportsCar(Vehicle):
    def __init__(self, trademark, serial_model, year, max_speed):
        super().__init__(trademark, serial_model, year)
        self.max_speed = max_speed

    def __str__(self):
        super().__str__()
        return self.var + f"FWD              : {self.max_speed} KM\n"


if __name__ == '__main__':
    v1 = Vehicle('BMW', '1 Serie 118i Joy Plus', 215)

    suv1 = SUV('Volvo', 'XC90 2.0 D5 Inscription', 2021, '4X4')

    sport1 = SportsCar('Porsche', 'Macan 2.0', 2020, 223)

    print(v1)
    print(suv1)
    print(sport1)
