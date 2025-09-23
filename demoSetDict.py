# demoSetDict.py

print("---set형식---")
a={1,2,3,3}
b={3,4,4,5}

print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))


print("--dict형식---")
fruits={"apple":100, "orange":200}
print(len(fruits))
print(fruits["apple"])
#입력
fruits["kiwi"]=150
#수정
fruits["apple"]=300
print(fruits)
#삭제
del fruits["kiwi"]
print(fruits)
#반복문
for item in fruits.items():
    print(item)