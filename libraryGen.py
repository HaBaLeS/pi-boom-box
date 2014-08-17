#Duchr verzeichnisse gehen wenn ein verziechnis keine unterverzeichnise hat und min. 1 mp3 drin ist, dann ist ein Album
#schauen ob die comer datei da ist. wenn nicht melden wenn ja playlist.mpu erstellen und image erzeugen.

import os
from PIL import Image, ImageDraw, ImageColor
from qrcode import *
from io import BytesIO


def hasAudio(fileList, rootDir):
	for f in fileList:
		if 'mp3' in f:
			return True
	print "No MP3s in Folder " + root
	return False
	
def buildPlaylist(fileList,rootDir):
	plPath = rootDir + '/pb-playlist.m3u'
	#print plPath
	pl = open(plPath,'w')
	for f in fileList:
		if 'mp3' in f:
			pl.write(str(f) + '\n')
	pl.close();
	#print 'Build PlayList'
	
def buildQRImage(root):
	coverImg = root + '/cover.jpg'
	if not os.path.isfile(coverImg):
		print 'No Cover for ' + root
		return 
	print 
	outImage = '/home/pi/code/pi-boom-box/output/' + root.rsplit('/',1)[1]	+ '.jpg'
	
	cover = Image.open(coverImg)
	cover = cover.resize((600,600))
	
	qr = QRCode(version=6, error_correction=ERROR_CORRECT_M)
	qr.add_data(root + '/pb-playlist.m3u')
	qr.make() # Generate the QRCode itself
	
	qrImg = qr.make_image()
	qrImg = qrImg.resize((600,600))

	qrZettel = Image.new("RGB", (1240,620))
	draw = ImageDraw.Draw(qrZettel)
	draw.rectangle([(0,0),(1240,620)], fill=(220,220,220), outline=(0,0,0))


	qrZettel.paste(qrImg, (630,10,1230,610))
	qrZettel.paste(cover, (10,10,610,610))
	qrZettel.save(outImage)
	
	print 'Build QR Image'
	

for root, dirs, files in os.walk('/home/pi/audio/hoerspiele'):
	if(len(dirs) == 0):
		if(hasAudio(files, root)):
			buildPlaylist(sorted(files),root)
			buildQRImage(root)
