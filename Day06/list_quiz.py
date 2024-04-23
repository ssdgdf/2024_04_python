# 1.유저에게 다섯개의 정수를 입력받고 리스트화 한 다음 각각 요소를 3배로 만든다음 출력하기
# num1 = int(input("숫자를 입력하시오 : "))
# num2 = int(input("숫자를 입력하시오 : "))
# num3 = int(input("숫자를 입력하시오 : "))
# num4 = int(input("숫자를 입력하시오 : "))
# num5 = int(input("숫자를 입력하시오 : "))
# number = ([num1, num2, num3, num4, num5])
# print(number)
# print([number[0]*3 , number[1]*3 , number[2]*3 , number[3]*3  , number[4]*3] )

numberList = []
for x in range(5):
    num = int(input("숫자를 입력하시오 : "))
    numberList.append(num)
print(numberList)

newNumberList = []
for x in numberList:
   newNumberList.append(x*3)
   print(newNumberList)

# 2. 유저에게 서로다른 다섯개의 정수를 입력받고 리스트화 한다음에 가장큰수를 뽑아내는 프로그램
numberList = []
for x in range(5):
    num = int(input("숫자를 입력하시오 : "))
    numberList.append(num)
numberList.sort() # 정렬하고  ex)1,3,5,7,8,
numberList.reverse() # 뒤집어서 ex)8,7,5,3,1,
print(numberList[0]) # 8

