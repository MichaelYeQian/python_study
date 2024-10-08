class Dog:
    def __init__(self,dog_name,dog_age):
        #形参是dog_name
        #属性（attribute）是self.name
        self.name = dog_name
        self.age = dog_age
    #funtion in class is method
    def bark(self):
        print(f"{self.name} say worf")

Libai = Dog("Libai" , 3)
print(Libai.name)
Libai.bark()

Sunshangxiang = Dog("Sunshangxiang" , 1)
Sunshangxiang.bark()
print(Sunshangxiang.name)

print("--------------------------------------------------------------------")

class Animal():
#这个class的名字叫做Animal

#'Brown' ' DaHuang
    def __init__(self, animal_color, animal_name,animal_age) :
        self.color = animal_color #'Brown'
        self.name = animal_name #DaHuang
        self.num_of_legs = 4
        self.age = animal_age

    def make_sound(self):
        print(f" {self.name} make sounds, I'm {self.age} years old")

              
#通过Animal这个class， 我们创建了一个叫做dog的Object/instance
dog = Animal( 'Brown','DaHuang', 9)

#如果使用呢？
print(dog.color)
print(dog. name)
print(dog.num_of_legs)
dog.make_sound()

cat = Animal('White', 'lily')
print(cat.color)
print(cat.name)
print(cat.num_of_legs)
cat.make_sound()


