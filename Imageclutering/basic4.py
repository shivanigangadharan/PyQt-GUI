import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QPushButton,QTextEdit, QFileDialog,QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLineEdit, QInputDialog


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
		
		self.vbox=QVBoxLayout()

		for image in name:
			self.minivbox=QVBoxLayout()
			self.le=QLabel(self)
			self.le.setPixmap(QPixmap(image))
			self.minivbox.addWidget(self.le)
			self.btnn = QPushButton('enter', self)
        	#self.btn.move(20, 20)
			self.btnn.clicked.connect(self.showDialog)
			self.txt = QLineEdit(self)
			self.minivbox.addWidget(self.btnn)
			self.minivbox.addWidget(self.txt)

			self.vbox.addLayout(self.minivbox)




		self.vlayout.addLayout(self.vbox)
		self.btn3=QPushButton('quit',self)
		self.btn2.clicked.connect(self.close_application)
		self.vlayout.addWidget(self.btn3)


			

		
	def showDialog(self):
        
		text, ok = QInputDialog.getText(self, 'Input Dialog', 
			'Enter your name:')
        
		if ok:
			self.txt.setText(str(text))
        		
		#self.le.move(50,50)
		#self.rese(100,100)
		



def run():
	app=QApplication(sys.argv)
	gui=window()
	sys.exit(app.exec_())

run()