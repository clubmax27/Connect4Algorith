from Connect4 import Connect4

from Connect4States import Connect4States
from Connect4Colors import Connect4Colors
from Connect4Pieces import Connect4Pieces

"""Function to evaluate the score of a board
Positive score means Yellow is winning
Negative score means Red is winning"""

def EvaluateBoard(game):

	centerPiecesCoef = 5
	combosOf2Coef = 8
	combosOf3Coef = 15
	multipleThreatsCoef = 100

	#We check if the game is won, in this case the result is trivial
	if game.state == Connect4States.YELLOW_WIN:
		return 10000

	if game.state == Connect4States.RED_WIN:
		return -10000 

	if game.state == Connect4States.STALEMATE:
		return 0 

	#We evaluate the game based on three characteristics

	#First, how many pieces we have in the center
	centerPieces = __countPiecesInCenter(game)

	#Second, how many combo of 3 pieces with one empty space at the end we have
	combosOf2 = __countCombosOfPiecesWithEmptySpace(game, 2, Connect4Pieces.YELLOW_PIECE.value) - __countCombosOfPiecesWithEmptySpace(game, 2, Connect4Pieces.RED_PIECE.value)

	#Third, how many combo of 2 pieces with one empty space at the end we have
	combosOf3 = __countCombosOfPiecesWithEmptySpace(game, 3, Connect4Pieces.YELLOW_PIECE.value) - __countCombosOfPiecesWithEmptySpace(game, 3, Connect4Pieces.RED_PIECE.value)

	#Fourth, how many multiple threats ("7" traps and double lines) we have
	multipleThreats = __countCombosOfMultipleThreats(game, 3, Connect4Pieces.YELLOW_PIECE.value) - __countCombosOfMultipleThreats(game, 3, Connect4Pieces.YELLOW_PIECE.value)

	#Fifth, instant double line, is handled by the depth of MinMax

	return centerPieces * centerPiecesCoef + \
		   combosOf2 * combosOf2Coef + \
		   combosOf3 * combosOf3Coef + \
		   multipleThreats * multipleThreatsCoef

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

	for x in range(Connect4.WIDTH):
		for y in range(Connect4.HEIGHT):
			count += __countCombosOfPiecesAroundEmptySpace(game, x, y, consecutive, color)

	return count

def __countCombosOfPiecesAroundEmptySpace(game, x, y, consecutive, color):
	isThreatPresent = False

	#Check for (1;0) row connect 4
	if x + (consecutive + 1) < Connect4.WIDTH:
		isThreatPresent = isThreatPresent or __checkConsecutivePiecesWithEmptySpace(game, x, y, 1, 0, color, consecutive)

	#Check for (-1;0) row connect 4
	if x - (consecutive + 1) >= 0:
		isThreatPresent = isThreatPresent or __checkConsecutivePiecesWithEmptySpace(game, x, y, 1, 0, color, consecutive)


	#Check for (0;1) column connect 4
	if y + (consecutive + 1) < Connect4.HEIGHT:
		isThreatPresent = isThreatPresent or __checkConsecutivePiecesWithEmptySpace(game, x, y, 0, 1, color, consecutive)

	#Check for (0;-1) column connect 4
	if y - (consecutive + 1) >= 0:
		isThreatPresent = isThreatPresent or __checkConsecutivePiecesWithEmptySpace(game, x, y, 0, -1, color, consecutive)


	#Check for (1;1) diagonal connect 4
	if x + (consecutive + 1) < Connect4.WIDTH and y + (consecutive + 1) < Connect4.HEIGHT:
		isThreatPresent = isThreatPresent or __checkConsecutivePiecesWithEmptySpace(game, x, y, 1, 1, color, consecutive)

	#Check for (-1;-1) diagonal connect 4
	if x - (consecutive + 1) >= 0 and y - (consecutive + 1) >= 0:
		isThreatPresent = isThreatPresent or __checkConsecutivePiecesWithEmptySpace(game, x, y, -1, -1, color, consecutive)


	#Check for (1;-1) diagonal connect 4
	if x + (consecutive + 1) < Connect4.WIDTH and y - (consecutive + 1) >= 0:
		isThreatPresent = isThreatPresent or __checkConsecutivePiecesWithEmptySpace(game, x, y, 1, -1, color, consecutive)

	#Check for (-1;1) diagonal connect 4
	if x + (consecutive + 1) < Connect4.WIDTH and y - (consecutive + 1) >= 0:
		isThreatPresent = isThreatPresent or __checkConsecutivePiecesWithEmptySpace(game, x, y, -1, 1, color, consecutive)

	return isThreatPresent

def __checkConsecutivePiecesWithEmptySpace(game, ox, oy, dx, dy, color, consecutive):
	
	#If (ox;oy) is not an empty space, skip
	if game.grid[oy, ox] == Connect4Pieces.EMPTY:
		consecutivePieces = 0

		for i in range(consecutive):
			if game.grid[oy + dy * (i + 1), ox + dx * (i + 1)] == color:
				consecutivePieces += 1
			else:
				consecutivePieces = 0

		if consecutivePieces == consecutive:
			return True
	
	return False
