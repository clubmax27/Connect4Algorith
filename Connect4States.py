from enum import Enum

class Connect4States(Enum):
	"Enum for the different states of a connect 4 game"
	NOT_STARTED = 1
	RED_TURN = 2
	YELLOW_TURN = 3
	RED_WIN = 4
	YELLOW_WIN = 5