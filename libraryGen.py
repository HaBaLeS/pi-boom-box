#Duchr verzeichnisse gehen wenn ein verziechnis keine unterverzeichnise hat und min. 1 mp3 drin ist, dann ist ein Album
#schauen ob die comer datei da ist. wenn nicht melden wenn ja playlist.mpu erstellen und image erzeugen.

import os
from PIL import Image, ImageDraw, ImageColor
from qrcode import *
from io import BytesIO
import hashlib

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
	

	
	#Check Generated indicator
	if os.path.isfile(root + '/GENERATED'):
		print "skip " + root
		return
	
	#Generate Generated indicator
	gen = open(root+'/GENERATED','w')
	gen.write("xXx")
	gen.close()
	
	
	locationName = root.rsplit('/',1)[1]
	hashCode = hashlib.sha224(locationName).hexdigest()
	
	db = open("/home/pi/code/pi-boom-box/playlists.db",'a')
	db.write(hashCode + "," + root + '/pb-playlist.m3u' + "\n")
	db.close()
	
	coverImg = root + '/cover.jpg'
	if not os.path.isfile(coverImg):
		print 'No Cover for ' + root
		return 
	print 
	#outImage = '/home/pi/code/pi-boom-box/output/' + root.rsplit('/',1)[1]	+ '.jpg'
	outImage = '/home/pi/code/pi-boom-box/output/' + hashCode	+ '.jpg'
	
	cover = Image.open(coverImg)
	cover = cover.resize((600,600))
	
	qr = QRCode(version=6, error_correction=ERROR_CORRECT_M)
	qr.add_data(hashCode)
	qr.make() # Generate the QRCode itself
	
	qrImg = qr.make_image()
	qrImg = qrImg.resize((600,600))

	qrZettel = Image.new("RGB", (1240,620))
	draw = ImageDraw.Draw(qrZettel)
	draw.rectangle([(0,0),(1240,620)], fill=(220,220,220), outline=(0,0,0))


	qrZettel.paste(qrImg, (630,10,1230,610))
	qrZettel.paste(cover, (10,10,610,610))
	qrZettel.save(outImage)
	qrZettel.save(root+'qrZettel.jpg')
	
	
	print 'Build QR Image'
	

for root, dirs, files in os.walk('/home/pi/audio/'):
	if(len(dirs) == 0):
		if(hasAudio(files, root)):
			buildPlaylist(sorted(files),root)
			buildQRImage(root)
