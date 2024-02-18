''' * Class and Object *
1. Problem: Create a Car class with attributes like brand and model.Then create an instance of this class.
'''
class Car:
    def __init__(self,brand, model, color, year, price):
     self.brand = brand
     self.model = model
     self.year = year
     self.color = color
     self.price = price
    
my_car = Car("Lamborghini", "Aventador", "Black", 2022, 1000000)
print(my_car.brand)
print(my_car.model)
print(my_car.color)
print(my_car.year)
print(my_car.price)

my_new_car = Car("BMW", "X6", "Black", 2022, 10000000)
print(my_new_car.brand)
print(my_new_car.model)
print(my_new_car.color)
print(my_new_car.year)
print(my_new_car.price)