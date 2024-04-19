# 1.1~100까지 총합을 나타내는 프로그램
# total=0
# for i in range(1,101):
#     total=i+total
#     print(total)

#유저에게 과일을 입력받고
#모음을 제거한 단어로 나타내기 apple -> ppl  ,  banana->bnn ,
# fruit = input("과일을 입력하시오")
# for x in "fruit":
#  if  x!='a' and x != 'e' and x != 'i' and x != 'o' and x != 'u' in fruit:
#      print(x)

fruit = input("과일을 입력하시오")
word=""
for x in fruit:
    if not x in 'aeiou':
        word += x
    print(word)

