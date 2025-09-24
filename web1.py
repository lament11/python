# web1.py
# 웹 크롤링 연습
from bs4 import BeautifulSoup

#웹페이지 로딩(read test): 유니코드로 해석(utf-8)
page=open("test01.html", "rt", encoding="utf-8").read()
#검색이 용이한 객체 생성
#두번째 인자 : 파서종류(html.parser:90%이상, lxml, xml 등)
soup=BeautifulSoup(page, "html.parser")
#전체 태그를 보여주기
#print(soup.prettify())
#<p>태그 검색
#선택하고 주석처리 : ctrl + /
# plist=soup.find_all("p")
# print(plist)
#첫번째 <p>태그 검색
# p1=soup.find("p")
# print(p1)
#조건이 있는 검색 : <p class="outer-text">만 검색
#파이썬에서 class는 예약어이므로 class_로 작성
# p2=soup.find_all("p", class_="outer-text")
# print(p2) 
#속성을 검색:attrs={"속성명":"속성값"} ==>attributes
p3=soup.find_all("p", attrs={"class":"outer-text"})
#print(p3)
# 태그는 삭제하고 문자열만 출력 + 앞뒤에 공백도 제거 : .text
# for item in p3:
#     #연속으로 객체의 속성이나 메서드를 호출 : 메서드 체인
#     title=item.text.strip()
#     print(title)