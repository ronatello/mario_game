import sys


"""Code to handle drawing of board on terminal"""

class Board:
	
	def __init__(self, length, width, level):
		
		"""Board object initializing"""
		
		self.board = []
		self.x = 0
		self.y = 0
		self.length = length
		self.width = width

		#Starting off entire board with only spaces#

		for i in range(0, self.length):
			self.board.append([])
			for j in range(0, self.width):
				self.board[i].append(level[i][j])

	def getString(self):

		"""Function to turn Board Matrix to printable string"""
		
		boardString = ""

		for i in range(0, self.length):
			for j in range(0, self.width):
				boardString += self.board[i][j]
			boardString += '\n'

		return boardString

	def collision(self, entity, newx, newy, flag): 
		
		"""Function to detect collisions for desired movement"""

		if (flag == 1):
			for i in range(newx, newx + entity.length):
				if newy + entity.width == 95:
					return 1, 1
				elif self.board[i][newy + entity.width] == '<' or self.board[i][newy + entity.width] == '>':
					return 3, 1
				elif self.board[i][newy + entity.width] == 'I' :
					return 2, 1
				elif self.board[i][newy + entity.width] == '0':
					return 5, newy + entity.width
				elif self.board[i][newy + entity.width] != ' ' and self.board[i][newy + entity.width] != '/':
					return 1, 1

		elif (flag == -1):
			for i in range(newx, newx + entity.length):
				if self.board[i][newy] == '<' or self.board[i][newy] == '>':
					return 3, 1
				elif self.board[i][newy] == 'I':
					return 2, 1
				elif self.board[i][newy] == '0':
					return 5, newy
				elif self.board[i][newy] != ' ' and self.board[i][newy] != '/':
					return 1, 1

		elif (flag == 0):
			for j in range(newy, newy + entity.width):
				if self.board[newx][j] == '<' or self.board[newx][j] == '>':
					return 3, 1
				elif self.board[newx][j] == 'I':
					return 2, 1
				elif self.board[newx][j] == '0':
					return 5, j
				elif self.board[newx][j] != ' ' and self.board[newx][j] != '/':
					return 1, 1
		
		return 0, 1


	def gravitycollision(self, entity, x, y):
		
		"""Function to detect collisions based on gravity"""

		for j in range(y, y + entity.width):
			if self.board[x + entity.length][j] == '_':
				return 2,j
			elif self.board[x + entity.length][j] == '#':
				return 4,j
			elif self.board[x + entity.length][j] == '0':
				return 5,j
			elif self.board[x + entity.length][j] != ' ' and self.board[x + entity.length][j] != '/':
				return 1,j
		
		return 0,j


	def drawonBoard(self, entity, x, y):

		"""Function to draw sprites on Board and update the Board"""

		#temporary matrix used to handle redraw function until completely drawn matrix is returned to Board Matrix#
		tempmatrix = self.board
		
		a = 0
		b = 0
		
		for i in range(x, x + entity.length):
			for j in range(y, y + entity.width):
				tempmatrix[i][j] = entity.sprite[a][b]
				b += 1
			a += 1
			b = 0

		self.board = tempmatrix


	def moveBoard(self, level):
		
		self.y += 1
		for i in range(0, 32):
			for j in range(0, 96):
				self.board[i][j] = level.levelmap[self.x + i][self.y + j]


	def eraseBoard(self, entity, level, flag):

		if (flag == 1):
			for i in range (entity.x, entity.x + entity.length):
				self.board[i][entity.y] = level[self.x + i][self.y + entity.y]

		elif (flag == -1):
			for i in range (entity.x, entity.x + entity.length):
				self.board[i][entity.y + entity.width - 1] = level[self.x + i][self.y + entity.y + entity.width - 1]

		elif (flag == 0):
			for j in range (entity.y, entity.y + entity.width):
				self.board[entity.x + entity.length - 1][j] = level[self.x + entity.x + entity.length - 1][self.y + j]

		elif (flag == 2):
			for j in range (entity.y, entity.y + entity.width):
				self.board[entity.x][j] = level[self.x + entity.x][self.y + j]