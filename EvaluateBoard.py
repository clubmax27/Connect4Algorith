import time
import numpy as np

from Connect4 import Connect4

from Connect4States import Connect4States
from Connect4Colors import Connect4Colors
from Connect4Pieces import Connect4Pieces

from Memoize import Memoize

"""Function to evaluate the score of a board
Positive score means Yellow is winning
Negative score means Red is winning"""

@Memoize
def EvaluateBoard(game):

	centerPiecesCoef = 3
	combosOf2Coef = 2
	combosOf3Coef = 5
	multipleThreatsCoef = 100

	#We check if the game is won, in this case the result is trivial
	if game.state == Connect4States.YELLOW_WIN:
		return 10000

	if game.state == Connect4States.RED_WIN:
		return -10000 

	if game.state == Connect4States.STALEMATE:
		return 0 
	
	start = time.time()
	#We evaluate the game based on three characteristics
	
	#First, how many pieces we have in the center
	centerPieces = __countPiecesInCenter(game)
	
	#Second, how many combo of 3 pieces with one empty space at the end we have
	combosOf2 = __countCombosOfPiecesWithEmptySpace(game, 2, Connect4Pieces.YELLOW_PIECE.value)

	#Third, how many combo of 2 pieces with one empty space at the end we have
	combosOf3 = __countCombosOfPiecesWithEmptySpace(game, 3, Connect4Pieces.YELLOW_PIECE.value)

	#Fourth, how many multiple threats ("7" traps and double lines) we have
	#multipleThreats = __countCombosOfMultipleThreats(game, 3, Connect4Pieces.YELLOW_PIECE.value) - __countCombosOfMultipleThreats(game, 3, Connect4Pieces.YELLOW_PIECE.value)
	
	#Fifth, instant double line, is handled by the depth of MinMax

	"""
	print("Score for pieces in the center : {0}".format(centerPieces * centerPiecesCoef))
	print("Score for combos of 2 : {0}".format(combosOf2 * combosOf2Coef))
	print("Score for combos of 3 : {0}".format(combosOf3 * combosOf3Coef))
	#print("Score for multiple threats : {0}".format(multipleThreats * multipleThreatsCoef))"""

	print("Time for the Eval function : {0}".format(time.time() - start))
	return centerPieces * centerPiecesCoef + \
		   combosOf2 * combosOf2Coef + \
		   combosOf3 * combosOf3Coef# + \
		   #multipleThreats * multipleThreatsCoef"""


def __countPiecesInCenter(game):
	count = 0
	for i in range(Connect4.HEIGHT):
		if game.grid[i, 3] == Connect4Pieces.YELLOW_PIECE.value:
			count += 1

		if game.grid[i, 3] == Connect4Pieces.RED_PIECE.value:
			count -= 1

	return count

def __countCombosOfMultipleThreats(game, consecutive, color):
	count = 0

	for x in range(Connect4.WIDTH):
		isMultipleThreatPresentInColumn = False

		for y in range(Connect4.HEIGHT - 1):
			if (not isMultipleThreatPresentInColumn) and (__countCombosOfPiecesAroundEmptySpace(game, x, y, consecutive, color) and __countCombosOfPiecesAroundEmptySpace(game, x, y + 1, consecutive, color)):	
				isMultipleThreatPresentInColumn = True

		if isMultipleThreatPresentInColumn:
			count += 1

	return count

def __countCombosOfPiecesWithEmptySpace(game, consecutive, color):
	count = 0

	#Check for (1;0) row connect 4
	for x in range(Connect4.WIDTH - 3):
		for y in range(Connect4.HEIGHT):
			extract = game.grid[y, x:(x + consecutive)]
			count =+ __checkCombosOfPiecesInExtract(extract, color, consecutive)

	#Check for (0;1) column connect 4
	for x in range(Connect4.WIDTH):
		for y in range(Connect4.HEIGHT - 3):
			extract = game.grid[y:(y + consecutive), x]
			count =+ __checkCombosOfPiecesInExtract(extract, color, consecutive)

	#Check for (1;1) diagonal connect 4
	for x in range(Connect4.WIDTH - 3):
		for y in range(Connect4.HEIGHT - 3):
			extract = [game.grid[y + i, x + i] for i in range(Connect4.CONSECUTIVE)]
			count =+ __checkCombosOfPiecesInExtract(extract, color, consecutive)

	#Check for (1;-1) diagonal connect 4
	for x in range(Connect4.WIDTH - 3):
		for y in range(3, Connect4.HEIGHT):
			extract = [game.grid[y - i, x + i] for i in range(Connect4.CONSECUTIVE)]
			count =+ __checkCombosOfPiecesInExtract(extract, color, consecutive)

	return count

"""
def __countCombosOfPiecesAroundEmptySpace(game, x, y, consecutive, color):
	count = 0

	#Check for (1;0) row connect 4
	if x + Connect4.CONSECUTIVE < Connect4.WIDTH:
		extract = game.grid[y, x:(x + consecutive)]
		count =+ __checkCombosOfPiecesInExtract(extract, color, consecutive)


	#Check for (0;1) column connect 4
	if y + Connect4.CONSECUTIVE < Connect4.HEIGHT:
		extract = game.grid[y:(y + consecutive), x]
		count =+ __checkCombosOfPiecesInExtract(extract, color, consecutive)


	#Check for (1;1) diagonal connect 4
	if x + Connect4.CONSECUTIVE < Connect4.WIDTH and y + Connect4.CONSECUTIVE < Connect4.HEIGHT:
		extract = [game.grid[y + i, x + i] for i in range(Connect4.CONSECUTIVE)]
		count =+ __checkCombosOfPiecesInExtract(extract, color, consecutive)


	#Check for (1;-1) diagonal connect 4
	if x + Connect4.CONSECUTIVE < Connect4.WIDTH and y - Connect4.CONSECUTIVE >= 0:
		extract = [game.grid[y - i, x + i] for i in range(Connect4.CONSECUTIVE)]
		count =+ __checkCombosOfPiecesInExtract(extract, color, consecutive)

	return count"""

def __checkCombosOfPiecesInExtract(extract, color, consecutive):

	emptySpaces = np.count_nonzero(extract == Connect4Pieces.EMPTY.value)
	piecesOfColor = np.count_nonzero(extract == color)

	if emptySpaces + piecesOfColor != Connect4.CONSECUTIVE: #If there is a piece of opposite color
		return 0

	if piecesOfColor == consecutive:
		return 1

	if piecesOfColor == 0 and emptySpaces == Connect4.CONSECUTIVE - consecutive:
		return -1
	return 0

def __evaluate_window(window):
		score = 0
		EMPTY = 0
		piece = 1
		opp_piece = 2

		if np.count_nonzero(window == piece) == 4:
			score += 100
		elif np.count_nonzero(window == piece) == 3 and np.count_nonzero(window == EMPTY) == 1:
			score += 5
		elif np.count_nonzero(window == piece) == 2 and np.count_nonzero(window == EMPTY) == 2:
			score += 2

		if np.count_nonzero(window == opp_piece) == 3 and np.count_nonzero(window == EMPTY) == 1:
			score -= 4

		return score