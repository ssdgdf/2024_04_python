# 1.현재 원화를 입력 하면 달러로 바꿔 주는 프로그램을 작성 하시오
money = input("현재 원화를 입력 하시오")
result = int(money)/1400
print(f"현재 {result}달러가 있습니다")

# 2.사용자 로 부터 두개의 숫자를 입력 받아 두 숫자에 대한 합 차 곱 몫 나머지 제곱을 계산 하는 프로그램을 작성 하시오
num1 = input("첫번쨰 숫자를 입력 하시오")
num2 = input("두번째 숫자를 입력 하시오")
plus = int(num1)+int(num2)
minus = int(num1)-int(num2)
div = int(num1)//int(num2)
ex = int(num1)%int(num2)
asd = int(num1)*int(num2)
asd2 = int(num1)**int(num2)
print(f"합 :{plus} 차 :{minus} 곱 :{asd} 몫 :{div} 나머지:{ex} 제곱 :{asd2}")
#print(f"합 :{num1+num2} 차 : {num1-num2} ..........

# 3.사용자로 부터 원의 반지름을 입력 받아 그원의 둘레와 넓이를 계산 하는 프로그램을 만들어 보시오
cir = input("원의 반지름 을 입력 하시오")
pie = 3.14
result1 = int(cir)*2*pie
result2 = int(cir)**2*pie
print(f"원의 둘레는 {result1} 이고 넓이는 {result2} 이다")