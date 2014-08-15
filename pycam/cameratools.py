import picamera
from time import sleep
import datetime

class PhotoBox:
	
	def __init__(self):	
		self.camera = picamera.PiCamera()
		
	def takePicture(self):
		now = datetime.datetime.now().strftime("image_%Y-%m-%d_%H%M%S.jpg")
		self.camera.capture(now)
		return now
	
	
	
