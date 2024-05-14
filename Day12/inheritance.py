class Animal:
    def eating(self):
        print("냠냠쩝쩝")

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("멍멍")

class Cat(Animal):
    def speak(self):
        print("야옹")


a = Dog()
a.speak()
a.eating()

b = Cat()
b.speak()
b.eating()

