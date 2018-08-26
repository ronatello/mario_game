import numpy as np
import random

class gameMap():

	def __init__(self):
		self.levelmap = np.empty((32, 500), dtype='U')
	
		self.levelmap[0:29, 0:500] = ' '
		self.levelmap[29, 0:500] = 'w'
		self.levelmap[30, 0:499:2] = '|'
		self.levelmap[30, 1:500:2] = '-'
		self.levelmap[31, 0:500] = 'T'

		#generating gaps#
		self.randx = random.randint(60, 91)
		self.randwidth = random.randint(6, 9)
		self.levelmap[28:32, self.randx:self.randx + self.randwidth] = ' '

		self.randx = random.randint(40, 60)
		self.randwidth = random.randint(6, 9)
		self.levelmap[28:32, self.randx:self.randx + self.randwidth] = ' '

		#generating pipes#
		self.randx = random.randint(280, 285)
		
		self.levelmap[23, self.randx] = '|'
		self.levelmap[23, self.randx + 17] = '|'
		self.levelmap[23, self.randx + 1:self.randx + 17] = 'B'
		
		self.levelmap[24:30, self.randx + 4] = '|'
		self.levelmap[24:30, self.randx + 13] = '|'
		self.levelmap[24:30, self.randx + 5:self.randx + 13] = 'H'

		self.randx = random.randint(100, 121)
		
		self.levelmap[23, self.randx] = '|'
		self.levelmap[23, self.randx + 17] = '|'
		self.levelmap[23, self.randx + 1:self.randx + 17] = 'B'
		
		self.levelmap[24:30, self.randx + 4] = '|'
		self.levelmap[24:30, self.randx + 13] = '|'
		self.levelmap[24:30, self.randx + 5:self.randx + 13] = 'H'


		#generating boxes#
		self.randnum = random.randint(0,2)
		self.randx = random.randint(140, 161)

		if(self.randnum < 1):
			self.levelmap[19:22, self.randx:self.randx + 6:5] = '|'
			self.levelmap[19:22, self.randx + 1:self.randx + 4:2] = ']'
			self.levelmap[19:22, self.randx + 2:self.randx + 5:2] = '['

		self.randnum = random.randint(0,2)
		self.randx += 6

		if(self.randnum < 1):
			self.levelmap[19:22, self.randx:self.randx + 6:5] = '|'
			self.levelmap[19:22, self.randx + 1:self.randx + 4:2] = ']'
			self.levelmap[19:22, self.randx + 2:self.randx + 5:2] = '['

		self.randnum = random.randint(0,2)
		self.randx += 6

		if(self.randnum < 1):
			self.levelmap[19:22, self.randx:self.randx + 6:5] = '|'
			self.levelmap[19:22, self.randx + 1:self.randx + 4:2] = ']'
			self.levelmap[19:22, self.randx + 2:self.randx + 5:2] = '['

		self.randnum = random.randint(0,2)
		self.randx += 6

		if(self.randnum < 1):
			self.levelmap[19:22, self.randx:self.randx + 6:5] = '|'
			self.levelmap[19:22, self.randx + 1:self.randx + 4:2] = ']'
			self.levelmap[19:22, self.randx + 2:self.randx + 5:2] = '['

		self.randnum = random.randint(0,2)
		self.randx += 6

		if(self.randnum < 1):
			self.levelmap[19:22, self.randx:self.randx + 6:5] = '|'
			self.levelmap[19:22, self.randx + 1:self.randx + 4:2] = ']'
			self.levelmap[19:22, self.randx + 2:self.randx + 5:2] = '['

		self.randnum = random.randint(0,2)
		self.randx += 6

		if(self.randnum < 1):
			self.levelmap[19:22, self.randx:self.randx + 6:5] = '|'
			self.levelmap[19:22, self.randx + 1:self.randx + 4:2] = ']'
			self.levelmap[19:22, self.randx + 2:self.randx + 5:2] = '['



		self.randnum = random.randint(0,2)
		self.randx = random.randint(240, 245)

		if(self.randnum < 1):
			self.levelmap[19:22, self.randx:self.randx + 6:5] = '|'
			self.levelmap[19:22, self.randx + 1:self.randx + 4:2] = ']'
			self.levelmap[19:22, self.randx + 2:self.randx + 5:2] = '['

		self.randnum = random.randint(0,2)
		self.randx += 6

		if(self.randnum < 1):
			self.levelmap[19:22, self.randx:self.randx + 6:5] = '|'
			self.levelmap[19:22, self.randx + 1:self.randx + 4:2] = ']'
			self.levelmap[19:22, self.randx + 2:self.randx + 5:2] = '['

		self.randnum = random.randint(0,2)
		self.randx += 6

		if(self.randnum < 1):
			self.levelmap[19:22, self.randx:self.randx + 6:5] = '|'
			self.levelmap[19:22, self.randx + 1:self.randx + 4:2] = ']'
			self.levelmap[19:22, self.randx + 2:self.randx + 5:2] = '['

		self.randnum = random.randint(0,2)
		self.randx += 6

		if(self.randnum < 1):
			self.levelmap[19:22, self.randx:self.randx + 6:5] = '|'
			self.levelmap[19:22, self.randx + 1:self.randx + 4:2] = ']'
			self.levelmap[19:22, self.randx + 2:self.randx + 5:2] = '['

		self.randnum = random.randint(0,2)
		self.randx += 6

		if(self.randnum < 1):
			self.levelmap[19:22, self.randx:self.randx + 6:5] = '|'
			self.levelmap[19:22, self.randx + 1:self.randx + 4:2] = ']'
			self.levelmap[19:22, self.randx + 2:self.randx + 5:2] = '['

		self.randnum = random.randint(0,2)
		self.randx += 6

		if(self.randnum < 1):
			self.levelmap[19:22, self.randx:self.randx + 6:5] = '|'
			self.levelmap[19:22, self.randx + 1:self.randx + 4:2] = ']'
			self.levelmap[19:22, self.randx + 2:self.randx + 5:2] = '['





		self.randnum = random.randint(0,2)
		self.randx = random.randint(370, 390)

		if(self.randnum < 1):
			self.levelmap[19:22, self.randx:self.randx + 6:5] = '|'
			self.levelmap[19:22, self.randx + 1:self.randx + 4:2] = ']'
			self.levelmap[19:22, self.randx + 2:self.randx + 5:2] = '['

		self.randnum = random.randint(0,2)
		self.randx += 6

		if(self.randnum < 1):
			self.levelmap[19:22, self.randx:self.randx + 6:5] = '|'
			self.levelmap[19:22, self.randx + 1:self.randx + 4:2] = ']'
			self.levelmap[19:22, self.randx + 2:self.randx + 5:2] = '['

		self.randnum = random.randint(0,2)
		self.randx += 6

		if(self.randnum < 1):
			self.levelmap[19:22, self.randx:self.randx + 6:5] = '|'
			self.levelmap[19:22, self.randx + 1:self.randx + 4:2] = ']'
			self.levelmap[19:22, self.randx + 2:self.randx + 5:2] = '['

		self.randnum = random.randint(0,2)
		self.randx += 6

		if(self.randnum < 1):
			self.levelmap[19:22, self.randx:self.randx + 6:5] = '|'
			self.levelmap[19:22, self.randx + 1:self.randx + 4:2] = ']'
			self.levelmap[19:22, self.randx + 2:self.randx + 5:2] = '['

		self.randnum = random.randint(0,2)
		self.randx += 6

		if(self.randnum < 1):
			self.levelmap[19:22, self.randx:self.randx + 6:5] = '|'
			self.levelmap[19:22, self.randx + 1:self.randx + 4:2] = ']'
			self.levelmap[19:22, self.randx + 2:self.randx + 5:2] = '['

		self.randnum = random.randint(0,2)
		self.randx += 6

		if(self.randnum < 1):
			self.levelmap[19:22, self.randx:self.randx + 6:5] = '|'
			self.levelmap[19:22, self.randx + 1:self.randx + 4:2] = ']'
			self.levelmap[19:22, self.randx + 2:self.randx + 5:2] = '['

		#generating gaps with stop points#
		self.randx = random.randint(165, 176)

		self.levelmap[24, self.randx:self.randx + 7] = 'w'
		self.levelmap[25:31, self.randx:self.randx + 7:2] = '|'
		self.levelmap[25:31, self.randx + 1:self.randx + 6:2] = '-'
		
		self.levelmap[25:32, self.randx + 7:self.randx + 22] = ' '

		self.levelmap[24, self.randx + 22:self.randx + 29] = 'w'
		self.levelmap[25:31, self.randx + 22:self.randx + 29:2] = '|'
		self.levelmap[25:31, self.randx + 23:self.randx + 28:2] = '-'


		self.randx = random.randint(310, 326)

		self.levelmap[24, self.randx:self.randx + 7] = 'w'
		self.levelmap[25:31, self.randx:self.randx + 7:2] = '|'
		self.levelmap[25:31, self.randx + 1:self.randx + 6:2] = '-'
		
		self.levelmap[25:32, self.randx + 7:self.randx + 22] = ' '

		self.levelmap[24, self.randx + 22:self.randx + 29] = 'w'
		self.levelmap[25:31, self.randx + 22:self.randx + 29:2] = '|'
		self.levelmap[25:31, self.randx + 23:self.randx + 28:2] = '-'
		
		
		#generating cliffs#
		self.randx = random.randint (210, 215)

		self.levelmap[15:30, self.randx:self.randx + 30] = 'X'
		self.levelmap[15:30, self.randx] = '|'
		self.levelmap[15:30, self.randx + 5] = '|'
		self.levelmap[15:30, self.randx + 6] = '|'
		self.levelmap[15:30, self.randx + 11] = '|'
		self.levelmap[15:30, self.randx + 12] = '|'
		self.levelmap[15:30, self.randx + 17] = '|'
		self.levelmap[15:30, self.randx + 18] = '|'
		self.levelmap[15:30, self.randx + 23] = '|'
		self.levelmap[15:30, self.randx + 24] = '|'
		self.levelmap[15:30, self.randx + 29] = '|'

		self.levelmap[15:18, self.randx:self.randx + 24] = ' '
		self.levelmap[18:21, self.randx:self.randx + 18] = ' '
		self.levelmap[21:24, self.randx:self.randx + 12] = ' '
		self.levelmap[24:27, self.randx:self.randx + 6] = ' '

		self.randnum = random.randint(27, 34)

		self.levelmap[29:32, self.randx + 30:self.randx + 30 + self.randnum] = ' '		
		
		#generating clouds#
		self.randx = 0

		while(self.randx < 500):
			self.levelmap[3, self.randx + 5:self.randx + 10] = '/'
			self.levelmap[4, self.randx + 1:self.randx + 11] = '/'
			self.levelmap[5, self.randx + 1:self.randx + 7] = '/'

			self.levelmap[1, self.randx + 25:self.randx + 34] = '/'
			self.levelmap[2:4, self.randx + 21:self.randx + 37] = '/'
			self.levelmap[4, self.randx + 21:self.randx + 31] = '/'

			self.levelmap[3:6:2, self.randx + 53:self.randx + 61] = '/'
			self.levelmap[4, self.randx + 49:self.randx + 67] = '/'

			self.levelmap[1, self.randx + 81:self.randx + 86] = '/'
			self.levelmap[2, self.randx + 77:self.randx + 87] = '/'
			self.levelmap[3, self.randx + 73:self.randx + 88] = '/'
			self.levelmap[4, self.randx + 77:self.randx + 85] = '/'

			self.randx += 100


		#generating victory platform#
		self.randx = 400

		self.levelmap[29:32, self.randx-8:self.randx] = ' '
		self.levelmap[29:32, self.randx:self.randx + 33] = '#'
		self.levelmap[26:29, self.randx + 8:self.randx + 25] = '#'
		self.levelmap[8:27, self.randx + 16] = '|'

		self.levelmap[9, self.randx + 12:self.randx + 16] = '-'
		self.levelmap[12, self.randx + 12:self.randx + 16] = '-'
		self.levelmap[14, self.randx + 14:self.randx + 17] = '-'

		self.levelmap[9, self.randx + 11] = '/'
		self.levelmap[10, self.randx + 10] = '/'
		self.levelmap[11, self.randx + 10] = '\\'
		self.levelmap[12, self.randx + 11] = '\\'
		self.levelmap[13, self.randx + 12] = '\\'
		self.levelmap[14, self.randx + 13] = '\\'

		self.levelmap[29:32, self.randx + 33:] = ' '