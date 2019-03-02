import sys
import os
import cv2
import numpy as numpy
from PyQt4 import QtGui,QtCore






class ControlWindow(QtGui.QWidget):
    def __init__(self,parent=None):
        super(ControlWindow, self).__init__(parent)
        self.capture = None
        self.setWindowTitle('TrackingGUI')
        self.setGeometry(100,100,500,500)
        self.fps = 24
        self.cap = cv2.VideoCapture(0)
       
        self.video_frame = QtGui.QLabel()
        imgg = QtGui.QImage('66.png')
        pix = QtGui.QPixmap.fromImage(imgg)
        self.video_frame.setPixmap(pix)

        


        self.start_button = QtGui.QPushButton('START')
        self.start_button.clicked.connect(self.start_application)
        self.start_button.resize(self.start_button.minimumSizeHint())
        #self.start_button.move(50,0)


        self.end_button = QtGui.QPushButton('END')
        self.end_button.clicked.connect(self.close_application)
        self.end_button.resize(self.end_button.minimumSizeHint())
        #self.end_button.move(50,50)

        self.stop_button = QtGui.QPushButton('STOP')
        self.stop_button.clicked.connect(self.stop_application)
        self.stop_button.resize(self.stop_button.minimumSizeHint())
        #self.stop_button.move(50,100)

        self.quit_button=QtGui.QPushButton('QUIT')
        self.quit_button.clicked.connect(self.close_application)
        self.quit_button.resize(self.quit_button.minimumSizeHint())
        #self.quit_button.move(50,100)



        vbox = QtGui.QVBoxLayout(self)
        vbox.addStretch(1)
        vbox.addWidget(self.video_frame)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.end_button)
        vbox.addWidget(self.stop_button)
        vbox.addWidget(self.quit_button)


        self.setLayout(vbox)


        self.show()

    def setFPS(self, fps):
        self.fps = fps

    def nextFrameSlot(self):
        ret, frame = self.cap.read()
        # OpenCV yields frames in BGR format
        frame = cv2.cvtColor(frame, cv2.cv.CV_BGR2RGB)
        img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(img)
        self.video_frame.setPixmap(pix)

    def start(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.nextFrameSlot)
        self.timer.start(1000./self.fps)

    def stop(self):
        self.timer.stop()

    def deleteLater(self):
        self.cap.release()
        super(QtGui.QWidget, self).deleteLater()


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