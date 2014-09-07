from mplayer import Player

class Mp3Player():
	
	def __init__(self):
		Player.exec_path = '/usr/bin/mplayer'
		Player.introspect()
		self.p = Player()
		
	def playAlbum(self, filename):
		self.p.loadlist(filename)
		
	def pause(self):
		self.p.pause()
		
	def previous(self):
		#TODO on press allway the previous track is playerd. normaly the first press goes back
		#to the start of the current track
		# -- to archive this we should first read the current positon .. is it is > XX sec we seek to 0 if below we go to previous track
		self.p.pt_step(-1)
		
	def next(self):
		self.p.pt_step(1)