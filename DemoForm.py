# DemoForm.py
# DemoForm.ui(화면단) + DemoForm.py(로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic   

#디자인 파일을 로딩
form_class = uic.loadUiType("DemoForm.ui")[0]

#윈도우 클래스 정의(처음에는 QDialog 상속, 다중상속)
class DemoForm(QDialog, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)  #화면단 로딩
        self.label.setText("첫번째 PyQt데모")      

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