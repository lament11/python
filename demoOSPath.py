#demoOSPath.py
import random
from os.path import *

print("---랜덤모듈---")
print("random():", random.random())
print("randint(1,10):", random.randint(1, 10))  
print("randrange(20):", [random.randrange(20) for i in range(10)])
print("randrange(20):", [random.randrange(20) for i in range(10)])
print(random.sample(range(20),10))
print(random.sample(range(20),10))

#파이썬 파일의 경로
#raw string notation
filepath = r"c:\python310\python.exe"
if exists(filepath):
    print("파일이 존재합니다.")
    print("디렉터리명:", dirname(filepath))
    print("파일명:", basename(filepath))
    print("파일크기:", getsize(filepath), "바이트")
else:
    print("파일이 존재하지 않습니다.")

import glob
#특정 폴더의 파일 리스트
print(glob.glob(r"C:\work\*.py"))
