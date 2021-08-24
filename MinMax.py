import copy
from Connect4 import Connect4

from Connect4States import Connect4States
from Connect4Colors import Connect4Colors
from Connect4Pieces import Connect4Pieces

class MinMax:
	"""MinMax algorithm for Connect 4
	Positive score means Yellow is winning
	Negative score means Red is winning"""

	MIN = 0
	MAX = 1

	def __init__(self):
		pass

	def __evaluateBoard(self, game):
		#We check if the game is won, in this case the result is trivial
		if game.state == Connect4States.YELLOW_WIN:
			return 10000 

		if game.state == Connect4States.RED_WIN:
			return -10000 

		#We evaluate the game based on three characteristics

		#First, how many pieces we have in the center
		centerPieces = self.__countPiecesInCenter(game)

		#Second, how many combo of 3 pieces with one empty space at the end we have
		combosOf2 = self.__countCombosOfPiecesWithEmptySpace(game, 2, Connect4Pieces.YELLOW_PIECE.value) - self.__countCombosOfPiecesWithEmptySpace(game, 2, Connect4Pieces.RED_PIECE.value)

		#Third, how many combo of 2 pieces with one empty space at the end we have
		combosOf3 = self.__countCombosOfPiecesWithEmptySpace(game, 3, Connect4Pieces.YELLOW_PIECE.value) - self.__countCombosOfPiecesWithEmptySpace(game, 3, Connect4Pieces.RED_PIECE.value)

		#Fourth, how many "7" traps we have
		#Fifth, how many "double line" traps we have

		return centerPieces + combosOf2 + combosOf3

	def __countPiecesInCenter(self, game):
		count = 0
		for i in range(Connect4.HEIGHT):
			if game.grid[i, 3] == Connect4Pieces.YELLOW_PIECE.value:
				count += 1

			if game.grid[i, 3] == Connect4Pieces.RED_PIECE.value:
				count -= 1

		return count

	def __countCombosOfPiecesWithEmptySpace(self, game, consecutive, color):
		count = 0

		for x in range(Connect4.WIDTH):
			for y in range(Connect4.HEIGHT):

				#Check for row connect 4
				if x + (consecutive + 1) < Connect4.WIDTH:
					count =+ int(self.__checkConsecutivePiecesWithEmptySpace(game, x, y, 1, 0, color, consecutive))

				#Check for column connect 4
				if y + (consecutive + 1) < Connect4.HEIGHT:
					count =+ int(self.__checkConsecutivePiecesWithEmptySpace(game, x, y, 0, 1, color, consecutive))

				#Check for (1;1) diagonal connect 4
				if x + (consecutive + 1) < Connect4.WIDTH and y + (consecutive + 1) < Connect4.HEIGHT:
					count =+ int(self.__checkConsecutivePiecesWithEmptySpace(game, x, y, 1, 1, color, consecutive))

				#Check for (1;-1) diagonal connect 4
				if x + (consecutive + 1) < Connect4.WIDTH and y - (consecutive + 1) > -1:
					count =+ int(self.__checkConsecutivePiecesWithEmptySpace(game, x, y, 1, -1, color, consecutive))

		return count

	def __checkConsecutivePiecesWithEmptySpace(self, game, ox, oy, dx, dy, color, consecutive):
		consecutivePieces = 0

		for i in range(consecutive):
			if game.grid[oy + dy * i, ox + dx * i] == color:
				consecutivePieces += 1
			else:
				consecutivePieces = 0

		if consecutivePieces == consecutive and game.grid[ox + dx * (consecutive + 1), oy + dy * (consecutive + 1)] == Connect4Pieces.EMPTY.value:
			return True
		else:
			return False


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
			return self.__evaluateBoard(game)

		if player == MinMax.MAX: #MAX because we want the maximum scoare for our color
			scoreChildren = [self.MinMaxAlgorithm(gameChildren[i], depth - 1, MinMax.MIN) for i in range(len(gameChildren))]
			return max(scoreChildren)

		else:
			scoreChildren = [self.MinMaxAlgorithm(gameChildren[i], depth - 1, MinMax.MAX) for i in range(len(gameChildren))]
			return min(scoreChildren)