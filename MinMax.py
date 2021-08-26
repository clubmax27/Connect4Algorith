import copy
from Connect4 import Connect4

from Connect4States import Connect4States
from Connect4Colors import Connect4Colors
from Connect4Pieces import Connect4Pieces

from EvaluateBoard import EvaluateBoard

class MinMax:
	"""MinMax algorithm for Connect 4
	Positive score means Yellow is winning
	Negative score means Red is winning"""

	MIN = 0
	MAX = 1

	def __init__(self):
		pass


	def __possibleMoves(self, game):
		ListOfPossibleMoves = []
		if game.state == Connect4States.RED_WIN or game.state == Connect4States.YELLOW_WIN: #If game has ended, not further move are possible
			return ListOfPossibleMoves

		for i in range(Connect4.WIDTH): #For every column
			NewGame = copy.deepcopy(game)
			if NewGame.grid[Connect4.HEIGHT - 1, i] == 0: #If move is playable
				NewGame.playMove(i)
				ListOfPossibleMoves.append(NewGame)

		return ListOfPossibleMoves



	def MinMaxAlgorithm(self, game, depth, player):
		gameChildren = self.__possibleMoves(game)

		if depth == 0 or len(gameChildren) == 0:
			return EvaluateBoard(game)

		if player == MinMax.MAX: #MAX because we want the maximum score for our color
			scoreChildren = [self.MinMaxAlgorithm(gameChildren[i], depth - 1, MinMax.MIN) for i in range(len(gameChildren))]
			return max(scoreChildren)

		else:
			scoreChildren = [self.MinMaxAlgorithm(gameChildren[i], depth - 1, MinMax.MAX) for i in range(len(gameChildren))]
			return min(scoreChildren)