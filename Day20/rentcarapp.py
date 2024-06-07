import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

print("렌트가 프로그램")
while(True):
    codeNumber = input("1. 자동차 2. 멤버등록 3. 예약하기[업데이트중] 4. 종료 ")
    if codeNumber =="1":
        carNumber = input("차 고유번호 입력")
        carName = input("차 이름 입력")
        carColor = input("차 색상 입력")
        carCompany = input("차 제조사 입력")

        sql = f"""
        INSERT INTO CARS ('car_number','car_name','car_color','car_company')
        VALUES ('{carNumber}','{carName}','{carColor}','{carCompany}')
        """

        cursor.execute(sql)
        connection.commit()
        print("데이터 저장 완료")

    elif codeNumber == "2":
        memberId = int(input("id를 입력하세요"))
        meberName = input("이름을 입력하세요")
        memberAddress = input("주소를 입력하세요")
        memberNumber = input("전화번호를 입력하세요")

        sql = f"""
        INSERT INTO MEMBERS ('id','name','address','number')
        VALUES ('{memberId}','{meberName}','{memberAddress}','{memberNumber}')
         """

        cursor.execute(sql)
        connection.commit()
        print("데이터 저장 완료")