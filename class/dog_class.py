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



