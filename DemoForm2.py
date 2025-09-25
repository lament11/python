# DemoForm2.py
# DemoForm2.ui(화면단) + DemoForm2.py(로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from bs4 import BeautifulSoup
import urllib.request
import re

#2번째 디자인 파일을 로딩(DemoForm2.ui)
form_class = uic.loadUiType("DemoForm2.ui")[0]

#윈도우 클래스 정의(QMainWindow, 다중상속)
class DemoForm(QMainWindow, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)  #화면단 로딩
    # 슬롯 메서드 추가
    def firstClick(self):
        #파일에 저장
        f= open('clien2.txt','w',encoding='utf-8')

        #페이징처리
        for i in range(0,10):
            #웹서버에 데이터 전달 : QueryString방식
            url="https://www.clien.net/service/board/" \
                + "sold?&od=T31&category=0&po=" + str(i)
            print(url)
            #페이지 실행 결과 문자열
            data=urllib.request.urlopen(url)
            #스프 객체 생성
            soup=BeautifulSoup(data,'html.parser')

            # 선택한 블럭 주석 : ctrl + /
            # <span class="subject_fixed" data-role="list-title-text" title="용인) 아이폰 15 프로 맥스 1테라 화이트 팝니다">
            # 							용인) 아이폰 15 프로 맥스 1테라 화이트 팝니다
            # 						</span>

            #중고장터 매물 제목
            list=soup.find_all('span',attrs={'data-role':'list-title-text'})
            for item in list:
                #문자열 가공
                title=item.text.strip()
                print(title)
                f.write(title+'\n')

        #1열에서 코딩
        f.close()

        self.label.setText("클리앙 중고장터 크롤링 완료 ") 


    def secondClick(self):
        self.label.setText("두번째 버튼 클릭했음")
    def thirdClick(self):
        self.label.setText("세번째 버튼 클릭~~")    

#진입점(Entry Point)를 체크: 직접 실행할 때만 실행
if __name__ == "__main__":    
    #먼저 실행 프로세스를 만들기
    app = QApplication(sys.argv)  
    #윈도우 클래스의 인스턴스 생성
    demoWindow = DemoForm()       
    #화면에 보여주기
    demoWindow.show()             
    #대기하면서 이벤트 처리
    sys.exit(app.exec_())         