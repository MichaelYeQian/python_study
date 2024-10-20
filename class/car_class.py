class Car:
    def __init__(self,speed):
        self.speed = speed
    def get_speed(self):
        return self.speed
    def add_speed(self,add):
        self.speed += add
    def brake(self,decrease):
        self.speed -= decrease

my_car = Car(30)
print(f"inital speed {my_car.get_speed()}")
my_car.add_speed(5)
print(f"after add speed {my_car.get_speed()}")

#my_car.brake(5)
