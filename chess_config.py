"""
print("Configurate use: ")
print("Mode: ")
config = input("1: AI, 2: Human: ")

while (config != "1") and (config != "2"):
    print("Type '1' for AI mode of '2' for human mode")
    config = input("1: AI, 2: Human: ")

def main(mode):
    current_game = chess()

    if mode == 1:

        print_board(current_game.board)

        test = find_moves(current_game)
        for t in test:
            print(t)

        while not game_ended(current_game):
            notation = input("Make Your Move " + str(current_game.current_player_turn) + ": ")
            move = chess_notation_translator(notation, current_game)

            if not move:
                print(current_game.move_feedback)
                continue

            make_move(current_game, move[0], move[1])

            # Gives proper response depending on the move outcome(valid or invalid, check or not)
            if current_game.move_feedback == "Success":
                print_board(current_game.board)
            elif current_game.move_feedback == "Check":
                print_board(current_game.board)
                print(current_game.move_feedback)
            else:
                print(current_game.move_feedback)
                continue

            update_repitition_states(current_game, move, notation)

        end_statement(current_game)
    else:
        while not game_ended(current_game):
            make_move(current_game)
"""

# Stores chess game info
class chess:
    def __init__(self):
        self.moves = []
        
        self.board = ([ [-5,-3, -3.25, -9, -10, -3.25, -3, -5],
                        [-1,-1, -1,    -1,  -1, -1,    -1, -1],
                        [ 0, 0,  0,     0,   0,  0,     0,  0],
                        [ 0, 0,  0,     0,   0,  0,     0,  0],
                        [ 0, 0,  0,     0,   0,  0,     0,  0],
                        [ 0, 0,  0,     0,   0,  0,     0,  0],
                        [ 1, 1,  1,     1,   1,  1,     1,  1],
                        [ 5, 3,  3.25,  9,  10,  3.25,  3,  5]])
        
        self.white_king_moved = False

        self.rook_a1_moved = False

        self.rook_h1_moved = False

        self.black_king_moved = False

        self.rook_a8_moved = False

        self.rook_h8_moved = False

        self.last_move_en_passant = False

        self.current_player_turn = 1

        self.move_feedback = ""

        self.is_repitition_states = []


class pawn:
    def __init__(self, color):
        # "color" is -1 for black and 1 for white
        self.side = color
        self.value = (1 * color)

    def legal_moves(self, position, game, checking_check = False):
        # Stores legal moves for this piece in the following list
        pawn_moves = []
        board_state = game.board
        # Checks moves if the piece color is black
        if self.side == -1:
            # Ensures that these moves aren't included when checking for checks since the pawn can't capture like this
            if not checking_check:
                # Checks if the piece can move forward
                if board_state[(position[0] + 1)][position[1]] == 0:
                    pawn_moves.append([(position[0] + 1), position[1]])
                    if position[0] == 1:
                        if board_state[(position[0] + 2)][position[1]] == 0:
                            pawn_moves.append([(position[0] + 2), position[1]])

            # Checks if the pawn can take any pieces
            if (position[0] < 7) and (position[1] < 7):
                if board_state[(position[0] + 1)][position[1] + 1] > 0:
                    pawn_moves.append([(position[0] + 1), (position[1] + 1)])

            if (position[0] < 7) and (position[1] > 0):
                if board_state[(position[0] + 1)][position[1] - 1] > 0:
                    pawn_moves.append([(position[0] + 1), (position[1] - 1)])

            if game.moves:
                if game.last_move_en_passant:
                    passant_pawn_pos = (game.moves[len(game.moves) - 2])["White"][2]
                    if passant_pawn_pos[0] == position[0]:
                        if passant_pawn_pos[1] == (position[1] + 1):
                            pawn_moves.append([(position[0] + 1), (position[1] + 1)])
                        elif passant_pawn_pos[1] == (position[1] - 1):
                            pawn_moves.append([(position[0] + 1), (position[1] - 1)])

        # Checks moves if the piece is white
        else:
            # Ensures that these moves aren't included when checking for checks since the pawn can't capture like this
            if not checking_check:
                # Checks if it can move forward
                if board_state[(position[0] - 1)][position[1]] == 0:
                    pawn_moves.append([(position[0] - 1), position[1]])
                    if position[0] == 6:
                        if board_state[(position[0] - 2)][position[1]] == 0:
                            pawn_moves.append([(position[0] - 2), position[1]])

            # Checks if the piece can take another
            if (position[0] > 0) and (position[1] < 7):
                if board_state[(position[0] - 1)][position[1] + 1] < 0:
                    pawn_moves.append([(position[0] - 1), (position[1] + 1)])

            if (position[0] > 0) and (position[1] > 0):
                if board_state[(position[0] - 1)][position[1] - 1] < 0:
                    pawn_moves.append([(position[0] - 1), (position[1] - 1)])

            if len(game.moves) > 1:
                if game.last_move_en_passant:
                    passant_pawn_pos = (game.moves[len(game.moves) - 2])["Black"][2]
                    if passant_pawn_pos[0] == position[0]:
                        if passant_pawn_pos[1] == (position[1] + 1):
                            pawn_moves.append([(position[0] - 1), (position[1] + 1)])
                        elif passant_pawn_pos[1] == (position[1] - 1):
                            pawn_moves.append([(position[0] - 1), (position[1] - 1)])

        return pawn_moves


class bishop:
    def __init__(self, color):
        # "color" is -1 for black and 1 for white
        self.side = color
        self.value = (3.25 * color)

    def legal_moves(self, position, game):
        # Stores the legal moves for the bishop or the defended squares when the defends parameter is true
        bishop_moves = []
        board_state = game.board

        # Checks moves for when the piece is white
        if self.side == -1:
            increment = 1

            # Repeatedly checks if the bishop can move to each square it can see based on the previous variables
            while True:
                # Try is used to prevent error in case the position that is being checked is out of range and stops the loop
                try:
                    # Checks if the spot is unoccupied or occupied by an enemy piece
                    if board_state[(position[0] + increment)][(position[1] + increment)] >= 0:
                        # Adds the spot to the list of legal moves
                        bishop_moves.append([(position[0] + increment), (position[1] + increment)])
                        
                    # Checks if the spot is empty
                    if board_state[(position[0] + increment)][(position[1] + increment)] != 0:
                        break
                    increment += 1
                except:
                    break


            increment = 1

            # Repeatedly checks if the bishop can move to each square it can see based on the previous variables
            while True:
                # Try is used to prevent error in case the position that is being checked is out of range and stops the loop
                try:
                    if ((position[0] - increment) >= 0) and ((position[1] - increment) >= 0):
                        # Checks if the spot is unoccupied or occupied by an enemy piece
                        if board_state[(position[0] - increment)][(position[1] - increment)] >= 0:
                            # Adds the spot to the list of legal moves
                            bishop_moves.append([(position[0] - increment), (position[1] - increment)])

                        # Checks if the spot is empty
                        if board_state[(position[0] - increment)][(position[1] - increment)] != 0:
                            break
                        increment += 1
                    else:
                        break
                except:
                    break

            increment = 1

            # Repeatedly checks if the bishop can move to each square it can see based on the previous variables
            while True:
                # Try is used to prevent error in case the position that is being checked is out of range and stops the loop
                try:
                    if ((position[0] - increment) >= 0):
                        # Checks if the spot is unoccupied or occupied by an enemy piece
                        if board_state[(position[0] - increment)][(position[1] + increment)] >= 0:
                            # Adds the spot to the list of legal moves
                            bishop_moves.append([(position[0] - increment), (position[1] + increment)])

                        # Checks if the spot is empty
                        if board_state[(position[0] - increment)][(position[1] + increment)] != 0:
                            break
                        increment += 1
                    else:
                        break
                except:
                    break

            increment = 1

            # Repeatedly checks if the bishop can move to each square it can see based on the previous variables
            while True:
                # Try is used to prevent error in case the position that is being checked is out of range and stops the loop
                try:
                    if ((position[1] - increment) >= 0):
                        # Checks if the spot is unoccupied or occupied by an enemy piece
                        if board_state[(position[0] + increment)][(position[1] - increment)] >= 0:
                            # Adds the spot to the list of legal moves
                            bishop_moves.append([(position[0] + increment), (position[1] - increment)])

                        # Checks if the spot is empty
                        if board_state[(position[0] + increment)][(position[1] - increment)] != 0:
                            break
                        increment += 1
                    else:
                        break
                except:
                    break

        else:
            increment = 1

            # Repeatedly checks if the bishop can move to each square it can see based on the previous variables
            while True:
                # Try is used to prevent error in case the position that is being checked is out of range and stops the loop
                try:
                    if board_state[(position[0] + increment)][(position[1] + increment)] <= 0:
                        # Adds the spot to the list of legal moves
                        bishop_moves.append([(position[0] + increment), (position[1] + increment)])
                             
                    # Checks if the spot is empty
                    if board_state[(position[0] + increment)][(position[1] + increment)] != 0:
                        break
                    increment += 1
                except:
                    break

            increment = 1

            # Repeatedly checks if the bishop can move to each square it can see based on the previous variables
            while True:
                # Try is used to prevent error in case the position that is being checked is out of range and stops the loop
                try:
                    if ((position[0] - increment) >= 0) and ((position[1] - increment) >= 0):
                        if board_state[(position[0] - increment)][(position[1] - increment)] <= 0:
                            # Adds the spot to the list of legal moves
                            bishop_moves.append([(position[0] - increment), (position[1] - increment)])

                        # Checks if the spot is empty
                        if board_state[(position[0] - increment)][(position[1] - increment)] != 0:
                            break
                        increment += 1
                    else:
                        break
                except:
                    break

            increment = 1

            # Repeatedly checks if the bishop can move to each square it can see based on the previous variables
            while True:
                # Try is used to prevent error in case the position that is being checked is out of range and stops the loop
                try:
                    if ((position[0] - increment) >= 0):
                        if board_state[(position[0] - increment)][(position[1] + increment)] <= 0:
                            # Adds the spot to the list of legal moves
                            bishop_moves.append([(position[0] - increment), (position[1] + increment)])

                        # Checks if the spot is empty
                        if board_state[(position[0] - increment)][(position[1] + increment)] != 0:
                            break
                        increment += 1
                    else:
                        #inRange = False
                        break
                except:
                    #inRange = False  
                    break

            increment = 1

            # Repeatedly checks if the bishop can move to each square it can see based on the previous variables
            while True:
                # Try is used to prevent error in case the position that is being checked is out of range and stops the loop
                try:
                    if ((position[1] - increment) >= 0):
                        if board_state[(position[0] + increment)][(position[1] - increment)] <= 0:
                            # Adds the spot to the list of legal moves
                            bishop_moves.append([(position[0] + increment), (position[1] - increment)])

                        # Checks if the spot is empty
                        if board_state[(position[0] + increment)][(position[1] - increment)] != 0:
                            break
                        increment += 1
                    else:
                        break
                except:
                    break
                        
        return bishop_moves


class knight:
    def __init__(self, color):
        # "color" is -1 for black and 1 for white
        self.side = color
        self.value = (3 * color)
    def legal_moves(self, position, game):
        # Stores legal moves for the knight or defended squares when the defends parameter is True
        knight_moves = []
        board_state = game.board

        # Checks legal moves for a black knight 
        if self.side == -1:
            # Checks legal moves in which the knight moves by 2 vertically
            for y in [2, -2]:
                for x in [1, -1]:
                    # Try in case the position is out of range
                    try:
                        # Makes sure that the index isn't negative
                        if ((position[0] + y) >= 0) and ((position[1] + x) >= 0):
                            if board_state[(position[0] + y)][position[1] + x] >= 0:
                                # If the square is empty and not another black piece the move is appended
                                knight_moves.append([(position[0] + y), (position[1] + x)])
                    except:
                        continue

            # Checks legal moves in which the knight moves by 2 vertically
            for x in [2, -2]:
                for y in [1, -1]:
                    # Try in case the position is out of range
                    try:
                        # Makes sure that the index isn't negative
                        if ((position[0] + y) >= 0) and ((position[1] + x) >= 0):
                            if board_state[(position[0] + y)][position[1] + x] >= 0:
                                # If the square is empty and not another black piece the move is appended
                                knight_moves.append([(position[0] + y), (position[1] + x)])
                    except:
                        continue
        else:
            # Checks legal moves in which the knight moves by 2 vertically
            for y in [2, -2]:
                for x in [1, -1]:
                    # Try in case the position is out of range
                    try:
                        # Makes sure that the index isn't negative
                        if ((position[0] + y) >= 0) and ((position[1] + x) >= 0):
                            if board_state[(position[0] + y)][position[1] + x] <= 0:
                                # If the square is empty and not another black piece the move is appended
                                knight_moves.append([(position[0] + y), (position[1] + x)])
                    except:
                        continue

            # Checks legal moves in which the knight moves by 2 vertically
            for x in [2, -2]:
                for y in [1, -1]:
                    # Try in case the position is out of range
                    try:
                        # Makes sure that the index isn't negative
                        if ((position[0] + y) >= 0) and ((position[1] + x) >= 0):
                            if board_state[(position[0] + y)][position[1] + x] <= 0:
                                # If the square is empty and not another black piece the move is appended
                                knight_moves.append([(position[0] + y), (position[1] + x)])
                    except:
                        continue
        return knight_moves


class rook:
    def __init__(self, color):
        # "color" is -1 for black and 1 for white
        self.side = color
        self.value = (5 * color)
    def legal_moves(self, position, game):
        # Stores legal moves for the rook or defended squares when defends is True
        rook_moves = []
        board_state = game.board

        if self.side == -1:
            # Checks moves forward(1) and backwards(-1), left(-1) and right(1)
            for direction in [1, -1]:
                increment = direction

                # Checks all legal moves vertically or in the y plane
                while True:
                    try:
                        # Ensures that the index isn't negative
                        if (position[0] + increment) >= 0:
                            # If the next spot on the board is unoccupied  or occupied by an enemy piece it's added as a legal move
                            if board_state[(position[0] + increment)][position[1]] >= 0:
                                rook_moves.append([(position[0] + increment), position[1]])
                            # Checks if the position is occupied to prevent the rook from jumping over pieces
                            if board_state[(position[0] + increment)][position[1]] != 0:
                                break
                        else:
                            break
                    except:
                        break

                    increment += direction

                increment = direction

                # Checks all legal moves horizontally or in the x plane
                while True:
                    try:
                        # Ensures that the index isn't negative
                        if (position[1] + increment) >= 0:
                            # If the next spot on the board is unoccupied  or occupied by an enemy piece it's added as a legal move
                            if board_state[position[0]][(position[1] + increment)] >= 0:
                                rook_moves.append([position[0], (position[1] + increment)])
                                # Checks if the position is occupied to prevent the rook from jumping over pieces
                            if board_state[position[0]][(position[1] + increment)] != 0:
                                break
                        else:
                            break
                    except:
                        break

                    increment += direction
        else:
            # Checks moves forward(1) and backwards(-1), left(-1) and right(1)
            for direction in [1, -1]:
                increment = direction

                # Checks all legal moves vertically or in the y plane
                while True:
                    try:
                        # Ensures that the index isn't negative
                        if (position[0] + increment) >= 0:
                            # If the next spot on the board is unoccupied  or occupied by an enemy piece it's added as a legal move
                            if board_state[(position[0] + increment)][position[1]] <= 0:
                                rook_moves.append([(position[0] + increment), position[1]])
                            # Checks if the position is occupied to prevent the rook from jumping over pieces
                            if board_state[(position[0] + increment)][position[1]] != 0:
                                break
                        else:
                            break
                    except:
                        break

                    increment += direction

                increment = direction

                # Checks all legal moves horizontally or in the x plane
                while True:
                    try:
                        # Ensures that the index isn't negative
                        if (position[1] + increment) >= 0:
                            # If the next spot on the board is unoccupied  or occupied by an enemy piece it's added as a legal move
                            if board_state[position[0]][(position[1] + increment)] <= 0:
                                rook_moves.append([position[0], (position[1] + increment)])
                                # Checks if the position is occupied to prevent the rook from jumping over pieces
                            if board_state[position[0]][(position[1] + increment)] != 0:
                                break
                        else:
                            break
                    except:
                        break

                    increment += direction
        return rook_moves


class queen:
    def __init__(self, color):
        # "color" is -1 for black and 1 for white
        self.side = color
        self.value = (9 * color)
    def legal_moves(self, position, game):
        queen_moves = []

        # Since the queen moves like a bishop and rook combined, I just call their classes and combine the legal moves for both
        bishop1 = bishop(self.side)
        rook1 = rook(self.side)

        # Stores the legal moves of the queen as if it were a bishop and rook
        bishop_moves = bishop1.legal_moves(position, game)
        rook_moves = rook1.legal_moves(position, game)
        
        # Combines the moves into a list of legal moves for the queen
        for moves in [bishop_moves, rook_moves]:
            for move in moves:
                queen_moves.append(move)

        return queen_moves


class king:
    def __init__(self, color):
        # "color" is -1 for black and 1 for white
        self.side = color
        self.value = (10 * color)
    def side(self):
        return self.side
    def legal_moves(self, position, game, checking_check = False):
        king_moves = []
        board_state = game.board
        
        if self.side == -1:
            # Loops through all the squares around the king
            for y in [-1, 0, 1]:
                for x in [-1, 0, 1]:
                    if ((position[0] + y) >= 0) and ((position[0] + y) < 8):
                        if ((position[1] + x) >= 0) and ((position[1] + x) < 8):
                            if board_state[(position[0] + y)][(position[1] + x)] >= 0:
                                if not checking_check:
                                    # Checks if the square is attacked by enemy pieces
                                    if not in_check(game, "attack", [(position[0] + y), (position[1] + x)]):
                                        king_moves.append([(position[0] + y), (position[1] + x)])
                                else:
                                    king_moves.append([(position[0] + y), (position[1] + x)])

            # Checks if the king can castle
            if not(game.black_king_moved):
                # Checks long castle
                if not(game.rook_a8_moved):
                    if (board_state[position[0]][position[1] - 1] == 0) and (board_state[position[0]][position[1] - 2] == 0) and (board_state[position[0]][position[1] - 3] == 0):
                        if not checking_check:
                            # Checks if the square is attacked by enemy pieces
                            if not in_check(game, "attack", [position[0], position[1] - 1]):
                                if not in_check(game, "attack", [position[0], (position[1] - 2)]):
                                    if not in_check(game, "attack", [position[0], position[1] - 3]):
                                        king_moves.append([position[0], (position[1] - 2)])
                        else:
                            king_moves.append([position[0], (position[1] - 2)])
                # Checks short castle
                if not(game.rook_h8_moved):
                    if (board_state[position[0]][position[1] + 1] == 0) and (board_state[position[0]][position[1] + 2] == 0):
                        if not checking_check:
                            # Checks if the square is attacked by enemy pieces
                            if not in_check(game, "attack", [position[0], position[1] + 1]):
                                if not in_check(game, "attack", [position[0], (position[1] + 2)]):
                                    king_moves.append([position[0], (position[1] + 2)])
                        else:
                            king_moves.append([position[0], (position[1] + 2)])
        else:
            # Loops through all the squares around the king
            for y in [-1, 0, 1]:
                for x in [-1, 0, 1]:
                    if ((position[0] + y) >= 0) and ((position[0] + y) < 8):
                        if ((position[1] + x) >= 0) and ((position[1] + x) < 8):
                            if board_state[(position[0] + y)][(position[1] + x)] <= 0:
                                if not checking_check:
                                    # Checks if the square is attacked by enemy pieces
                                    if not in_check(game, position, [(position[0] + y), (position[1] + x)]):
                                        king_moves.append([(position[0] + y), (position[1] + x)])
                                else:
                                    king_moves.append([(position[0] + y), (position[1] + x)])

            # Checks if the king can castle
            if not(game.white_king_moved):
                # Checks long castle
                if not(game.rook_a1_moved):
                    if (board_state[position[0]][position[1] - 1] == 0) and (board_state[position[0]][position[1] - 2] == 0) and (board_state[position[0]][position[1] - 3] == 0):
                        if not checking_check:
                            # Checks if the square is attacked by enemy pieces
                            if not in_check(game, "attack", [position[0], position[1] - 1]):
                                if not in_check(game, "attack", [position[0], (position[1] - 2)]):
                                    if not in_check(game, "attack", [position[0], position[1] - 3]):
                                        king_moves.append([position[0], (position[1] - 2)])
                        else:
                            king_moves.append([position[0], (position[1] - 2)])
                        
                # Checks short castle
                if not(game.rook_h1_moved):
                    if (board_state[position[0]][position[1] + 1] == 0) and (board_state[position[0]][position[1] + 2] == 0):
                        if not checking_check:
                            # Checks if the square is attacked by enemy pieces
                            if not in_check(game, "attack", [position[0], position[1] + 1]):
                                if not in_check(game, "attack", [position[0], (position[1] + 2)]):
                                    king_moves.append([position[0], (position[1] + 2)])
                        else:
                            king_moves.append([position[0], (position[1] + 2)])

        return king_moves


def piece_caller(value):
    if value == 1:
        return pawn(1)
    elif value == -1:
        return pawn(-1)
    elif value == 3:
        return knight(1)
    elif value == -3:
        return knight(-1)
    elif value == 3.25:
        return bishop(1)
    elif value == -3.25:
        return bishop(-1)
    elif value == 5:
        return rook(1)
    elif value == -5:
        return rook(-1)
    elif value == 9:
        return queen(1)
    elif value == -9:
        return queen(-1)
    elif value == 10:
        return king(1)
    elif value == -10:
        return king(-1)
    

def is_capture_notation(notation):
    for letter in notation:
        if letter == "x":
            return True
    return False


def is_check_notation(notation):
    for letter in notation:
        if letter == "+":
            return True
    return False


def is_checkmate_notation(notation):
    for letter in notation:
        if letter == "#":
            return True
    return False


def in_check(game, start_pos, end_pos):
    # Makes the tested move in order to check for checks
    king_position = []
    board_state = []
    if start_pos == "attack":
        board_state = game.board
    else:
        board_state = simulate_move(game, start_pos, end_pos)

    # Checks for checks for the black pieces
    if game.current_player_turn == -1:
        # Finds the king
        for row in range(0, 8):
            for col in range(0, 8):
                if board_state[row][col] == -10:
                    king_position = [row, col]
        # Iterates through each row and square
        for row in range(0, 8):
            for col in range(0, 8):
                # Checks if an enemy piece is in the position/square
                if board_state[row][col] > 0:
                    # If yes, it calls that piece and checks it's legal moves
                    enemy_piece = piece_caller(board_state[row][col])
                    if (abs(enemy_piece.value) == 10) or (abs(enemy_piece.value) == 1):
                        enemy_moves = enemy_piece.legal_moves([row, col], game, True)
                    else:
                        enemy_moves = enemy_piece.legal_moves([row, col], game)

                    if start_pos == "attack":
                        if end_pos in enemy_moves:
                            return True
                    else:
                        # If any of it's moves hits the king, if it were to move into that square
                        #  then True is returned
                        if king_position in enemy_moves:
                            return True
    # Same as before, but for white
    else:
        for row in range(0, 8):
            for col in range(0, 8):
                if board_state[row][col] == 10:
                    king_position = [row, col]
        # Iterates through each row and square
        for row in range(0, 8):
            for col in range(0, 8):
                # Checks if an enemy piece is in the position/square
                if board_state[row][col] <  0:
                    # If yes, it calls that piece and checks it's legal moves
                    enemy_piece = piece_caller(board_state[row][col])
                    if (enemy_piece.value == -10) or (enemy_piece.value == -1):
                        enemy_moves = enemy_piece.legal_moves([row, col], game, True)
                    else:
                        enemy_moves = enemy_piece.legal_moves([row, col], game)

                    if start_pos == "attack":
                        if end_pos in enemy_moves:
                            return True
                    else:
                        # If any of it's moves hits the king, if it were to move into that square
                        #  then True is returned
                        if king_position in enemy_moves:
                            return True
    # If none of the enemy pieces hit's the king were it to move into that square
    # Then False is returned
    return False


def letter_to_piece(letter, turn):
    if letter == 'K':
        return piece_caller(10 * turn)
    
    elif letter == 'Q':
        return piece_caller(9 * turn)
    
    elif letter == 'R':
        return piece_caller(5 * turn)
    
    elif letter == 'B':
        return piece_caller(3.25 * turn)
    
    elif letter == 'N':
        return piece_caller(3 * turn)
    
    elif letter == '':
        return piece_caller(turn)
    else:
        return False
    

def letter_to_index(letter):
    index = 0
    for Letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        if letter == Letter:
            return index
        
        index += 1
    
    return False


def chess_notation_translator(notation, game):
    turn = game.current_player_turn
    piece = None
    found = False
    true_row = 8

    end_pos_row = None
    end_pos_col = None

    start_pos_row = None
    start_pos_col = None

    if len(notation) == 2:
        # Checks if the notation for a pawn move was made correctly
        if notation[0].isalpha() and notation[1].isdigit():
            true_row -= int(notation[1])
            # Checks if the move is within bounds
            if (notation[0] == notation[0].lower()) and (true_row >= 0) and (true_row <= 7) and (letter_to_index(notation[0]) >= 0) and (letter_to_index(notation[0]) <= 7):
                piece = piece_caller(turn)
                end_pos_row = true_row
                end_pos_col = letter_to_index(notation[0])
                
            else:
                game.move_feedback = "Invalid Notation"
                return False
        else:
            game.move_feedback = "Invalid Notation"
            return False

    elif len(notation) == 3:
        # Checks if its a short castle
        if notation == "O-O":
            if turn == -1:
                piece = king(-1)
                end_pos_row = 0
                end_pos_col = 6
            else:
                piece = king(1)
                end_pos_row = 7
                end_pos_col = 6
        # Checks if the move is signaled as a check or checkmate
        elif is_check_notation(notation) or is_checkmate_notation(notation):
            # Checks that the move notation was made with the right format
            if notation[0].isalpha() and notation[1].isdigit():
                if notation[0] == notation[0].lower():
                    true_row -= int(notation[1])
                    # Checks if the move is within bounds
                    if (true_row >= 0) and (true_row <= 7) and (letter_to_index(notation[0]) >= 0) and (letter_to_index(notation[0]) <= 7):
                        end_pos_row = true_row
                        end_pos_col = letter_to_index(notation[0])
                        piece = piece_caller(turn)
                    else:
                        game.move_feedback = "Invalid Notation"
                        return False
                else:
                    game.move_feedback = "Invalid Notation"
                    return False
            else:
                game.move_feedback = "Invalid Notation"
                return False
        else:
            # Checks if its the correct notation for a move of a non-pawn piece
            # That doesn't involve any capture, check or checkmate
            if notation[0].isalpha() and notation[1].isalpha() and notation[2].isdigit():
                if notation[0] == notation[0].upper():
                    if notation[1] == notation[1].lower():
                        true_row -= int(notation[2])
                        # Checks if the move is within bounds
                        if (true_row >= 0) and (true_row <= 7) and (letter_to_index(notation[1]) >= 0) and (letter_to_index(notation[1]) <= 7):
                            piece = letter_to_piece(notation[0], turn)
                            end_pos_row = true_row
                            end_pos_col = letter_to_index(notation[1])
                        else:
                            game.move_feedback = "Invalid Notation"
                            return False
                    else:
                        game.move_feedback = "Invalid Notation"
                        return False
                else:
                    game.move_feedback = "Invalid Notation"
                    return False
            else:
                game.move_feedback = "Invalid Notation"
                return False
        
    elif len(notation) == 4:
        if notation[0].isalpha():
            # Checks if the notation involves a piece capture
            if is_capture_notation(notation):
                true_row -= int(notation[3])
                # Checks if it's a valid notation
                if notation[2].isalpha() and (notation[2] == notation[2].lower()) and notation[3].isdigit():
                    # Checks if the move is within bounds
                    if (true_row >= 0) and (true_row <= 7) and (letter_to_index(notation[2]) >= 0) and (letter_to_index(notation[2]) <= 7):
                        # Checks if it's a pawn capture with a specified column
                        if notation[0] == notation[0].lower():
                            piece = piece_caller(turn)
                            end_pos_row = true_row
                            end_pos_col = letter_to_index(notation[2])
                            start_pos_col = letter_to_index(notation[0])
                        # Checks if it's valid non-pawn capture
                        elif notation[0] == notation[0].upper():

                            piece = letter_to_piece(notation[0], turn)
                            end_pos_row = true_row
                            end_pos_col = letter_to_index(notation[2])
                        else:
                            game.move_feedback = "Invalid Notation"
                            return False
                    else:
                        game.move_feedback  = "Invalid Notation"
                        return False
                else:
                    game.move_feedback = "Invalid Notation"
                    return False
            # Checks if it's a notation the involves a check or a checkmate
            elif is_check_notation(notation) or is_checkmate_notation(notation):
                # Checks if the notation was made properly
                if notation[1].isalpha() and notation[2].isdigit():
                    true_row -= int(notation[2])
                    if (notation[0] == notation[0].upper()) and (notation[1] == notation[1].lower()):
                        if ((true_row >= 0) and (true_row <= 7)) and ((letter_to_index(notation[1]) >= 0) and (letter_to_index(notation[1]) <= 7)):
                            piece = letter_to_piece(notation[0], turn)
                            end_pos_row = true_row
                            end_pos_col = letter_to_index(notation[1])
                        else:
                            game.move_feedback = "Invalid Notation"
                            return False
                    else:
                        game.move_feedback = "Invalid Notation"
                        return False
                else:
                    game.move_feedback = "Invalid Notation"
                    return False
            # Checks if its a move with a specified starting column and that the notation was made correctly
            elif notation[1].isalpha() and notation[2].isalpha() and notation[3].isdigit():
                true_row -= int(notation[3])
                if (notation[0] == notation[0].upper()) and (notation[1] == notation[1].lower()) and (notation[2] == notation[2].lower()):
                    # Checks if the move is within bounds
                    if ((true_row >= 0) and (true_row <= 7)) and ((letter_to_index(notation[2]) >= 0) and (letter_to_index(notation[2]) <= 7)) and ((letter_to_index(notation[1]) >= 0) and (letter_to_index(notation[1]) <= 7)):
                        piece = letter_to_piece(notation[0], turn)
                        end_pos_row = true_row
                        end_pos_col = letter_to_index(notation[2])
                        start_pos_col = letter_to_index(notation[1])
                    else:
                        game.move_feedback = "Invalid Notation"
                        return False
                else:
                    game.move_feedback = "Invalid Notation"
                    return False
            elif notation[1].isdigit() and notation[2].isalpha() and notation[3].isdigit():
                true_row -= int(notation[3])
                true_col = 8 - int(notation[1])
                if (notation[0] == notation[0].upper()) and ((true_col >= 0) and (true_col <= 7)) and (notation[2] == notation[2].lower()) and  ((true_row >= 0) and (true_row <= 7)):
                    piece = letter_to_piece(notation[0], turn)
                    end_pos_row = true_row
                    end_pos_col = letter_to_index(notation[2])
                    start_pos_col = true_col
                else:
                    game.move_feedback = "Invalid Notation"
                    return False
            else:
                game.move_feedback = "Invalid Notation"
                return False
            
    elif len(notation) == 5:
        if notation == "O-O-O":
            if turn == -1:
                piece = king(-1)
                end_pos_row = 0
                end_pos_col = 2
            else:
                piece = king(1)
                end_pos_row = 7
                end_pos_col = 2
        elif is_check_notation(notation) or is_checkmate_notation(notation):
            if is_capture_notation(notation):
                if notation[0].isalpha() and notation[2].isalpha() and notation[3].isdigit():
                    true_row -= int(notation[3])
                    if (notation[0] == notation[0].upper()) and (notation[2] == notation[2].lower()) and ((true_row >= 0) and (true_row <= 7)) and ((letter_to_index(notation[2]) >= 0) and (letter_to_index(notation[2]) <= 7)):
                        piece = letter_to_piece(notation[0], turn)
                        end_pos_row = true_row
                        end_pos_col = letter_to_index(notation[2])
            else:
                game.move_feedback = "Invalid Notation"
                return False
    elif len(notation) == 6: 
        if is_check_notation(notation) or is_checkmate_notation(notation):
            if notation[0:5] == "O-O-O":
                if turn == -1:
                    piece = king(-1)
                    end_pos_row = 0
                    end_pos_col = 2
                else:
                    piece = king(1)
                    end_pos_row = 7
                    end_pos_col = 2

    else:
        game.move_feedback = "Invalid Notation"
        return False
    
    if type(piece) == None:
        game.move_feedback = "Invalid Notation"
        return False

    for row in range(0, 8):
        if found:
            break
        
        for col in range(0, 8):
            if found:
                break

            if game.board[row][col] == piece.value:
                moves = []
                if abs(piece.value) == 10:
                    moves = piece.legal_moves([row, col], game, True)
                else:
                    moves = piece.legal_moves([row, col], game)

                if not (start_pos_col == None):
                    if ([end_pos_row, end_pos_col] in moves) and col == start_pos_col:
                        start_pos_row = row
                        start_pos_col = col
                        found = True
                elif not (start_pos_row == None):
                    if ([end_pos_row, end_pos_col] in moves) and row == start_pos_row:
                        start_pos_col = col
                        start_pos_row = row
                        found = True
                elif [end_pos_row, end_pos_col] in moves:
                    start_pos_row = row
                    start_pos_col = col
                    found = True
                elif [row, col] == [8, 8]:
                    game.move_feedback = "Couldn't find move"
                    return False
                    
    if found:
        game.move_feedback = "Valid Notation"
        return [[start_pos_row, start_pos_col], [end_pos_row, end_pos_col]]
    else:
        game.move_feedback = "Invalid notation and/or move"
        return False


def make_move(game, start_pos, end_pos):
    game.move_feedback = "Move Error"
    en_passant = False
    castling = False
    legal_moves = []

    if not (start_pos):
        game.move_feedback = "Error: empty starting position"
        return False
    elif not (end_pos):
        game.move_feedback = "Error: empty ending position"
        return False
    elif (not (start_pos[0])) and (start_pos[0] != 0):
        game.move_feedback = "Error: empty starting position"
        return False
    elif (not (start_pos[1])) and (start_pos[1] != 0):
        game.move_feedback = "Error: empty starting position"
        return False
    elif (not (end_pos[0])) and (end_pos[0] != 0):
        game.move_feedback = "Error: empty ending position"
        return False
    elif (not (end_pos[1])) and (end_pos[1] != 0):
        game.move_feedback = "Error: empty ending position"
        return False
    else:
        
        piece = piece_caller(game.board[start_pos[0]][start_pos[1]])

        if abs(piece.value) == 10:
            legal_moves = piece.legal_moves(start_pos, game, True)
        else:
            legal_moves = piece.legal_moves(start_pos, game)

        if end_pos in legal_moves:
            if in_check(game, start_pos, end_pos):
                game.move_feedback = "This move leaves you in check"
                return False
            
            else:
                # Checks that the piece is the black king
                if piece.value == -10:
                    castling = True
                elif piece.value == 10:
                    castling = True
                elif piece.value == -1:
                    # Checks if the pawn moved 2 squares
                    if (end_pos[0] - 2) == start_pos[0]:
                        en_passant = True
                elif piece.value == 1:
                    # Checks if the pawn moved 2 squares
                    if (end_pos[0] + 2) == start_pos[0]:
                        en_passant = True
                # Records the move
                if game.current_player_turn == 1:
                    (game.moves).append({"White" : [piece.value, start_pos, end_pos]})
                    if (piece.value == 5) and (start_pos == [7, 0]):
                        game.rook_a1_moved == True
                    elif (piece.value == 5) and (start_pos == [7, 7]):
                        game.rook_h1_moved == True
                else:
                    ((game.moves)[len(game.moves) - 1]).update({"Black": [piece.value, start_pos, end_pos]})
                    if (piece.value == -5) and (start_pos == [0, 0]):
                        game.rook_a8_moved == True
                    elif (piece.value == -5) and (start_pos == [0, 7]):
                        game.rook_h8_moved == True

                if game.moves:
                    if game.last_move_en_passant:
                        if piece.value == -1:
                            passant_pawn_pos = (game.moves[len(game.moves) - 1])["White"][2]
                            if passant_pawn_pos[0] == start_pos[0]:
                                if passant_pawn_pos[1] == (start_pos[1] + 1):
                                    # Clears the enemy pawn if en passant is used
                                    if game.current_player_turn == -1:
                                        game.board[end_pos[0] - 1][end_pos[1]] = 0
                                    else:
                                        game.board[end_pos[0] + 1][end_pos[1]] = 0
                                elif passant_pawn_pos[1] == (start_pos[1] - 1):
                                    # Clears the enemy pawn if en passant is used
                                    if game.current_player_turn == -1:
                                        game.board[end_pos[0] - 1][end_pos[1]] = 0
                                    else:
                                        game.board[end_pos[0] + 1][end_pos[1]] = 0

                # Changes whos turn it is
                game.current_player_turn *= -1

                if en_passant:
                    game.last_move_en_passant = True
                else:
                    game.last_move_en_passant = False

                # Warns the opponent if they're in check
                if in_check(game, start_pos, end_pos):
                    game.move_feedback = "Check"
                else:
                    game.move_feedback = "Success"
                
                # Plays/makes the move
                game.board[start_pos[0]][start_pos[1]] = 0
                game.board[end_pos[0]][end_pos[1]] = piece.value
                
                if castling:
                    castle(piece.value, game, start_pos, end_pos)

                return True
        else:
            game.move_feedback = "Illegal Move"
            return False


def num_to_letter(value):

    if value == 0:
        return " "
    elif value == 1:
        return "P"
    elif value == -1:
        return "p"
    elif value == 3:
        return "N"
    elif value == -3:
        return "n"
    elif value == 3.25:
        return "B"
    elif value == -3.25:
        return "b"
    elif value == 5:
        return "R"
    elif value == -5:
        return "r"
    elif value == 9:
        return "Q"
    elif value == -9:
        return "q"
    elif value == 10:
        return "K"
    elif value == -10:
        return "k"
    

def print_board(board):
    modified_row = []

    for row in board:
        #print(row)
        for col in row:
            modified_row.append(num_to_letter(col))
        print(modified_row)
        modified_row = []


def find_king(value, board):
    for row in range(0, 8):
        for col in range(0, 8):
            if board[row][col] == value:
                return [row, col]


def is_checkmate(game):
    # Checks if 
    if game.current_player_turn == -1:
        for row in range(0, 8):
            for col in range(0 ,8):
                if game.board[row][col] < 0:
                    piece = piece_caller(game.board[row][col])

                    moves = []
                    if abs(piece.value) == 10:
                        moves = piece.legal_moves([row, col], game, True)
                    else:
                        moves = piece.legal_moves([row, col], game)
                    for move in moves:
                        if not (in_check(game, [row, col], move)):
                            return False
    else:
        for row in range(0, 8):
            for col in range(0 ,8):
                if game.board[row][col] > 0:
                    piece = piece_caller(game.board[row][col])

                    moves = []
                    if abs(piece.value) == 10:
                        moves = piece.legal_moves([row, col], game, True)
                    else:
                        moves = piece.legal_moves([row, col], game)
                    for move in moves:
                        if not (in_check(game, [row, col], move)):
                            return False
                        
    return True


def simulate_move(game, start_pos, end_pos):
    temp_game = chess()
    simulation = temp_game.board
    legal_moves = []
    castling = False
    en_passant_capture = False

    for row in range(0, 8):
        for col in range(0, 8):
            simulation[row][col] = game.board[row][col]

    if not (start_pos):
        game.move_feedback = "Error: empty starting position"
        return False
    if not (end_pos):
        game.move_feedback = "Error: empty ending position"
        return False
    if (not (start_pos[0])) and (start_pos[0] != 0):
        game.move_feedback = "Error: empty starting position"
        return False
    if (not (start_pos[1])) and (start_pos[1] != 0):
        game.move_feedback = "Error: empty starting position"
        return False
    if (not (end_pos[0])) and (end_pos[0] != 0):
        game.move_feedback = "Error: empty ending position"
        return False
    if (not (end_pos[1])) and (end_pos[1] != 0):
        game.move_feedback = "Error: empty ending position"
        return False
            
    piece = piece_caller(simulation[start_pos[0]][start_pos[1]])

    if abs(piece.value) == 10:
        legal_moves = piece.legal_moves(start_pos, game, True)
    else:
        legal_moves = piece.legal_moves(start_pos, game)

    if end_pos in legal_moves:
            
        # Checks that the piece is the black king
        if piece.value == -10:
            castling = True
        elif piece.value == 10:
            castling = True

        if game.moves:
            if game.last_move_en_passant:
                if piece.value == -1:
                    passant_pawn_pos = (game.moves[len(game.moves) - 1])["White"][2]
                    if passant_pawn_pos[0] == start_pos[0]:
                        if passant_pawn_pos[1] == (start_pos[1] + 1):
                            en_passant_capture = True
                        elif passant_pawn_pos[1] == (start_pos[1] - 1):
                            en_passant_capture = True

        # Clears the enemy pawn if en passant is used
        if en_passant_capture:
            if game.current_player_turn == -1:
                simulation[end_pos[0] - 1][end_pos[1]] = 0
            else:
                simulation[end_pos[0] + 1][end_pos[1]] = 0

        # Plays/makes the move
        simulation[start_pos[0]][start_pos[1]] = 0
        simulation[end_pos[0]][end_pos[1]] = piece.value

        if castling:
            castle(game.current_player_turn, temp_game, start_pos, end_pos)

        return simulation
     

def castle(value, game, start_pos, end_pos):
    if value < 0:
        # Updates the king_moved variable to disable future castling
        game.black_king_moved = True
        # Checks if the player is currently castling short
        if (end_pos[1] - 2) == start_pos[1]:
        # Updates the rook position and variable
            game.rook_h8_moved = True
            game.board[0][7] = 0
            game.board[0][5] = -5
        # Checks if the player is currently castling long
        elif (end_pos[1] + 2) == start_pos[1]:
            # Updates the rook position and variable
            game.rook_a8_moved = True
            game.board[0][0] = 0
            game.board[0][3] = -5
    else:
        # Updates the king_moved variable to disable future castling
        game.white_king_moved = True
        # Checks if the player is currently castling short
        if (end_pos[1] - 2) == start_pos[1]:
            # Updates the rook position and variable
            game.rook_h1_moved = True
            game.board[7][7] = 0
            game.board[7][5] = 5
        # Checks if the player is currently castling long
        elif (end_pos[1] + 2) == start_pos[1]:
            # Updates the rook position and variable
            game.rook_a1_moved = True
            game.board[7][0] = 0
            game.board[7][3] = 5


def copy_board(board):
    copy = ([   [-5,-3, -3.25, -9, -10, -3.25, -3, -5],
                [-1,-1, -1,    -1,  -1, -1,    -1, -1],
                [ 0, 0,  0,     0,   0,  0,     0,  0],
                [ 0, 0,  0,     0,   0,  0,     0,  0],
                [ 0, 0,  0,     0,   0,  0,     0,  0],
                [ 0, 0,  0,     0,   0,  0,     0,  0],
                [ 1, 1,  1,     1,   1,  1,     1,  1],
                [ 5, 3,  3.25,  9,  10,  3.25,  3,  5]])
    
    for row in range(0, 8):
        for col in range(0, 8):
            copy[row][col] = board[row][col]

    return copy


def is_stalemate(game):
    piece = None
    moves = []
    legal__moves = []

    if game.current_player_turn == -1:
        for row in range(0, 8):
            for col in range(0, 8):
                if game.board[row][col] < 0:
                    piece = piece_caller(game.board[row][col])
                    moves = piece.legal_moves([row, col], game)
                    for move in moves:
                        if not in_check(game, [row, col], move):
                            legal__moves.append(move)
    else:
        for row in range(0, 8):
            for col in range(0, 8):
                if game.board[row][col] > 0:
                    piece = piece_caller(game.board[row][col])
                    moves = piece.legal_moves([row, col], game)
                    for move in moves:
                        if not in_check(game, [row, col], move):
                            legal__moves.append(move)


def is_repitition(game):
    len_states = len(game.is_repitition_states)

    for index in range(0, len_states):
        counter = 0
        for index_cmp in range(0, len_states):
            if index != index_cmp:
                if game.is_repitition_states[index] == game.is_repitition_states[index_cmp]:
                    counter += 1
                    if counter == 3:
                        return True
                    
    return False


def game_ended(game):
    if is_checkmate(game):
        if game.current_player_turn == 1:
            print("Checkmate, Black wins")
            return True
        else:
            print("Checkmate, White wins")
            return True
    elif is_stalemate(game):
        if game.current_player_turn == 1:
            print("Stalemate, White has no legal moves")
            return True
        else:
            print("Stalemate, Black has no legal moves")
            return True
    elif is_repitition(game):
        print("Draw by repitition")
        return True
    else:
        return False
            

def end_statement(game):
    print("Ex:")
    print("White: [piece, starting position, ending position], Black: [piece, starting position, ending position]")
    for row in game.moves:
        print(row)


def update_repitition_states(game, move, notation):
    if (abs(game.board[move[1][0]][move[1][1]]) == 1) or is_capture_notation(notation):
        game.is_repitition_states = []

    (game.is_repitition_states).append(copy_board(game.board))

    return
    

def find_moves(game):
    verified_moves = []

    if game.current_player_turn == -1:
        for row in range(0, 8):
            for col in range(0, 8):
                if game.board[row][col] < 0:
                    piece = piece_caller(game.board[row][col])
                    moves = piece.legal_moves([row, col], game)

                    for move in moves:
                        if not in_check(game, [row, col], move):
                            verified_moves.append(move)
    else:
        for row in range(0, 8):
            for col in range(0, 8):
                if game.board[row][col] > 0:
                    piece = piece_caller(game.board[row][col])
                    moves = piece.legal_moves([row, col], game)

                    for move in moves:
                        if not in_check(game, [row, col], move):
                            verified_moves.append([num_to_letter(piece.value), move])
                            

    return verified_moves
