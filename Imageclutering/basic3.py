import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QPushButton,QTextEdit, QFileDialog,QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout


class window(QWidget):
	def __init__(self):
		super(window,self).__init__()
		self.setGeometry(20,20,500,300)
		self.setWindowTitle('himss')

		self.vlayout=QVBoxLayout()


		self.btn2=QPushButton('browse',self)
		self.btn2.clicked.connect(self.file_open)
		self.btn2.resize(100,50)
		self.btn2.move(210,200)


		#self.le=QLabel(self)
		self.vlayout.addWidget(self.btn2)
		#self.vlayout.addWidget(self.le)

		self.setLayout(self.vlayout)


		self.show()

	#def home(self):
		#btn1=QPushButton('quit',self)
		#btn1.clicked.connect(self.close_application)
		#btn1.resize(100,50)
		#btn1.move(100,200)


		



	def close_application(self):
		sys.exit()



	def file_open(self):
        # need to make name an tupple otherwise i had an error and app crashed
		name,_= QFileDialog.getOpenFileNames(self, 'Open File', options=QFileDialog.DontUseNativeDialog)
		
		self.hbox=QHBoxLayout()

		for image in name:
			self.le=QLabel(self)
			self.le.setPixmap(QPixmap(image))
			self.hbox.addWidget(self.le)



		self.vlayout.addLayout(self.hbox)
		self.btn3=QPushButton('quit',self)
		self.btn2.clicked.connect(self.close_application)
		self.vlayout.addWidget(self.btn3)


			

		
			
		#self.le.move(50,50)
		#self.resize(100,100)
		



def run():
	app=QApplication(sys.argv)
	gui=window()
	sys.exit(app.exec_())

run()