# db1.py
import sqlite3

#연결객체를 생성(일단 메모리에서 작업)
conn = sqlite3.connect(":memory:")
#커서 객체를 리턴
cur = conn.cursor()
#테이블 생성
cur.execute("CREATE TABLE PhoneBook (name text, phoneNum text);")
#데이터 삽입
cur.execute("INSERT INTO PhoneBook(name,phoneNum) VALUES(?,?);",
             ("Alice", "123-456-7890"))

#파라메터를 입력
name="전우치"
phoneNum="987-654-3210"
cur.execute("INSERT INTO PhoneBook(name,phoneNum) VALUES(?,?);",  
                (name, phoneNum))

#다중의 행을 입력
datalist=(("박문수", "555-666-7777"),
          ("임꺽정", "444-555-6666"))
cur.executemany("INSERT INTO PhoneBook(name,phoneNum) VALUES(?,?);",  
              datalist)
#검색
for row in cur.execute("SELECT * FROM PhoneBook;"):
    print(row)
#연결 종료
conn.close()