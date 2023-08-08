import chess_config as cc
import MCTS

print("Configurate use: ")
print("Mode: ")
config = input("1: AI, 2: Human: ")

while (config != "1") and (config != "2"):
    print("Type '1' for AI mode or '2' for human mode")
    config = input("1: AI, 2: Human: ")



current_game = cc.chess()

if config == "1":
    responded = False
    searches = 1
    c_value = 1.4
    
    while not responded:
        num = input("How many searches do you want to make per move? ")
        try:
            int(num)
        except:
            responded = False
        finally:
            searches = int(num)
            responded = True

    mcts = MCTS.mcts(current_game, c_value, searches)
    cc.print_board(current_game.board)
    print(" ")
    while True:
        # Gives proper response depending on the move outcome(valid or invalid, check or not)
        if cc.game_ended(current_game):
            cc.print_board(current_game.board)
            print(" ")
            for move in current_game.moves:
                print(move)
            break
        elif current_game.move_feedback == "Success":
            cc.print_board(current_game.board)
            print(" ")
        elif current_game.move_feedback == "Check":
            cc.print_board(current_game.board)
            print(current_game.move_feedback)
            print(" ")

        if current_game.current_player_turn == 1:
            notation = input("Make Your Move " + str(current_game.current_player_turn) + ": ")
            move = cc.chess_notation_translator(notation, current_game)

            if not move:
                print(current_game.move_feedback)
                continue

            cc.make_move(current_game, move[0], move[1])
            cc.update_repitition_states(current_game, move, notation)
            continue
        else:
            
            mcts_probs = mcts.search()
            move = []
            visits = 0
            for action in mcts_probs:
                if action[1] > visits:
                    move = action[0]
                    visits = action[1]
            cc.make_move(current_game, move[0], move[1])
            continue
else:
    cc.print_board(current_game.board)

    while not cc.game_ended(current_game):
        notation = input("Make Your Move " + str(current_game.current_player_turn) + ": ")
        move = cc.chess_notation_translator(notation, current_game)

        if not move:
            print(current_game.move_feedback)
            continue

        cc.make_move(current_game, move[0], move[1])

        # Gives proper response depending on the move outcome(valid or invalid, check or not)
        if cc.game_ended(current_game):
                print(current_game.moves)
                break
        elif current_game.move_feedback == "Success":
            cc.print_board(current_game.board)
        elif current_game.move_feedback == "Check":
            cc.print_board(current_game.board)
            print(current_game.move_feedback)
        else:
            print(current_game.move_feedback)
            continue

        cc.update_repitition_states(current_game, move, notation)

    cc.end_statement(current_game)