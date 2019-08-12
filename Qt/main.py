import sys
import displayUI
from PyQt5.QtWidgets import QApplication, QMainWindow
from uiCtrl import View 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWnd = QMainWindow()
    #调用UI界面
    ui = displayUI.Ui_cvWindow()
    # 可以理解成将创建的 ui 绑定到新建的 mainWnd 上
    ui.setupUi(mainWnd)
    #调用控制函数
    display = View(ui,mainWnd)
    mainWnd.show()

    sys.exit(app.exec_())