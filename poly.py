from abc import ABC, abstractmethod
from functools import singledispatch
 
class Toy(ABC):  # Interface (abstract class)
    @abstractmethod
    def make_sound(self):
        pass  # "I don't know how yet!"
 
    @abstractmethod
    def light_up(self):
        pass  # "I don't know how yet!"
 
class RobotToy(Toy):  # A toy that follows the interface
    @singledispatch
    def make_sound(self):         
        print( "Beep Beep")  # Default return type: string

    @make_sound.register
    def _(self, word:str):     
        print(f"Robot says: {word}")  # When input is a string
 
    def light_up(self):
        print("Flashing Light")
 
class BarbieToy(Toy):  # A toy that follows the interface
    def make_sound(self):
        print("Smile")
   
    def light_up(self):
        print("No lights")
 
 
obj = RobotToy()
obj.make_sound("murali")



# 🎭 Parent Class
class Animal:
    def make_sound(self):
        return "Some generic sound"

# 🐶 Child Class
class Dog(Animal):
    def make_sound(self):  # Overriding method
        return "Woof! 🐶"

# 🐱 Child Class
class Cat(Animal):
    def make_sound(self):  # Overriding method
        return "Meow! 🐱"

# ✅ Polymorphism in Action
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    print(animal.make_sound())



