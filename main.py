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
		print(ai.MinMaxAlgorithm(game, 0, Connect4Colors.YELLOW))

if __name__=="__main__":
   main()