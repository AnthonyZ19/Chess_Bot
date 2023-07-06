
def main():
    current_game = chess()
    piece = king(-1)
    moves = piece.legal_moves(([0, 4]), current_game)
    print(moves)


# Stores chess game info
class chess:
    def __init__(self):
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

        self.last_move_end_pos = []

        self.last_move_en_passant = False

        self.current_player_turn = 1


class pawn:
    def __init__(self, color):
        # "color" is -1 for black and 1 for white
        self.side = color
        self.value = (1 * color)

    def legal_moves(self, position, game):
        # Stores legal moves for this piece in the following list
        pawn_moves = []
        board_state = game.board
        # Checks moves if the piece color is black
        if self.side == -1:
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

        # Checks moves if the piece is white
        else:
            # Checks if it can move forward
            if board_state[(position[0] - 1)][position[1]] == 0:
                pawn_moves.append([(position[0] - 1), position[1]])
                if position[0] == 6:
                    if board_state[(position[0] - 2)][position[1]] == 0:
                        pawn_moves.append([(position[0] - 2), position[1]])

            # Checks if the piece can take another
            if (position[0] > 0) and (position[1] < 7):
                if board_state[(position[0] - 1)][position[1] + 1] > 0:
                    pawn_moves.append([(position[0] - 1), (position[1] + 1)])

            if (position[0] > 0) and (position[1] > 0):
                if board_state[(position[0] - 1)][position[1] - 1] > 0:
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
    def legal_moves(self, position, game):
        king_moves = []
        board_state = game.board
        
        if self.side == -1:
            # Loops through all the squares around the king
            for y in [-1, 0, 1]:
                for x in [-1, 0, 1]:
                    if ((position[0] + y) >= 0) and ((position[0] + y) < 8):
                        if ((position[1] + x) >= 0) and ((position[1] + x) < 8):
                            if board_state[(position[0] + y)][(position[1] + x)] >= 0:
                                # Checks if the square is attacked by enemy pieces
                                if not in_check(game, self, position, [(position[0] + y), (position[1] + x)]):
                                    king_moves.append([(position[0] + y), (position[1] + x)])

            # Checks if the king can castle
            if not(game.black_king_moved):
                # Checks long castle
                if not(game.rook_a8_moved):
                    if (board_state[position[0]][position[1] - 1] == 0) and (board_state[position[0]][position[1] - 2] == 0) and (board_state[position[0]][position[1] - 3] == 0):
                        king_moves.append([position[0], (position[1] - 2)])
                # Checks short castle
                if not(game.rook_h8_moved):
                    if (board_state[position[0]][position[1] + 1] == 0) and (board_state[position[0]][position[1] + 2] == 0):
                        king_moves.append([position[0], (position[1] + 2)])
        else:
            # Loops through all the squares around the king
            for y in [-1, 0, 1]:
                for x in [-1, 0, 1]:
                    if ((position[0] + y) >= 0) and ((position[0] + y) < 8):
                        if ((position[1] + x) >= 0) and ((position[1] + x) < 8):
                            if board_state[(position[0] + y)][(position[1] + x)] <= 0:
                                # Checks if the square is attacked by enemy pieces
                                if not in_check(board_state, self, position, [(position[0] + y), (position[1] + x)]):
                                    king_moves.append([(position[0] + y), (position[1] + x)])

            # Checks if the king can castle
            if not(game.white_king_moved):
                # Checks long castle
                if not(game.rook_a1_moved):
                    if (board_state[position[0]][position[1] - 1] == 0) and (board_state[position[0]][position[1] - 2] == 0) and (board_state[position[0]][position[1] - 3] == 0):
                        king_moves.append([position[0], (position[1] - 2)])
                # Checks short castle
                if not(game.rook_h1_moved):
                    if (board_state[position[0]][position[1] + 1] == 0) and (board_state[position[0]][position[1] + 2] == 0):
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
    

def in_check(game, piece, start_pos, end_pos):
    # Makes the tested move in order to check for checks
    king_position = []
    board_state = game.board
    board_state[start_pos[0]][start_pos[1]] = 0
    board_state[end_pos[0]][end_pos[1]] = piece.value

    # Checks for checks for the black pieces
    if piece.side == -1:
        # Finds the king
        for row in range(0, 8):
            for square in range(0, 8):
                if board_state[row][square] == -10:
                    king_position = [row, square]
        # Iterates through each row and square
        for row in range(0, 8):
            for square in range(0, 8):
                # Checks if an enemy piece is in the position/square
                if board_state[row][square] > 0:
                    # If yes, it calls that piece and checks it's legal moves
                    enemy_piece = piece_caller(board_state[row][square])
                    enemy_moves = enemy_piece.legal_moves([row, square], game)
                    # If any of it's moves hits the king, if it were to move into that square
                    #  then True is returned
                    if king_position in enemy_moves:
                        board_state[start_pos[0]][start_pos[1]] = piece.value
                        board_state[end_pos[0]][end_pos[1]] = 0
                        return True
    # Same as before, but for white
    else:
        # Iterates through each row and square
        for row in range(0, 8):
            for square in range(0, 8):
                # Checks if an enemy piece is in the position/square
                if board_state[row][square] > 0:
                    # If yes, it calls that piece and checks it's legal moves
                    enemy_piece = piece_caller(board_state[row][square])
                    enemy_moves = enemy_piece.legal_moves([row, square], game)
                    # If any of it's moves hits the king, if it were to move into that square
                    #  then True is returned
                    if end_pos in enemy_moves:
                        board_state[start_pos[0]][start_pos[1]] = piece.value
                        board_state[end_pos[0]][end_pos[1]] = 0
                        return True
    # If none of the enemy pieces hit's the king were it to move into that square
    # Then False is returned
    board_state[start_pos[0]][start_pos[1]] = piece.value
    board_state[end_pos[0]][end_pos[1]] = 0
    return False



def make_move(game, start_pos, end_pos):
    piece = piece_caller(game.board[start_pos[0]][start_pos[1]])
    if end_pos in piece.legal_moves(start_pos, game.board):
        # Checks that the piece is the black king
        if piece.value == -10:
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
        elif piece.value == 10:
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

        if in_check(game, piece, start_pos, end_pos):
            return False
        else:
            game.board[start_pos[0]][start_pos[1]] = 0
            game.board[end_pos[0]][end_pos[1]] = piece.value
            return True


main()