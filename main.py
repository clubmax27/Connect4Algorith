import pygame
import math
import sys
import time

import Connect4
from Connect4States import Connect4States
from Connect4Colors import Connect4Colors

from MinMax import MinMax
from AlphaBeta import AlphaBeta
from EvaluateBoard import EvaluateBoard

from GUI import LoadGUI, handleMouseMotion, drawBoard, handleGameVictory
from GUIConsts import GUIConsts


def main():

	DEPTH = 5
	PLAYER_STARTING = False

	game = Connect4.Connect4(Connect4Colors.YELLOW)
	screen = LoadGUI(game.grid)

	if not PLAYER_STARTING:
		player = Connect4Colors.YELLOW.value if (game.state == Connect4States.YELLOW_TURN) else Connect4Colors.RED.value

		start = time.time()
		column, score = AlphaBeta.AlphaBetaAlgorithm(game, DEPTH, player, -math.inf, math.inf)
		end = time.time()
		print("Time for the Alpha Beta algorith : {0}".format(end - start))
		print("Score : {0}".format(score))
		print("Number of grid evaluated : {0}".format(AlphaBeta.numberOfEvaluations))
		print("-------------------------------------------------")

		game.playMove(column)
		drawBoard(game.grid, screen)
		print(game.state)

	if game.isGameOver():
		handleGameVictory(screen, game)

	while game.state != Connect4States.RED_WIN or game.state != Connect4States.YELLOW_WIN:

		for event in pygame.event.get(): 
			if game.state == Connect4States.RED_WIN or game.state == Connect4States.YELLOW_WIN:
				break

			if event.type == pygame.QUIT: #If user quits GUI
				sys.exit()

			if event.type == pygame.MOUSEMOTION: #If user moves mouse
				handleMouseMotion(event, screen, game)
			pygame.display.update()

			if event.type == pygame.MOUSEBUTTONDOWN:
				pygame.draw.rect(screen, GUIConsts.BLACK.value, (0,0, GUIConsts.width.value, GUIConsts.SQUARESIZE.value))

				posx = event.pos[0]
				column = int(math.floor(posx/GUIConsts.SQUARESIZE.value))

				if game.isValidLocation(column):
					game.playMove(column)

					if game.isGameOver():
						handleGameVictory(screen, game)
					else: #If game is not finished, we make the bot play

						player = Connect4Colors.YELLOW.value if (game.state == Connect4States.YELLOW_TURN) else Connect4Colors.RED.value

						"""start = time.time()
						column, score = MinMax.MinMaxAlgorithm(game, DEPTH, player)
						end = time.time()
						print("Time for the Min Max algorith : {0}".format(end - start))"""

						#MemoizedAlphaBeta = Memoize.Memoize(AlphaBeta.AlphaBetaAlgorithm)

						start = time.time()
						column, score = AlphaBeta.AlphaBetaAlgorithm(game, DEPTH, player, -math.inf, math.inf)
						end = time.time()
						print("Time for the Alpha Beta algorith : {0}".format(end - start))
						print("Score : {0}".format(score))
						print("Number of grid evaluated : {0}".format(AlphaBeta.numberOfEvaluations))
						print("-------------------------------------------------")

						game.playMove(column)

						print(game.state)

						if game.isGameOver():
							handleGameVictory(screen, game)

				drawBoard(game.grid, screen)


	

	"""
		game.printGrid()
		column = int(input("what column to play in ? (1 - 7)"))
		game.playMove(column - 1)

		player = Connect4Colors.RED.value
		if game.state == Connect4States.YELLOW_TURN:
			player = Connect4Colors.YELLOW.value

		column, score = ai.MinMaxAlgorithm(game, 4, player)
		print("Current score : {0}".format(score))
		print("Best column : {0}".format(column + 1))
		if score == 10000:
			print("Yellow can only win")

		if score == -10000:
			print("Red can only win")"""

if __name__=="__main__":
   main()