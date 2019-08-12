import cv2
import threading
from PyQt5.QtWidgets import QFileDialog,QGraphicsPixmapItem,QGraphicsScene
from PyQt5.QtGui import QImage, QPixmap

class View:

    def __init__(self,ui,MainWindow):

        self.ui = ui
        self.MainWindow = MainWindow

        #链接按键功能函数
        self.ui.Open.clicked.connect(self.Open)
        self.ui.Close.clicked.connect(self.Close)

        # #创建一个关闭事件
        self.stopEvent = threading.Event()
        self.stopEvent.clear()
   
    def Open(self):
        if self.ui.localFile.isChecked():
            self.fileName, self.fileType = QFileDialog.getOpenFileName(self.MainWindow, \
            	'Choose file', '', '*.mp4')
            if self.fileName:
                self.cap = cv2.VideoCapture(self.fileName)
        elif self.ui.camera.isChecked():
            self.cap = cv2.VideoCapture(0)
        else:
            return   
        self.Display()    

           
    
    def Close(self):
    	self.stopEvent.set()

    def Display(self):
        while self.cap.isOpened():

            self.ui.Open.setEnabled(False)
            self.ui.Close.setEnabled(True)

            ret,frame = self.cap.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            rows,cols = frame.shape[:2]
            frame = QImage(frame, cols, rows, QImage.Format_RGB888)
            pix = QPixmap.fromImage(frame)
            item = QGraphicsPixmapItem(pix)
            scene = QGraphicsScene()
            scene.addItem(item)
            self.ui.display.setScene(scene)
            self.ui.display.fitInView(item)

            key = cv2.waitKey(25)

                        # 判断关闭事件是否已触发
            if self.stopEvent.is_set() == True:
                # 关闭事件置为未触发，清空显示label
                self.stopEvent.clear()
                self.ui.display.destroy()
                self.ui.Close.setEnabled(False)
                self.ui.Open.setEnabled(True)
                self.cap.release()
                break


    		
                   


	