import chess_config as cc

print("Configurate use: ")
print("Mode: ")
config = input("1: AI, 2: Human: ")

while (config != "1") and (config != "2"):
    print("Type '1' for AI mode of '2' for human mode")
    config = input("1: AI, 2: Human: ")



current_game = cc.chess()

if config == "1":
    while not cc.game_ended(current_game):
        cc.make_move(current_game)

else:
    cc.print_board(current_game.board)

    test = cc.find_moves(current_game)
    for t in test:
        print(t)

    while not cc.game_ended(current_game):
        notation = input("Make Your Move " + str(current_game.current_player_turn) + ": ")
        move = cc.chess_notation_translator(notation, current_game)

        if not move:
            print(current_game.move_feedback)
            continue

        cc.make_move(current_game, move[0], move[1])

        # Gives proper response depending on the move outcome(valid or invalid, check or not)
        if current_game.move_feedback == "Success":
            cc.print_board(current_game.board)
        elif current_game.move_feedback == "Check":
            cc.print_board(current_game.board)
            print(current_game.move_feedback)
        else:
            print(current_game.move_feedback)
            continue

        cc.update_repitition_states(current_game, move, notation)

    cc.end_statement(current_game)