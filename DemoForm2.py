# DemoForm2.py
# DemoForm2.ui(화면단) + DemoForm2.py(로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

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
        self.label.setText("첫번째 버튼 클릭") 
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