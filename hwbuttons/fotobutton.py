import RPi.GPIO as GPIO
from thread import start_new_thread
import time

class FotoButton:


	
	

	def __init__(self, callback):	
		global cbi, lastButton
				
		
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(15,GPIO.IN,pull_up_down=GPIO.PUD_UP)

		cbi = callback
		lastButton = 0		
	
		start_new_thread(self.trun,())

	def trun(a):
		while True:
		  inb = GPIO.input(15)
		  if (not inb and lastButton ):
		    cbi()
		    time.sleep(0.1)

		
		  lastButton = inb				
		  time.sleep(0.01)




if __name__ == "__main__":
	def testPrint():
		print("Foto Button Pressed")
			

	fb = FotoButton(testPrint)
	time.sleep(10)



