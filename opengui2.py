import sys
import os
import cv2
import numpy as numpy
from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import random

class ControlWindow(QtGui.QWidget):
    def __init__(self,parent=None):
        super(ControlWindow, self).__init__(parent)
        self.capture = None
        self.setWindowTitle('TrackingGUI')
        self.setGeometry(0,0,900,700)

        self.fps = 24
        self.count=0
        self.newlist=[]
        self.cap = cv2.VideoCapture(0)

        """oimage=QImage('photo.jpg')
        sImage=oimage.scaled(QSize(900,700))
        palette=QPalette()

        palette.setBrush(10,QBrush(sImage))
        self.setPalette(palette)

        self.label4=QLabel('photo.jpg',self)
        """
       
        self.video_frame = QtGui.QLabel()
        imgg = QtGui.QImage('logo.png')
        pix = QtGui.QPixmap.fromImage(imgg)
        pix2=pix.scaled(650,600,QtCore.Qt.KeepAspectRatio)
        #self.video_frame.setStyleSheet("height:700px; margin-top:100px;")
        self.video_frame.setPixmap(pix2)
        
        
        self.centralwidget=QtGui.QWidget(self)

        self.start_button = QtGui.QPushButton('START')
        self.start_button.clicked.connect(self.start_application)
        self.start_button.resize(self.start_button.minimumSizeHint())
        #self.start_button.setIcon(icon)
        #self.start_button.setStyleSheet("background-image:url(\"start.png\")")
        #self.start_button.setStyleSheet("height:20px")
        self.start_button.setStyleSheet("height:20px; margin:20px;")
       

        self.stop_button = QtGui.QPushButton('PAUSE')
        self.stop_button.clicked.connect(self.stop_application)
        #self.stop_button.setStyleSheet("height:20px")
        self.stop_button.setStyleSheet("height:20px; margin:20px;")


        self.quit_button=QtGui.QPushButton('QUIT')
        self.quit_button.clicked.connect(self.close_application)
        self.quit_button.setStyleSheet("height:20px; margin:20px;")

    
        #self.quit_button.setStyleSheet("height:20px;margin:10px")
    
        #self.comboBoxWidget=QtGui.QWidget(self.centralwidget)
        #self.comboBoxWidget.setGeometry(QtCore.QRect(0,0,50,50))

        #self.comboBox = QtGui.QComboBox(self.comboBoxWidget)

        self.comboBox=QtGui.QComboBox()
        self.comboBox.setStyleSheet("height:30px")
        font = self.comboBox.font()
        font.setPointSize(20)
        self.comboBox.setFont(font)
        #self.comboBox.setStyleSheet("width:40px")

        self.s1 = QSlider(Qt.Horizontal)
        self.s1.setMinimum(30)
        self.s1.setMaximum(100)
        self.s1.setValue(50)
        self.s1.valueChanged.connect(self.valuechange)

        self.s2 = QSlider(Qt.Horizontal)
        self.s2.setMinimum(0)
        self.s2.setMaximum(1)
        self.s2.setValue(0.0)
        self.s2.setTickPosition(QSlider.TicksBelow)
        self.s2.setTickInterval(5)
        self.s2.valueChanged.connect(self.valuechange2)





        self.verticalayoutWidget=QtGui.QWidget(self.centralwidget)
        self.verticalayoutWidget.setGeometry(QtCore.QRect(0,0,680,700))

        self.vbox=QtGui.QVBoxLayout(self.verticalayoutWidget)


        self.vbox.addWidget(self.video_frame)


        self.verticalayoutWidget_2=QtGui.QWidget(self.centralwidget)
        self.verticalayoutWidget_2.setGeometry(QtCore.QRect(670,200,200,300))

        self.vbox2=QtGui.QVBoxLayout(self.verticalayoutWidget_2)
        #self.vbox2.addStretch(1)

        self.label1 = QLabel()
        self.label2 = QLabel()
        self.label3 = QLabel()

        self.label1.setText("Select Person:-")
        self.label2.setText("Adjust Age:-")
        self.label3.setText("Ajust minimum confidence:-")



        self.vbox2.addWidget(self.label1)
        self.vbox2.addWidget(self.comboBox)
        self.vbox2.addWidget(self.label2)
        self.vbox2.addWidget(self.s1)
        self.vbox2.addWidget(self.label3)
        self.vbox2.addWidget(self.s2)


        self.horizontalayoutWidget=QtGui.QWidget(self.centralwidget)
        self.horizontalayoutWidget.setGeometry(QtCore.QRect(0,600,680,91))

        self.hbox=QtGui.QHBoxLayout(self.horizontalayoutWidget)
        #self.hbox.setContentMargins(0,0,0,0)
        #self.hbox.addStretch(1)
        self.hbox.addWidget(self.start_button)
        self.hbox.addWidget(self.stop_button)
        self.hbox.addWidget(self.quit_button)




        #self.setLayout(self.vbox)
        #self.setLayout(self.vbox2)









        

        """hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.end_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.quit_button)
        hbox.addWidget(self.comboBox)


        

        vbox = QtGui.QVBoxLayout(self)
        vbox.addStretch(1)
        vbox.addWidget(self.video_frame)
        vbox.addLayout(hbox)

        
       

        self.setLayout(vbox)"""


        self.show()

    def valuechange(self):
        size = self.s1.value()
        #print(size)

    def valuechange2(self):
        size2=self.s2.value()
        #print(size2)

    def dropdown(self,number):

        pers_id = { 
            0: "Name",
            1: "Rohit", 
            2: "Himani", 
            3: "Shivani", 
            4: "Lovetesh", 
            5: "Manu",
            6: "Sakshi",
            7: "Ross",
            8: "Rachel",
            9: "Phoebe",
            10: "Ross",
            11: "Joey",
            12: "Chandler"
            }

    
        keylist=number

        for i in keylist:
            self.comboBox.addItem("{0}".format(pers_id[i]))
        #self.comboBox.clear()  
        self.comboBox.activated[str].connect(self.style_choice)

    def style_choice(self,text):
        print(text)
         
           #self.styleChoice.setText(text)



    def setFPS(self, fps):
        self.fps = fps

    def nextFrameSlot(self):
        ret, frame = self.cap.read()
        # OpenCV yields frames in BGR format
        frame = cv2.cvtColor(frame, cv2.cv.CV_BGR2RGB)
        img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)

        ############MANU CODE
        pix = QtGui.QPixmap.fromImage(img)
        self.video_frame.setPixmap(pix)
        self.comboBox.clear()

        self.count=random.randrange(1,6)
        self.newlist=random.sample(range(10),self.count)
        self.dropdown(self.newlist)



    def start(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.nextFrameSlot)
        self.timer.start(100./self.fps)

    def stop(self):
        self.timer.stop()

    def deleteLater(self):
        self.cap.release()
        #cv2.destroyAllWindows()
        #super(QtGui.QWidget, self).deleteLater()


    def start_application(self):
        self.start()

    def stop_application(self):
        self.stop()

    def end_application(self):
        self.deleteLater(self)








    def close_application(self):
        choice=QtGui.QMessageBox.question(self,'choose','Do you want to exit?',QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
        if choice==QtGui.QMessageBox.Yes:
            print("exiting")
            sys.exit()
        else:
            pass

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    window = ControlWindow()
    sys.exit(app.exec_())