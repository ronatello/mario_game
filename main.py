
"""Main driver program"""

import os
import sys
from board import Board
from people import Mario, EnemyShroom
from objects import Coin
from input import Get, input_to
from map import gameMap
import subprocess
from colorama import Fore, Back, Style

def main():

	music = subprocess.Popen(["aplay", "-q", "./main.wav"])
	level = gameMap()
	display = Board(32, 96, level.levelmap)
	mario = Mario(26, 10, display)
	enemy = []
	enemy.append(EnemyShroom(26, 30, display, level.levelmap, -1))
	enemy.append(EnemyShroom(26, 140, display, level.levelmap, -1))

	enemy.append(EnemyShroom(26, 300, display, level.levelmap, 1))
	enemy.append(EnemyShroom(26, 305, display, level.levelmap, -1))

	coins = []
	coins.append(Coin(17, 30, display))
	coins.append(Coin(17, 34, display))
	coins.append(Coin(17, 38, display))
	coins.append(Coin(17, 42, display))
	coins.append(Coin(17, 140, display))
	coins.append(Coin(17, 142, display))
	coins.append(Coin(17, 144, display))
	coins.append(Coin(17, 146, display))
	coins.append(Coin(14, 200, display))
	coins.append(Coin(17, 210, display))
	coins.append(Coin(17, 300, display))
	coins.append(Coin(17, 305, display))
	getch = Get()
	
	gameloop = True
	os.system('clear')
	print(display.getString())

	while gameloop == True:

		mario.death(coins, display, music)
		cam = mario.playercamera(display, level)
		if cam == 1:
			mario.score += 5
		if coins:
			for coin in coins:
				if(display.y + 95 > coin.y and coin.spawn == 0):
					coin.y = coin.y - display.y
					display.drawonBoard(coin, coin.x, coin.y)
					coin.spawn = 1
				
				elif(coin.spawn == 1):
					if cam == 1:
						coin.y -= 1
						display.drawonBoard(coin, coin.x, coin.y)

					if (coin.y == 0):
						coin.sprite = [[' ']]
						display.drawonBoard(coin, coin.x, coin.y)
						coins.remove(coin)
		if enemy:
			for monster in enemy:
				if(display.y + 95 > monster.y + monster.width and monster.spawn == 0):
					monster.y = monster.y - display.y
					display.drawonBoard(monster, monster.x, monster.y)
					monster.spawn = 1

				elif(monster.spawn == 1):
					if cam == 1:
						monster.y -= 1
					monster.movement(display, level.levelmap, mario, coins, music)
					if (monster.y == 0):
						monster.life = 0
						monster.death(display)
						enemy.remove(monster)

		inp = input_to(getch)
		os.system('clear')

		if mario.gravityon == -1 or mario.gravityon == 1:
			fallstate, pos = mario.Descend(display, level.levelmap)
			
			if (fallstate == 1):
				mario.gravityon = 1

			elif (fallstate == 2):
				min = 0
				minval = pos + 10
				if enemy:
					for monster in enemy:
						if(monster.y + 1 < minval):
							minval = monster.y + 1
							min = monster
					subprocess.Popen(["aplay", "-q", "./kill.wav"])
					min.life -= 1
					if (min.life <= 0):
						min.death(display)
						mario.score += 200
						enemy.remove(min)
						mario.gravityon = 0
						mario.jump_height = 7
			
			elif (fallstate == 5):
				if coins:
					for coin in coins:
						if(coin.y == pos):
							subprocess.Popen(["aplay", "-q", "./coin.wav"])
							mario.score += 100
							coin.sprite = [[' ']]
							display.drawonBoard(coin, coin.x, coin.y)
							coins.remove(coin)
			elif (fallstate == 4):
				music.kill()
				subprocess.Popen(["aplay", "-q", "./win.wav"])
				mario.score += 2000
				print("Stage Clear!")
				print("Score: " + str(mario.score))
				sys.exit()
		
		elif mario.gravityon == 0:
			if mario.jump_height < 12:
				mario.jump_height += 1
				fallstate, pos = mario.Ascend(display, level.levelmap)
				if (fallstate == 1):
					mario.gravityon = -1
				elif (fallstate == 5):
					if coins:
						for coin in coins:
							if coin.y == pos:
								subprocess.Popen(["aplay", "-q", "./coin.wav"])
								mario.score += 100
								coin.sprite = [[' ']]
								display.drawonBoard(coin, coin.x, coin.y)
								coins.remove(coin)

			if mario.jump_height == 12:
				mario.jump_height = 0
				mario.gravityon = -1

		print(Fore.GREEN + Style.BRIGHT + display.getString())
		print("Score: " + str(mario.score))
		if inp == 'q':
			os.system('clear')
			music.kill()
			sys.exit()
		
		if inp is not None:
			mario.movement(inp, display, level.levelmap, coins, music)


main()
