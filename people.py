import os
import sys
import subprocess

"""Handling all entities that can perform actions"""

class Person:
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.length = 0
		self.width = 0
		self.gravityon = 1
		self.jump_height = 0

	def changePosition(self, x, y):
		self.x = x
		self.y = y

	def moveLeft(self, board, level):
		collisionret, pos = board.collision(self, self.x, self.y - 1, -1)
		if self.y != 0 and collisionret == 0:
			board.eraseBoard(self, level, -1)
			board.drawonBoard(self, self.x, self.y - 1)
			self.changePosition(self.x, self.y - 1)
			return collisionret, pos
		else:
			board.drawonBoard(self, self.x, self.y)
			return collisionret, pos

	def moveRight(self, board, level):
		collisionret, pos = board.collision(self, self.x, self.y, 1)
		if collisionret == 0 or collisionret == 5:
			board.eraseBoard(self, level, 1)
			board.drawonBoard(self, self.x, self.y + 1)
			self.changePosition(self.x, self.y + 1)
			return collisionret, pos
		else:
			board.drawonBoard(self, self.x, self.y)
			return collisionret, pos

	def Ascend(self, board, level):
		collisionret, pos = board.collision(self, self.x - 1, self.y, 0)
		if collisionret == 0 or collisionret == 5:
			board.eraseBoard(self, level, 0)
			board.drawonBoard(self, self.x - 1, self.y)
			self.changePosition(self.x - 1, self.y)
			return collisionret, pos
		else:
			board.drawonBoard(self, self.x, self.y)
			return collisionret, pos

	def Descend(self, board, level):
		collisionret, pos = board.gravitycollision(self, self.x, self.y)
		if collisionret == 0 or collisionret == 5:
			board.eraseBoard(self, level, 2)
			board.drawonBoard(self, self.x + 1, self.y)
			self.changePosition(self.x + 1, self.y)
			return collisionret, pos

		else:
			board.drawonBoard(self, self.x, self.y)
			return collisionret, pos


class Mario(Person):

	def __init__(self, x, y, board):
		Person.__init__(self, x, y)
		self.sprite = [[' ', 'O', 'O', ' '], ['I', '|', '|', 'I'], ['_', '|', '|', '_']]
		self.length = 3
		self.width = 4
		self.score = 0
		self.deathstate = 0
		self.pos = 0

		board.drawonBoard(self, self.x, self.y)

	def movement(self, input, board, level, coins, music):
		
		if input == 'a':
			self.deathstate, self.pos = Person.moveLeft(self, board, level)
			if(self.deathstate == 5):
				self.death(coins, board, music)

		if input == 'd':
			self.deathstate, self.pos = Person.moveRight(self, board, level)
			if(self.deathstate == 5):
				self.death(coins, board, music)

		if input == 'w':
			if self.gravityon == 1:
				subprocess.Popen(["aplay", "-q", "./jump.wav"])
				self.gravityon = 0
			else:
				pass
		else:
			pass

	def death(self, coins, board, music):
		
		if self.deathstate == 3:
			print("Game Over")
			subprocess.Popen(["aplay", "-q", "./death.wav"])
			music.kill()
			sys.exit()

		elif self.deathstate == 5:
			if coins:
				for coin in coins:
					if coin.y == self.pos:
						subprocess.Popen(["aplay", "-q", "./coin.wav"])
						self.score += 100
						coin.sprite = [[' ']]
						board.drawonBoard(coin, coin.x, coin.y)
						coins.remove(coin)
					

		if self.x == 29:
			print("Game Over")
			subprocess.Popen(["aplay", "-q", "./death.wav"])
			music.kill()
			sys.exit()
			

	def playercamera(self, board, level):
		
		if self.y >= 47:
			self.changePosition(self.x, self.y - 1)
			board.moveBoard(level)
			board.drawonBoard(self, self.x, self.y)
			return 1

		elif self.y < 0:
			self.changePosition(self.x, 0)
			board.drawonBoard(self, self.x, self.y)
			return -1

		else:
			return 0


class EnemyShroom(Person):
	
	def __init__(self, x, y, board, level, flag):
		
		Person.__init__(self, x, y)
		self.sprite = [[' ', '_', '_', ' '], ['<', '^', '^', '>'], [' ', 'd', 'b', ' ']]
		self.length = 3
		self.width = 4
		self.flag = flag
		self.life = 1
		self.spawn = 0
		self.movestateL = 0
		self.movestateR = 0
		self.deviation = 0

	def death(self, board):
		self.sprite = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
		board.drawonBoard(self, self.x, self.y)
		self.spawn = 0

	def movement(self, board, level, mario, coins, music):
		if self.life > 0:
			if self.flag == 1:
				if(self.movestateR != 1):
					self.movestateL = 0
					self.movestateR, self.pos = Person.moveRight(self, board, level)

					if(self.movestateR == 2):
						mario.deathstate = 3
						mario.death(coins, board, music)

					self.deviation += 1


					if (self.deviation > 30):
						self.movestateR = 1

				elif (self.movestateR == 1):
					self.movestateL, self.pos = Person.moveLeft(self, board, level)

					if(self.movestateL == 2):
						mario.deathstate = 3
						mario.death(coins, board, music)

					self.deviation -= 1

					if(self.deviation < -30):
						self.movestateL = 1

					if (self.movestateL == 1):
						self.movestateR = 0

			else:
				if(self.movestateL != 1):
					self.movestateR = 0
					self.movestateL, self.pos = Person.moveLeft(self, board, level)
					if (self.movestateL == 2):
						mario.deathstate = 3
						mario.death(coins, board, music)

					self.deviation -= 1

					if (self.deviation < -30):
						self.movestateL = 1

				elif (self.movestateL == 1):
					self.movestateR, self.pos = Person.moveRight(self, board, level)

					if (self.movestateR == 2):
						mario.deathstate = 3
						mario.death(coins, board, music)

					self.deviation += 1

					if(self.deviation > 30):
						self.movestateR = 1

					if (self.movestateR == 1):
						self.movestateL = 0