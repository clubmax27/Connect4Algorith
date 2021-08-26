from enum import Enum
import pygame
from Connect4 import Connect4

class GUIConsts(Enum):
	"Enum for the different constants for the GUI"

	BLUE = (0,0,255)
	BLACK = (0,0,0)
	RED = (255,0,0)
	YELLOW = (255,255,0)

	ROW_COUNT = Connect4.HEIGHT
	COLUMN_COUNT = Connect4.WIDTH

	SQUARESIZE = 100

	width = COLUMN_COUNT * SQUARESIZE
	height = (ROW_COUNT+1) * SQUARESIZE

	size = (width, height)

	RADIUS = int(SQUARESIZE/2 - 5)