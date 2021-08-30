from enum import Enum

class Connect4Pieces(Enum):
	"Enum for the different pieces of a connect 4 game"
	EMPTY = 0
	RED_PIECE = 1
	YELLOW_PIECE = 2

	"""def getOppositeColorPiece(color):
		if color == Connect4Pieces.RED_PIECE:
			return Connect4Pieces.YELLOW_PIECE
		else:
			return Connect4Pieces.RED_PIECE"""