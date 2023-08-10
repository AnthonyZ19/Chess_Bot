This is my attempt at making an AI capable of playing chess modeled after alpha zero.

The chess_config.py file contains the functions that create the rules and will allow for the game of chess to be played.
MCTS.py contains the framework for the Monte-Carlo Tree Search
main.py contains the user interface and combines the previous two file to create the program
Currently supports player vs player and player vs bot, with moves being defined via chess algebraic notation as defined by chess.com
Conducts a certain amount of searches before playing a move for each move as pre-defined by the user.
