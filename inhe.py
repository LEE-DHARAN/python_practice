class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_info(self):
        print(f"This is a {self.brand} vehicle.")

class Car(Vehicle): 
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show_car(self):
        print(f"This is a {self.brand} {self.model} car.")

# Creating a Car
my_car = Car("Toyota", "Corolla")
my_car.show_info()  
my_car.show_car()  


my_vehicle = Vehicle("honda")
my_vehicle.show_info()