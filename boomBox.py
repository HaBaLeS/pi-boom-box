
from pycam import cameratools
from hwbuttons import fotobutton
from qrtools import scanner
import time


def fotoButtonCB():
	imfl = camera.takePicture() 
	imscanner.scanImage(imfl)
	print imfl

fButton = fotobutton.FotoButton(fotoButtonCB)
camera = cameratools.PhotoBox()
imscanner = scanner.ImageScanner()

while True:
	time.sleep(1)

