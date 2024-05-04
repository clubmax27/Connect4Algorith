# Connect 4 MinMax Algorithm

This project implements a MinMax algorithm with Alpha-Beta pruning for playing Connect 4 against an AI opponent. The algorithm is implemented in Python using the pygame library for the graphical user interface (GUI).

## Overview

The main components of the project include:

-   **Connect4.py**: Contains the logic for the Connect 4 game.
-   **Connect4States.py**: Enumerates the possible states of the Connect 4 game.
-   **Connect4Colors.py**: Enumerates the colors used in the Connect 4 game (e.g., RED, YELLOW).
-   **MinMax.py**: Implements the MinMax algorithm for game decision making.
-   **AlphaBeta.py**: Implements the Alpha-Beta pruning optimization for the MinMax algorithm.
-   **EvaluateBoard.py**: Contains the evaluation function to assess the game state.
-   **GUI.py**: Handles the graphical user interface using pygame for game visualization.
-   **GUIConsts.py**: Defines constants used in the GUI.

## Pre-requisites

1. Clone this repository to your local machine.
2. Install the requirements with the following command :

```bash
pip install -r requirements.txt
```

### Running the Program

Run the main script `main.py` to start playing Connect 4 against the AI using the MinMax algorithm:

```bash
python main.py
```

## Algorithm Parameters

-   **DEPTH**: The depth of the MinMax tree, controlling the algorithm's lookahead depth.
-   **PLAYER_STARTING**: Flag indicating whether the player or AI starts the game.

## Gameplay

-   The AI player uses the Alpha-Beta pruning enhanced MinMax algorithm to make optimal moves.
-   Game states and moves are displayed in the pygame GUI.
-   The algorithm's performance metrics such as time taken and the number of evaluated grids are printed during AI decision-making.

## Contributions

Contributions to improving the algorithm's efficiency or the GUI interface are welcome. Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
