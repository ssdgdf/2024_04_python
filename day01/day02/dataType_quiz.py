# 유저에게
#첫번째 정수 입력
# 두번 쨰 정수 입력
# 받은 후 두수의 합을 출력하는 프로그램
num1 = input("첫번째 정수를 입력하시오")
num2 = input("두번째 정수를 입력하시오")
result = int(num1)+int(num2)
print(f"결과는{result}이다")

# 사용자의 나이를 입력받아 그사람이 태어난 연도를 계산하여 출력하는 프로그램
age = input("당신의 나이를 입력하시오")
result1 = 2024-int(age)+1
print(f"당신은{age}살이고 {result1}년에 태어났군요")

# 한 변의 길이를 입력받아 정사각형의 넓이를 구하는 프로그램
cm = input("한변의 길이를 입력하시오")
square = int(cm)*int(cm)
print(f"한변의 길이가 {cm}이면 정사각형의 넓이는 {square}이군요")
