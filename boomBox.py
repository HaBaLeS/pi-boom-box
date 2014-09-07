
from pycam import cameratools
from hwbuttons import fotobutton
from qrtools import scanner
import time
from audiosystem import mp3player


def fotoButtonCB():
	imfl = camera.takePicture() 
	albumhash = imscanner.scanImage(imfl)
	if not albumhash:
		print "Wat ... nix gefunden"
	else: 
		findAndPlayAlbum(albumhash)
def nextSong():
	player.next()
	
def previousSong():
	player.previous()
	
def playPause():
	player.pause()
	

	
def findAndPlayAlbum(albumhash):
	db = open("/home/pi/code/pi-boom-box/playlists.db",'r')
	for line in db:
		entrys = line.split(',')
		if(entrys and entrys[0] == albumhash):
			print entrys[0]
			player.playAlbum(entrys[1])
	
	

camera = cameratools.PhotoBox()
imscanner = scanner.ImageScanner()
player = mp3player.Mp3Player() 


fotobutton.FotoButton(7,fotoButtonCB)
fotobutton.FotoButton(13,nextSong)
fotobutton.FotoButton(11,previousSong)
fotobutton.FotoButton(15,playPause)


while True:
	time.sleep(1)

