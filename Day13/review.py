# 1. 문자열 my_string 이 매개변수로 주어집니다 이 매개변수를 거꾸로 뒤집은 문자열을 return하도록 함수를 완성하시오
def reversedWord(my_string):
    wordList = list(my_string) #[k,o,r,e,a]
    wordList.reverse()
    reversedWord = "".join(wordList)
    return reversedWord



# 2. todo_list에 있는 할 일 중 finshed배열을 통해 아직 끝내지 못한 일들을 찾아 순서대로 배열에 담아 반환하는 함수
# todo_list = ["problemsolving","practiceguitar","swim","studygraph"]
# finished = [true,false,true,false]
# return = ["practiceguitar","studygraph"]

a =  ["problemsolving","practiceguitar","swim","studygraph"]
b = [True,False,True,False]

# num = 0
# doneList = []
# for x in a:
#     if b[num]==True:
#         doneList.append(x)
#     num+=1

# doneList = []
# for index, item in enumerate(a):
#     if b[num]==True:
#         doneList.append(x)


# [item for index, item in enumerate(a) if b[index]==True]

def filterDoneList(todoList,doneList):
    return [item for index, item in enumerate(a) if b[index]==True]


class Animal:
    def __init__(self,name,bread):
        self.name = name
        self.bread = bread

    def eat(self):
            print("냠냠냠")

    def sound(self):
            pass

    def introduce(self):
        print(f"이름:{self.name} 종:{self.bread}")


class Dog(Animal):
    def __init__(self,name,bread):
        self.name = name
        self.bread = bread

    # def eat(self):
    #     print("냠냠냠")

    def sound(self):
        print("멍멍")

class Cat(Animal):
    def __init__(self,name,bread):
        self.name = name
        self.bread = bread

    # def eat(self):
    #     print("냠냠냠")

    def sound(self):
        print("야옹야옹")

a = Dog("킹율","이탈리안하우스")
b = Cat("치즈","치즈냥이")
a.eat()
a.introduce()
a.sound()
b.eat()
b.sound()
b.introduce()

# 퀴즈
# 관리자 편집자 뷰어 라는 각각  사용자가 존재한다
# 모두 접근하기라는 함수를 가지고 있다
# 모두 username이라는 속성도 가지고 있다
# 관리자 유저만들기
# 편집자 편집하기
# 뷰어 조회하기
class User:
    def __init__(self,username):
        self.username = username

    def access(self):
       pass


class manger(User):
    def access(self):
        print("관리자가 접근합니다")

    def usermake(self):
        print("유저만들기")

class edit(User):
    def access(self):
        print("편집자가 접근합니다")

    def editing(self):
        print("편집하기")

class viewer(User):
    def access(self):
        print("뷰어가 접근합니다")

    def view(self):
        print("조회하기")

