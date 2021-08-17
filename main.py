import Connect4

def main():
	game = Connect4.Connect4(Connect4.Connect4Colors.YELLOW)
	game.printGrid()
	game.playMove(0)
	game.playMove(0)
	game.printGrid()
	game.playMove(1)
	game.playMove(1)
	game.printGrid()
	game.playMove(2)
	game.playMove(2)
	game.printGrid()
	game.playMove(3)
	game.printGrid()

if __name__=="__main__":
   main()