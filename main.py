import Connect4
from MinMax import MinMax
from enum import Enum

from Connect4States import Connect4States
from Connect4Colors import Connect4Colors

def main():
	game = Connect4.Connect4(Connect4Colors.YELLOW)
	ai = MinMax()
	while game.state != Connect4States.RED_WIN or game.state != Connect4States.YELLOW_WIN:
		game.printGrid()
		column = int(input("what column to play in ? (1 - 7)"))
		game.playMove(column - 1)

		player = Connect4Colors.RED.value
		if game.state == Connect4States.YELLOW_TURN:
			player = Connect4Colors.YELLOW.value

		score = ai.MinMaxAlgorithm(game, 3, player)
		print(score)
		if score == 10000:
			print("Yellow can only win")

		if score == -10000:
			print("Red can only win")

if __name__=="__main__":
   main()