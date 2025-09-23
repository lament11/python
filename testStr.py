# testStr.py

strC="""이번에는
다중라인으로
저장합니다."""

print(strC)

strB="python"
#슬라이싱(인덱싱)
print(strB[0])
print(strB[1])
print(strB[0:3])
print(strB[:3])
print(strB[-2:])

print("---리스트 형식---")
lst = [10,20,30]
print(lst)
print(len(lst))
lst.append(40)
print(lst)
lst.remove(10)
print(lst)
print(lst[0])

print("---튜플(Tuple)---")
tp=(10,20,30)
print(len(tp))
print(tp.index(30))

#함수를 정의
def times(a,b):
    return a+b, a*b

#호출 
print(times(3,4))

#한번에 여러개 입력
print("id:%s, name:%s" % ("kim","김유신"))