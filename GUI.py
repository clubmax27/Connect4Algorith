import pygame

from Connect4 import Connect4
from Connect4States import Connect4States

from GUIConsts import GUIConsts

BLUE = GUIConsts.BLUE.value
BLACK = GUIConsts.BLACK.value
RED = GUIConsts.RED.value
YELLOW = GUIConsts.YELLOW.value

ROW_COUNT = GUIConsts.ROW_COUNT.value
COLUMN_COUNT = GUIConsts.COLUMN_COUNT.value

SQUARESIZE = GUIConsts.SQUARESIZE.value

width = GUIConsts.width.value
height = GUIConsts.height.value

size = (GUIConsts.width.value, GUIConsts.height.value)

RADIUS = GUIConsts.RADIUS.value

def drawBoard(board, screen):
	for c in range(Connect4.WIDTH):
		for r in range(Connect4.HEIGHT):
			pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	
	for c in range(Connect4.WIDTH):
		for r in range(Connect4.HEIGHT):
			if board[r][c] == 1:
				pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
			elif board[r][c] == 2: 
				pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
	pygame.display.update()

def LoadGUI(board):
	pygame.init()

	screen = pygame.display.set_mode(size)
	drawBoard(board, screen)
	pygame.display.update()

	return screen

def handleMouseMotion(event, screen, game):
	pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
	posx = event.pos[0]
	if game.state == Connect4States.YELLOW_TURN:
		pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
	else: 
		pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)

def handleGameVictory(screen, game):
	label = None
	myfont = pygame.font.SysFont("monospace", 75)

	if game.state == Connect4States.RED_WIN:
		label = myfont.render("Player 1 wins!!", 1, GUIConsts.RED.value)

	if game.state == Connect4States.YELLOW_WIN:	
		label = myfont.render("Player 2 wins!!", 1, GUIConsts.YELLOW.value)

	screen.blit(label, (40,10))