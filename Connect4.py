import numpy as np
from enum import Enum

from Connect4States import Connect4States
from Connect4Colors import Connect4Colors
from Connect4Pieces import Connect4Pieces

class Connect4:
	"Represents a game of connect 4"


	HEIGHT = 6
	WIDTH = 7
	CONSECUTIVE = 4

	def __init__(self, color):
		self.grid = np.zeros((Connect4.HEIGHT,Connect4.WIDTH), dtype=int)

		state = Connect4States.RED_TURN if color == Connect4Colors.RED else Connect4States.YELLOW_TURN
		self.state = state

	def playMove(self, column):
		"""Play a move in the selected column
		raises error if the selected colunm is full
		return 0 if the move was successfully played"""

		#Should never trigger, but as a safety measure
		if self.grid[self.HEIGHT - 1, column] != 0:
			raise NameError("Column Full")
		if self.state == Connect4States.RED_WIN or self.state == Connect4States.YELLOW_WIN:
			raise NameError("Game ended")


		columnHeight = 0

		#Finds the height of the selected column
		emptySlotFound = False
		i = 0
		while not emptySlotFound and i < self.HEIGHT:
			if self.grid[i, column] == 0:
				columnHeight = i
				emptySlotFound = True
			i += 1

		#Change the grid
		if self.state == Connect4States.YELLOW_TURN:
			self.grid[columnHeight, column] = Connect4Pieces.YELLOW_PIECE.value

		if self.state == Connect4States.RED_TURN:
			self.grid[columnHeight, column] = Connect4Pieces.RED_PIECE.value


		#Check if game has ended because of the move
		gameStatus = self.checkIfGameFinished()

		#If game is ongoing
		if gameStatus == 0:
			self.switchTurn()

		#Set the correct state
		if gameStatus == 1:
			self.state = Connect4States.RED_WIN
		if gameStatus == 2:
			self.state = Connect4States.YELLOW_WIN

	def isValidLocation(self, column):
		return self.grid[self.HEIGHT - 1, column] == 0


	def switchTurn(self):
		"Switchs the turn of the game"

		if self.state == Connect4States.RED_TURN:
			self.state = Connect4States.YELLOW_TURN 
		else:
			self.state = Connect4States.RED_TURN




	def checkIfGameFinished(self):
		"""Checks if there is a connect 4 on the grid
		returns 0 if game is ongoing, 1 if game is won for red, 2 if game is won for yellow"""

		status = 0
		if self.__checkConnect4(Connect4Pieces.RED_PIECE.value):
			status = 1

		if self.__checkConnect4(Connect4Pieces.YELLOW_PIECE.value):
			status = 2

		return status


	def __checkConnect4(self, color):
		for x in range(self.WIDTH):
			for y in range(self.HEIGHT):

				isConnect4 = False

				#Check for row connect 4
				if not isConnect4 and x + self.CONSECUTIVE <= self.WIDTH:
					isConnect4 = self.__checkConsecutivePieces(x, y, 1, 0, color)

				#Check for column connect 4
				if not isConnect4 and y + self.CONSECUTIVE <= self.HEIGHT:
					isConnect4 = self.__checkConsecutivePieces(x, y, 0, 1, color)

				#Check for (1;1) diagonal connect 4
				if not isConnect4 and (x + self.CONSECUTIVE <= self.WIDTH) and (y + self.CONSECUTIVE <= self.HEIGHT):
					isConnect4 = self.__checkConsecutivePieces(x, y, 1, 1, color)

				#Check for (1;-1) diagonal connect 4
				if not isConnect4 and (x + self.CONSECUTIVE <= self.WIDTH) and (y - self.CONSECUTIVE <= -1):
					isConnect4 = self.__checkConsecutivePieces(x, y, 1, -1, color)

				if isConnect4:
					return True

		return False


	def __checkConsecutivePieces(self, ox, oy, dx, dy, color):
		consecutivePieces = 0
		#print(ox, oy)

		for i in range(self.CONSECUTIVE):
			if self.grid[oy + dy * i, ox + dx * i] == color:
				consecutivePieces += 1
			else:
				consecutivePieces = 0

		if consecutivePieces == self.CONSECUTIVE:
				print("detected connect 4 : ", ox, oy, dx, dy)

		return (True if consecutivePieces == self.CONSECUTIVE else False)


	def printGrid(self):
		print(np.flipud(self.grid))