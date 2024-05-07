# 변수들[name,breed,happiness]
class Dog:
    def __init__(self, a,b):
        self.name = a
        self.breed = b
        self.happiness = 0

    def intro(self):
        print(f"{self.name} {self.breed} {self.happiness}")

a = Dog('우유','허스키')
a.intro()
b = Dog('꽃님이','푸들')
b.intro()
c= Dog('백산이','진돗개')
c.intro()



