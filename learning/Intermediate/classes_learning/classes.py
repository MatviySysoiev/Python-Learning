class Car:
    def move(self):
        print("The car is moving")

    def stop(self):
        print("The car has stopped")


my_car = Car()

print(my_car)  # <__main__.Car object at 0x000002413C1D86E0>
print(type(my_car))  # <class '__main__.Car'>

print(isinstance(my_car, Car))  # True

print(dir(my_car))
# it is empty so it means all attributes were taken from class Car
print(my_car.__dict__)

my_car.move()  # The car is moving
my_car.stop()  # The car has stopped

my_second_car = Car()

print(my_car == my_second_car)  # False
Car.move(my_car)  # The car is moving
