# db1.py
import sqlite3

#연결객체를 생성:파일에 영구적으로 저장(sample.db)
#raw string 사용
conn = sqlite3.connect(r"C:\work\sample.db")
#커서 객체를 리턴
cur = conn.cursor()
#테이블 생성
#테이블이 이미 존재하면 무시    
cur.execute("CREATE TABLE if not exists PhoneBook (name text, phoneNum text);")
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
          ("이순신", "444-555-6666"))
cur.executemany("INSERT INTO PhoneBook(name,phoneNum) VALUES(?,?);",  
              datalist)
#검색작업
cur.execute("SELECT * FROM PhoneBook;")
print("---fetchall()---")
print(cur.fetchall()) #나머지행 리턴 

#쓰기작업
conn.commit() #변경내용 저장

#연결 종료
conn.close()