#operator_quiz
# 1. 뉴스 기사를 스크랩해온 후 사용자로부터 입력받은 단어가 그 기사 내에 존재하는지 여부를 나타내는 프로그램
# word = input("검색하고 싶은 단어를 입력하시오")
# news = """지난 14일 서울 송파 올림픽공원 KSPO돔에서 열린 2024 LCK 스프링 시즌 결승전에서는
#  젠지가 T1을 3-2로 제압하고 우승컵을 들어올렸다. T1의 '통산 11번째 우승'을 저지한 젠지는
#  사상 첫 '4연속 우승'을 달성하면서 LCK 역사를 새로 썼다."""
# result = word in news
# print(f"검색하신 단어는 뉴스 기사 내에 {result}"  )

# 사용자로 부터 비밀번호 설정을 입력받아 해당 비밀번호가 느낌표를 포함하고 IT라는 문자열을 포함하고 있는지 확인하는 프로그램
password = input("비밀번호를 설정해주세요")
check = "!" in password and "IT" in password
print(f"비밀번호 요구사항이 {check}")