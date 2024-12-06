import random
class Car:

    color = "color"
    car_brand = "brand"

    def go(self):
        print("Go")

    def stop(self):
        print("Stop")

    def info(self):
        print("цвет машины: ", self.color, ", марка машины: ", self.car_brand)

bmw = Car()
bmw.info()
bmw.color = "синяя"
bmw.car_brand = 'Бмв'

bmw.info()

#a = input()

#result = eval(a)

#print(result)