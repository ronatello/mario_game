"""Handling objects in game"""

class Coin():

	def __init__(self, x, y, board):

		self.x = x
		self.y = y
		self.length = 1
		self.width = 1
		self.sprite = [['0']]
		self.spawn = 0

	def spawn(self, board):
		if(display.y + 95 > self.y and self.spawn == 0):
			board.drawonBoard(self, self.x, self.y)
			self.spawn = 1
