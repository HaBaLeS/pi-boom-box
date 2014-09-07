import RPi.GPIO as GPIO
from thread import start_new_thread
import time

class FotoButton:


	

	def __init__(self,pin, callback):	
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
		
		start_new_thread(self.trun,(pin,callback))

	def trun(a, pin, cbi):
		lastButton = 0
		while True:
		  inb = GPIO.input(pin)
		  if (not inb and lastButton ):
		    cbi()
		    time.sleep(0.1)
			
		  lastButton = inb				
		  time.sleep(0.01)




if __name__ == "__main__":
	def testPlay():
		print("Play/Pause Button Pressed")
			
	def testFF():
		print("Fast Forward Button Pressed")

	def testFR():
		print("Fast Rewind Button Pressed")

	def testFoto():
		print("Foto Button Pressed")
		
		
	
	fb2 =FotoButton(13,testFF)
	fb3 = FotoButton(11,testFR)
	fb4 = FotoButton(7,testFoto)
	fb1 = FotoButton(15,testPlay)
	
	time.sleep(100)



