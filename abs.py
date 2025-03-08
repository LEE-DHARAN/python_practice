from abc import ABC, abstractmethod

class Animal(ABC): 
    @abstractmethod
    def make_sound(self):  
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof! 🐶"

class Cat(Animal):
    def make_sound(self):
        return "Meow! 🐱"

#  Creating Objects
dog = Dog()
print(dog.make_sound()) 

cat = Cat()
print(cat.make_sound())  


from abc import ABC, abstractmethod 

# Abstract Parent Class
class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def show_info(self):  
        pass  

# Child Class
class Car(Vehicle):  
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    # Implementing the abstract method
    def show_info(self):
        print(f"This is a {self.brand} {self.model} car.")

    def show_car(self):
        print(f"This is a {self.brand} {self.model} car.")
    

# Creating a Car Object
my_car = Car("Toyota", "Corolla")
my_car.show_info()  
my_car.show_car()


