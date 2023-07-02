board = [[-5, -3, -3.25, -9, -10, -3.25, -3, -5],
         [-1,-1,  -1,    -1,  -1, -1,    -1, -1],
         [0,  0,   0,     0,   0,  0,     0,  0],
         [0,  0,   0,     0,   0,  0,     0,  0],
         [0,  0,   0,     0,   0,  0,     0,  0],
         [0,  0,   0,     0,   0,  0,     0,  0],
         [1,  1,   1,     1,   1,  1,     1,  1],
         [5,  3, 3.25,    9,  10, 3.25,   3,  5]]


class pawn:
    def __init__(self, color):
        # "color" is -1 for black and 1 for white
        self.side = color
        self.firstMove = True

    def legal_moves(self, position):
        # Stores legal moves for this piece in the following list
        pawn_moves = []
        # Checks moves if the piece color is black
        if self.side == -1:
            # Checks if the piece can move forward
            if board[(position[0] + 1)][position[1]] == 0:
                pawn_moves.append([(position[0] + 1), position[1]])
                if self.firstMove:
                    if board[(position[0] + 2)][position[1]] == 0:
                        pawn_moves.append([(position[0] + 2), position[1]])

            # Checks if it can take any pieces
            if (position[0] < 7) and (position[1] < 7):
                if board[(position[0] + 1)][position[1] + 1] > 0:
                    pawn_moves.append([(position[0] + 1), (position[1] + 1)])

            if (position[0] < 7) and (position[1] > 0):
                if board[(position[0] + 1)][position[1] - 1] > 0:
                    pawn_moves.append([(position[0] + 1), (position[1] - 1)])

        # Checks moves if the piece is white
        else:
            # Checks if it can move forward
            if board[(position[0] - 1)][position[1]] == 0:
                pawn_moves.append([(position[0] - 1), position[1]])
                if self.firstMove:
                    if board[(position[0] - 2)][position[1]] == 0:
                        pawn_moves.append([(position[0] - 2), position[1]])

            # Checks if the piece can take another
            if (position[0] > 0) and (position[1] < 7):
                if board[(position[0] - 1)][position[1] + 1] > 0:
                    pawn_moves.append([(position[0] - 1), (position[1] + 1)])

            if (position[0] > 0) and (position[1] > 0):
                if board[(position[0] - 1)][position[1] - 1] > 0:
                    pawn_moves.append([(position[0] - 1), (position[1] - 1)])
        return pawn_moves


class bishop:
    def __init__(self, color):
        # "color" is -1 for black and 1 for white
        self.side = color

    def legal_moves(self, position):
        # Stores the legal moves for the bishop
        bishop_moves = []

        # Checks moves for when the piece is white
        if self.side == -1:
            increment = 1

            # Repeatedly checks if the bishop can move to each square it can see based on the previous variables
            while True:
                # Try is used to prevent error in case the position that is being checked is out of range and stops the loop
                try:
                    # Checks if the spot is unoccupied or occupied by an enemy piece
                    if board[(position[0] + increment)][(position[1] + increment)] >= 0:
                        # Adds the spot to the list of legal moves
                        bishop_moves.append([(position[0] + increment), (position[1] + increment)])
                        
                    # Checks if the spot is empty
                    if board[(position[0] + increment)][(position[1] + increment)] != 0:
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
                        if board[(position[0] - increment)][(position[1] - increment)] >= 0:
                            # Adds the spot to the list of legal moves
                            bishop_moves.append([(position[0] - increment), (position[1] - increment)])

                        # Checks if the spot is empty
                        if board[(position[0] - increment)][(position[1] - increment)] != 0:
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
                        if board[(position[0] - increment)][(position[1] + increment)] >= 0:
                            # Adds the spot to the list of legal moves
                            bishop_moves.append([(position[0] - increment), (position[1] + increment)])

                        # Checks if the spot is empty
                        if board[(position[0] - increment)][(position[1] + increment)] != 0:
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
                        if board[(position[0] + increment)][(position[1] - increment)] >= 0:
                            # Adds the spot to the list of legal moves
                            bishop_moves.append([(position[0] + increment), (position[1] - increment)])

                        # Checks if the spot is empty
                        if board[(position[0] + increment)][(position[1] - increment)] != 0:
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
                    # Checks if the spot is unoccupied or occupied by an enemy piece
                    if board[(position[0] + increment)][(position[1] + increment)] <= 0:
                        # Adds the spot to the list of legal moves
                        bishop_moves.append([(position[0] + increment), (position[1] + increment)])
                             
                    # Checks if the spot is empty
                    if board[(position[0] + increment)][(position[1] + increment)] != 0:
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
                        if board[(position[0] - increment)][(position[1] - increment)] <= 0:
                            # Adds the spot to the list of legal moves
                            bishop_moves.append([(position[0] - increment), (position[1] - increment)])

                        # Checks if the spot is empty
                        if board[(position[0] - increment)][(position[1] - increment)] != 0:
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
                        if board[(position[0] - increment)][(position[1] + increment)] <= 0:
                            # Adds the spot to the list of legal moves
                            bishop_moves.append([(position[0] - increment), (position[1] + increment)])

                        # Checks if the spot is empty
                        if board[(position[0] - increment)][(position[1] + increment)] != 0:
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
                        # Checks if the spot is unoccupied or occupied by an enemy piece
                        if board[(position[0] + increment)][(position[1] - increment)] <= 0:
                            # Adds the spot to the list of legal moves
                            bishop_moves.append([(position[0] + increment), (position[1] - increment)])

                        # Checks if the spot is empty
                        if board[(position[0] + increment)][(position[1] - increment)] != 0:
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
    def legal_moves(self, position):
        # Stores legal moves for the knight
        knight_moves = []

        # Checks legal moves for a black knight 
        if self.side == -1:
            # Checks legal moves in which the knight moves by 2 vertically
            for y in [2, -2]:
                for x in [1, -1]:
                    # Try in case the position is out of range
                    try:
                        # Makes sure that the index isn't negative
                        if ((position[0] + y) >= 0) and ((position[1] + x) >= 0):
                            if board[(position[0] + y)][position[1] + x] >= 0:
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
                            if board[(position[0] + y)][position[1] + x] >= 0:
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
                            if board[(position[0] + y)][position[1] + x] <= 0:
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
                            if board[(position[0] + y)][position[1] + x] <= 0:
                                # If the square is empty and not another black piece the move is appended
                                knight_moves.append([(position[0] + y), (position[1] + x)])
                    except:
                        continue
        return knight_moves


class rook:
    def __init__(self, color):
        # "color" is -1 for black and 1 for white
        self.side = color
    def legal_moves(self, position):
        # Stores legal moves for the rook
        rook_moves = []

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
                            if board[(position[0] + increment)][position[1]] >= 0:
                                rook_moves.append([(position[0] + increment), position[1]])
                            # Checks if the position is occupied to prevent the rook from jumping over pieces
                            if board[(position[0] + increment)][position[1]] != 0:
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
                            if board[position[0]][(position[1] + increment)] >= 0:
                                rook_moves.append([position[0], (position[1] + increment)])
                                # Checks if the position is occupied to prevent the rook from jumping over pieces
                            if board[position[0]][(position[1] + increment)] != 0:
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
                            if board[(position[0] + increment)][position[1]] <= 0:
                                rook_moves.append([(position[0] + increment), position[1]])
                            # Checks if the position is occupied to prevent the rook from jumping over pieces
                            if board[(position[0] + increment)][position[1]] != 0:
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
                            if board[position[0]][(position[1] + increment)] <= 0:
                                rook_moves.append([position[0], (position[1] + increment)])
                                # Checks if the position is occupied to prevent the rook from jumping over pieces
                            if board[position[0]][(position[1] + increment)] != 0:
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
    def legal_moves(self, position):
        queen_moves = []

        # Since the queen moves like a bishop and rook combined, I just call their classes and combine the legal moves for both
        bishop1 = bishop(self.side)
        rook1 = rook(self.side)

        # Stores the legal moves of the queen as if it were a bishop and rook
        bishop_moves = bishop1.legal_moves(position)
        rook_moves = rook1.legal_moves(position)
        
        # Combines the moves into a list of legal moves for the queen
        for moves in [bishop_moves, rook_moves]:
            for move in moves:
                queen_moves.append(move)

        return queen_moves


class king:
    def __init__(self, color):
        # "color" is -1 for black and 1 for white
        self.side = color
    def legal_moves(self, position):
        king_moves = []
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
    

def attacks(color, board_state):
    # Stores position attacked
    attacked = []
    # Tracks what row is being checked
    row_index = 0

    # Checks attacks for the black pieces
    if color < 0:
        for row in board_state:
            # Tracks the column being checked per row
            square_index = 0
            for square in row:
                # Ensures that it's a black piece
                if square < 0:
                    # Gets and stores the moves of the piece
                    moves = piece_caller(square).legal_moves([row_index, square_index])
                    
                    # Ensures the list isn't empty
                    if moves:
                        for move in moves:
                            # Ensures the list isn't empty
                            if move:
                                # Checks if it's an enemy piece that can be taken
                                if board_state[move[0]][move[1]] > 0:
                                    attacked.append(move)
                    square_index += 1
            row_index += 1
    else:
        for row in board_state:
            # Tracks the column being checked per row
            square_index = 0
            for square in row:
                # Ensures that it's a white piece
                if square > 0:
                    # Gets and stores the moves of the piece
                    moves = piece_caller(square).legal_moves([row_index, square_index])
                    
                    # Ensures the list isn't empty
                    if moves:
                        for move in moves:
                            # Ensures the list isn't empty
                            if move:
                                # Checks if it's an enemy piece that can be taken
                                if board_state[move[0]][move[1]] < 0:
                                    attacked.append(move)
                    square_index += 1
            row_index += 1
    return attacked


h1 = queen(-1)
h1_moves = h1.legal_moves([3, 3])
#print(h1_moves)
print(attacks(-1, board))