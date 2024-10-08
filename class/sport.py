class Sport():
    def __init__(self,sport_name,num_of_people): #init初始器
        self.name = sport_name
        self.num = num_of_people
        self.member = True


    def score(self):
        print(f"{self.name} team cheering!")



football = Sport('football',11)#存到 object(football) 里面
basketball = Sport('basketball',5)

print(football.name,football.num,football.member)
print(basketball.name,basketball.num,basketball.member)
football.score()
