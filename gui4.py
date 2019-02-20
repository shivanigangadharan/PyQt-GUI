import cv2
import os
#import cv
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.phonon import Phonon



image_folder = 'images'
video_name = 'video.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name,cv2.VideoWriter_fourcc('M','J','P','G'),1, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()


app = QtGui.QApplication(sys.argv)
vp = Phonon.VideoPlayer()
vp.show()
media = Phonon.MediaSource('video.avi')
vp.load(media)
vp.play()
vp.move(200,100)
vp.setGeometry(50,50, 600, 600)
sys.exit(app.exec_())