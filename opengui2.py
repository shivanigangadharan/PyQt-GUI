import sys
import os
import cv2
import numpy as numpy
from PyQt4 import QtGui,QtCore
import random






class ControlWindow(QtGui.QWidget):
    def __init__(self,parent=None):
        super(ControlWindow, self).__init__(parent)
        self.capture = None
        self.setWindowTitle('TrackingGUI')
        self.setGeometry(0,0,300,300)
        self.fps = 24
        self.count=0
        self.newlist=[]
        self.cap = cv2.VideoCapture(0)
       
        self.video_frame = QtGui.QLabel()
        imgg = QtGui.QImage('himani.jpg')
        pix = QtGui.QPixmap.fromImage(imgg)
        self.video_frame.setPixmap(pix)


        icon  = QtGui.QPixmap('himani.jpg')
        #button.setIcon(icon)
        


        self.start_button = QtGui.QPushButton('START')
        self.start_button.clicked.connect(self.start_application)
        self.start_button.resize(self.start_button.minimumSizeHint())
        #self.start_button.setIcon(icon)
        self.start_button.setStyleSheet("background-image:url(\"start.png\")")
        #self.start_button.move(50,0)


        self.end_button = QtGui.QPushButton('END')
        self.end_button.clicked.connect(self.close_application)
        self.end_button.resize(self.end_button.minimumSizeHint())

        #self.end_button.move(50,50)

        self.stop_button = QtGui.QPushButton('PAUSE')
        self.stop_button.clicked.connect(self.stop_application)
        self.stop_button.resize(self.stop_button.minimumSizeHint())
        #self.stop_button.move(50,100)

        self.quit_button=QtGui.QPushButton('QUIT')
        self.quit_button.clicked.connect(self.close_application)
        self.quit_button.resize(self.quit_button.minimumSizeHint())
        #self.quit_button.move(50,100)

        #number = random.randrange(1,12)
        self.comboBox = QtGui.QComboBox()
        

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.end_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.quit_button)
        hbox.addWidget(self.comboBox)


        #vbox1=QtGui.QVBoxLayout(self)
        #vbox1.addWidget(self.comboBox)

        vbox = QtGui.QVBoxLayout(self)
        vbox.addStretch(1)
        vbox.addWidget(self.video_frame)
        vbox.addLayout(hbox)

        
        #hbox.addWidget(self.comboBox)


        self.setLayout(vbox)


        self.show()

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
        self.timer.start(1000./self.fps)

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