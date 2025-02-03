
class Transport:
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def display_info(self):
        print(f"Transport Information: Brand: {self.__brand}, Model: {self.__model}, Year: {self.__year}")

class Car(Transport):
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)
        self.__fuel_type = fuel_type

    def get_fuel_type(self):
        return self.__fuel_type

    def set_fuel_type(self, fuel_type):
        self.__fuel_type = fuel_type

    def display_info(self):
        super().display_info()
        print(f"Fuel Type: {self.__fuel_type}")

class Truck(Transport):
    def __init__(self, brand, model, year, max_load):
        super().__init__(brand, model, year)
        self.__max_load = max_load

    def get_max_load(self):
        return self.__max_load

    def set_max_load(self, max_load):
        self.__max_load = max_load

    def display_info(self):
        super().display_info()
        print(f"Max Load: {self.__max_load}")

car = Car("Toyota", "Corolla", 2020, "Gasoline")
truck = Truck("Volvo", "FH16", 2018, 25000)

car.display_info()
print()