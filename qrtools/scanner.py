import zbar
import Image

class ImageScanner:

	def __init__(self):
		self.scanner = zbar.ImageScanner()
		# configure the reader
		self.scanner.parse_config('enable')

		
	def scanImage(self,file):
		# obtain image data
		pil = Image.open(file).convert('L')
		width, height = pil.size
		raw = pil.tostring()

		# wrap image data
		image = zbar.Image(width, height, 'Y800', raw)

		# scan the image for barcodes
		self.scanner.scan(image)
		
		
		
		
		# extract results
		for symbol in image:
			# do something useful with results
			print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
			if symbol:
				# clean up
				del(image)
				return symbol.data
			
		