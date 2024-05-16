class Bird:
    def __init__(self,name,bread):
        self.name = name
        self.bread = bread

    def lay(self):
        print(f"{self.name}이 알을 낳습니다")

class flyable:
    def fly(self):
        print(f"{self.name}가(이) 날아오릅니다")

class Eagle(Bird,flyable):
    def crawl(self):
        print(f"{self.name}이 사냥합니다")

class penguin(Bird):
    def swiming(self):
        print(f"{self.name}이 수영을 합니다")