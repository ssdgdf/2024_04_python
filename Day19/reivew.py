# 1. 전화번호가 문자열 phone_number로 주어졌을때 전화번호 뒤 4자리를 제외한 숫자를 전부 *로 가린 문자열을 리턴하는 함수 solution
def solution(target):
    target = "01033334444"
    answer = ""
    for index,item in enumerate(list(target)):
        if len(target)- index<=4:
            print(item)
        else:
            answer +="*"
    return answer

# 2. 문자열 number가 매개변수로 주어질때 number를 정수로 바꿔 리턴하도록 solution함수를 만드시오
def solution1(numberstr):
    numberDict = {
        "one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"zero":0,
    }

    numberstr = "onetwothreefourfivesixseveneightnine"

    for x in list(numberDict.keys()):
        if x in numberstr:
            numberstr = numberstr.replace(x,str(numberDict[x]))
    return numberstr

