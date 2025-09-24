# demoStr.py
# 문자열 처리와 정규표현식 간단하게 소개
# 정규표현석 : 특정한 패턴을 바로인식 검색
import re

strA= "pythone is very powerful" 
strB="파이썬은 강력해"
print(len(strA), len(strB))  # 영문자 1글자, 한글 1글자
print(strA.capitalize())  # 맨앞글자 대문자
print(strA.replace("python", "java"))  # 문자열 바꾸기
data="<<< spam and ham and egg  >>>"
result=data.strip("<> ")  # 양쪽 공백과 < > 제거
print(result)
lst= result.split()  # 공백 기준으로 문자열 나누기
print(lst)
print(":)".join(lst))  # 리스트를 :로 연결해서 문자열로

#정규표현식:특정한 패턴을 인식
#a*,b*(0번에서 N번 출현횟수),a+,b+(1번에서 N번),a?,b?(0번 또는 1번)
#특정 패턴이 두번째 문자열 데이터에서 포함되어 있으면 검색
result = re.search("[0-9]*th", "35th")  # 0~9사이 숫자가 0개 이상 나오고 th로 끝나는 패턴
print(result)
print(result.group())  # 매칭된 문자열

result = re.search("apple", "this is apple")  # 0~9사이 숫자가 0개 이상 나오고 th로 끝나는 패턴
print(result)
print(result.group())  # 매칭된 문자열

#\d는 digit으로 숫자를 의미 {4} 4자리
result = re.search("\d{4}", "올해는 2025년 입니다.")  # 0~9사이 숫자가 0개 이상 나오고 th로 끝나는 패턴
print(result)
print(result.group())  # 매칭된 문자열