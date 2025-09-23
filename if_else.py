#파이썬은 오타체크가 안된다!
#선언이 없기 때문에 문제!

score = int(input('점수를 입력: '))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"
else:
    grade = "F"
    
print("Grade is " + grade)
