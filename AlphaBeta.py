import copy
import math
import time

from Connect4 import Connect4
from Connect4States import Connect4States
from Connect4Colors import Connect4Colors
from Connect4Pieces import Connect4Pieces

from EvaluateBoard import EvaluateBoard

from Memoize import Memoize

class AlphaBeta:
	"""MinMax algorithm for Connect 4
	Positive score means Yellow is winning
	Negative score means Red is winning"""

	numberOfEvaluations = 0


	MIN = 0
	MAX = 1

	def __init__(self):
		pass

	#@Memoize
	def __possibleMoves(game):
		ListOfPossibleMoves = []
		ListOfPossibleGames = []
		if game.state == Connect4States.RED_WIN or game.state == Connect4States.YELLOW_WIN: #If game has ended, not further move are possible
			return ListOfPossibleMoves, ListOfPossibleGames

		for i in range(Connect4.WIDTH): #For every column
			NewGame = copy.deepcopy(game)
			if NewGame.grid[Connect4.HEIGHT - 1, i] == 0: #If move is playable
				NewGame.playMove(i)
				ListOfPossibleMoves.append(i)
				ListOfPossibleGames.append(NewGame)

		return ListOfPossibleMoves, ListOfPossibleGames


	def AlphaBetaAlgorithm(game, depth, player, alpha, beta):
		possibleMoves, gameChildren = AlphaBeta.__possibleMoves(game)

		if depth == 0 or len(gameChildren) == 0:
			AlphaBeta.numberOfEvaluations += 1
			return (None, EvaluateBoard(game))

		if player == AlphaBeta.MAX: #MAX because we want the maximum score for our color
			bestScore = -math.inf
			i = -1

			for possibleGame in gameChildren:
				i += 1

				scoreChild = AlphaBeta.AlphaBetaAlgorithm(possibleGame, depth - 1, AlphaBeta.MIN, alpha, beta)[1]

				if scoreChild > bestScore:
					bestScore = scoreChild
					column = possibleMoves[i]
				alpha = max(alpha, bestScore)
				if beta <= alpha:
					break

			return column, bestScore

		else:
			bestScore = math.inf
			i = -1

			for possibleGame in gameChildren:
				i += 1

				scoreChild = AlphaBeta.AlphaBetaAlgorithm(possibleGame, depth - 1, AlphaBeta.MAX, alpha, beta)[1]

				if scoreChild < bestScore:
					bestScore = scoreChild
					column = possibleMoves[i]
				beta = min(beta, bestScore)
				if beta <= alpha:
					break


			return column, bestScore
	"""
	def score_position(board, piece):
		start = time.time()
		score = 0
		COLUMN_COUNT = 7
		ROW_COUNT = 6

		WINDOW_LENGTH = 4

		## Score center column
		center_array = [int(i) for i in list(board[:, COLUMN_COUNT//2])]
		center_count = center_array.count(piece)
		score += center_count * 3

		## Score Horizontal
		for r in range(ROW_COUNT):
			row_array = [int(i) for i in list(board[r,:])]
			for c in range(COLUMN_COUNT-3):
				window = row_array[c:c+WINDOW_LENGTH]
				score += AlphaBeta.evaluate_window(window, piece)

		## Score Vertical
		for c in range(COLUMN_COUNT):
			col_array = [int(i) for i in list(board[:,c])]
			for r in range(ROW_COUNT-3):
				window = col_array[r:r+WINDOW_LENGTH]
				score += AlphaBeta.evaluate_window(window, piece)

		## Score posiive sloped diagonal
		for r in range(ROW_COUNT-3):
			for c in range(COLUMN_COUNT-3):
				window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]
				score += AlphaBeta.evaluate_window(window, piece)

		for r in range(ROW_COUNT-3):
			for c in range(COLUMN_COUNT-3):
				window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
				score += AlphaBeta.evaluate_window(window, piece)

		print("Time for the Eval function : {0}".format(time.time() - start))

		return score

	def evaluate_window(window, piece):
		score = 0
		EMPTY = 0
		piece = 1
		opp_piece = 2

		if window.count(piece) == 4:
			score += 100
		elif window.count(piece) == 3 and window.count(EMPTY) == 1:
			score += 5
		elif window.count(piece) == 2 and window.count(EMPTY) == 2:
			score += 2

		if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
			score -= 4

		return score"""