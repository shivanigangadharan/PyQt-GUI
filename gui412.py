import sys
import os
import utils


from PyQt4 import QtGui,QtCore

class SlideShowPics(QtGui.QMainWindow):

    """ SlideShowPics class defines the methods for UI and
        working logic
    """
    def __init__(self, imgLst, parent=None):
        super(SlideShowPics, self).__init__(parent)
        # self._path = path
        self._imageCache = []
        self._imagesInList = imgLst
        self._pause = False
        self._count = 0
        self.animFlag = True
      
        self.updateTimer = QtCore.QTimer()
        self.updateTimer.timeout.connect(self.nextImage)
        self.updateTimer.start(250)
        self.prepairWindow()
        self.nextImage()
        

    

    def prepairWindow(self):
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQT tuts!")


        extractAction = QtGui.QAction("&FILE", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)
        

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&FILE')
        fileMenu.addAction(extractAction)

        self.label = QtGui.QLabel()
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.setCentralWidget(self.label)
        #self.label.move(100,100)

        btn = QtGui.QPushButton("OPENN", self)
        btn.clicked.connect(self.openit)
        btn.resize(btn.minimumSizeHint())
        btn.move(50,0)


        pbtn = QtGui.QPushButton("Pause", self)
        pbtn.clicked.connect(self.pause_application)
        pbtn.resize(pbtn.minimumSizeHint())
        pbtn.move(50,50)


        sbtn = QtGui.QPushButton("start", self)
        sbtn.clicked.connect(self.start_application)
        sbtn.resize(pbtn.minimumSizeHint())
        sbtn.move(50,100)




        print(self.style().objectName())
        self.styleChoice = QtGui.QLabel(self)


        number = 3

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

        keylist = []

        for i in range(number):
            keylist.append(int(input("Enter person id: ")))

        comboBox = QtGui.QComboBox(self)

        for i in range(number):
            comboBox.addItem("{0}".format(pers_id[keylist[i]]))
        
        comboBox.move(50, 250)
        
        self.styleChoice.move(50,150)
        comboBox.activated[str].connect(self.style_choice)


    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))


    def pause_application(self):
        self.updateTimer.stop()

    def start_application(self):
        if self._count==len(self._imagesInList):
            self._count=0

        self.updateTimer.start(250)

    def openit(self):
        





    def close_application(self):
        choice=QtGui.QMessageBox.question(self,'choose','Do you want to exit?',QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
        if choice==QtGui.QMessageBox.Yes:
            print("exiting")
            sys.exit()
        else:
            pass

    def nextImage(self):
        """ switch to next image or previous image
        """
        if self._imagesInList:
            if self._count == len(self._imagesInList):
                #pass
                self.updateTimer.stop()

            else:
                self.showImageByPath(self._imagesInList[self._count])

            self._count=self._count+1

            #if self.animFlag:
            #    self._count += 1
            #else:
            #    self._count -= 1


    def showImageByPath(self, path):
        if path:
            image = QtGui.QImage(path)
            pp = QtGui.QPixmap.fromImage(image)
            self.label.setPixmap(pp.scaled(
                    200,200,
                    QtCore.Qt.KeepAspectRatio,
                    QtCore.Qt.SmoothTransformation))
            #self.label.move(0,100)
    
def main(paths):
    if isinstance(paths, list):
        imgLst = utils.imageFilePaths(paths)
    elif isinstance(paths, str):
        imgLst =  utils.imageFilePaths([paths])
    else:
        print " You can either enter a list of paths or single path"
    app = QtGui.QApplication(sys.argv)
    if imgLst:
        window =  SlideShowPics(imgLst)
        window.show()
        #window.raise_()
        sys.exit(app.exec_())
    else:
        msgBox = QtGui.QMessageBox()
        msgBox.setText("No Image found in any of the paths below\n\n%s" % paths)
        msgBox.setStandardButtons(msgBox.Cancel | msgBox.Open);
        if msgBox.exec_() == msgBox.Open:
            main(str(QtGui.QFileDialog.getExistingDirectory(None, 
                "Select Directory to SlideShow",
                os.getcwd())))

if __name__ == '__main__':
   # curntPaths = os.getcwd()
   # if len(sys.argv) > 1:
    #    curntPaths = sys.argv[1:]
    #image_folder='images'
    #images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    curntPaths='images'
    main(curntPaths)