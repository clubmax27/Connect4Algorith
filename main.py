import Connect4
from enum import Enum

import Connect4States

def main():
	game = Connect4.Connect4(Connect4.Connect4Colors.YELLOW)
	while game.state != Connect4States.RED_WIN or game.state != Connect4States.YELLOW_WIN:
		game.printGrid()
		column = int(input("what column to play in ? (1 - 7)"))
		game.playMove(column - 1)

if __name__=="__main__":
   main()