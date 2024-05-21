# 1.정수를 저장한 배열 arr에서 가장 작은 수를 제거한 배열을 리턴하는 함수 solution을 완성하시오
def solution(arr):
    arr=[4,3,2,1]
    arr.sort()
    arr.remove(arr[0])
    if arr.remove(min(arr)):
        return arr
    elif len(arr)==1:
        return [-1]

# 2.두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 return하는 solution함수를 완성하시오
def solution1(str1,str2):
    result = ""
    for x in range(len(str1)):
        result+=str1[x]
        result += str2[x]
        return result
print(solution1(str1="aaaa",str2="bbbb"))

# 3. 문자열 mystring이 주어집니다 mystring을 문자x를 기준으로 나누었을때 나눠진 문자열 각각 길이를 순서대로 저장한 배열을 return하는 solution함수를 완성해라
def solution2(mystring):
    a = "oxooxoxxox".split("x")
    b = list(filter(lambda x:len(x)>0,a))
    c = list(map(lambda x:len(x),b))
    print(c)

def solution3(str):

    return list(map(lambda x:len(x),filter(lambda x: len(x)>0,str.split())))

# 4. 최대 5명씩 탑승가능한 놀이기구를 타기위해 줄을 서있는 사람들의 이름이 담긴 문자열 리스트 names가 주어질때
# 앞에서 부터 5명씩 묶는 그룹의 가장 앞에 서있는 사람들의 이름을 담은 리스트를 return하도록 함수를 완성해주세요
arr= ["nami","jace","jack","garen","vex","jin","ivern"]
def solution4(arr):
 return [item for index,item  in enumerate(arr) if index%5==0]



class Animal:
    def __init__(self):
        pass

    def speak(self):
        return "소리 내는 중"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__()
        self.breed = breed

    def speak(self):
        return f"{super().speak()}.... 멍멍"

a = Dog("흰둥이","하얀개")
print(a.speak())

