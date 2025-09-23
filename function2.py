# function2.py 

#LGB이름 해석 규칙
#전역변수
x=5
def fun1(a):
    return a+x

#호출
print(fun1(1))

def func2(a):
    #지역변수
    x=1
    return a+x

print(func2(1))

#기본 값이 있는 경우
def times(a=10, b=20):
    return a*b 

#호출
print( times() )
print( times(5) )
print( times(5,6) )

#키워드 인자 방식 전달
def connectURI(server, port):
    str = "http://" + server + ":" + port 
    return str 

print(connectURI("credu.com", "80"))
print(connectURI(port="80",server="test.com"))

#가변인자(갯수가 정해져 있지 않은경우)
# *Tuple이라는 힌트
def union(*ar):
    #지역변수로 리스트 초기화
    res = []
    for item in ar:
        for x in item:
            if x not in res:
                res.append(x)
    return res 

print( union("HAM","SPAM") )
print( union("HAM","SPAM","EGG") )


#람다 함수 정의
g = lambda x,y:x*y
print( g(2,3) )
print( g(3,5) )
#즉흥적으로, 이름없이 함수를 정의
print( (lambda  x:x*x)(3) )
print( dir() )
print( globals() )

