board = [[-5, -3, -3.25, -9, -10, -3.25, -3, -5],
         [-1, 1, -1,    -1,  -1, -1,    -1, -1],
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
            # Variables used to track how far the bishop can move
            inRange = True
            unBlocked = True
            increment = 1

            # Repeatedly checks if the bishop can move to each square it can see based on the previous variables
            while inRange and unBlocked:
                # Try is used to prevent error in case the position that is being checked is out of range and stops the loop
                try:
                    # Checks if the spot is unoccupied or occupied by an enemy piece
                    if board[(position[0] + increment)][(position[1] + increment)] >= 0:
                        # Adds the spot to the list of legal moves
                        bishop_moves.append([(position[0] + increment), (position[1] + increment)])
                        
                    # Checks if the spot is empty
                    if board[(position[0] + increment)][(position[1] + increment)] != 0:
                        # Takes note that the bishop is blocked in this direction and can't see further
                        unBlocked = False
                    increment += 1
                except:
                    inRange = False


            # Variables to track the bishop's range are reset and a new one is used to for when it goes in the other direction on the same diagonal
            inRange = True
            unBlocked = True
            increment = 1

            # Repeatedly checks if the bishop can move to each square it can see based on the previous variables
            while inRange and unBlocked:
                # Try is used to prevent error in case the position that is being checked is out of range and stops the loop
                try:
                    if ((position[0] - increment) >= 0) and ((position[1] - increment) >= 0):
                        # Checks if the spot is unoccupied or occupied by an enemy piece
                        if board[(position[0] - increment)][(position[1] - increment)] >= 0:
                            # Adds the spot to the list of legal moves
                            bishop_moves.append([(position[0] - increment), (position[1] - increment)])

                        # Checks if the spot is empty
                        if board[(position[0] - increment)][(position[1] - increment)] != 0:
                            # Takes note that the bishop is blocked in this direction and can't see further
                            unBlocked = False
                        increment += 1
                    else:
                        inRange = False
                except:
                    inRange = False

            # Variables to track the bishop's range are reset
            inRange = True
            unBlocked = True
            increment = 1

            # Repeatedly checks if the bishop can move to each square it can see based on the previous variables
            while inRange and unBlocked:
                # Try is used to prevent error in case the position that is being checked is out of range and stops the loop
                try:
                    if ((position[0] - increment) >= 0):
                        # Checks if the spot is unoccupied or occupied by an enemy piece
                        if board[(position[0] - increment)][(position[1] + increment)] >= 0:
                            # Adds the spot to the list of legal moves
                            bishop_moves.append([(position[0] - increment), (position[1] + increment)])

                        # Checks if the spot is empty
                        if board[(position[0] - increment)][(position[1] + increment)] != 0:
                            # Takes note that the bishop is blocked in this direction and can't see further
                            unBlocked = False
                        increment += 1
                    else:
                        inRange = False
                except:
                    inRange = False  

            # Variables to track the bishop's range are reset
            inRange = True
            unBlocked = True
            increment = 1

            # Repeatedly checks if the bishop can move to each square it can see based on the previous variables
            while inRange and unBlocked:
                # Try is used to prevent error in case the position that is being checked is out of range and stops the loop
                try:
                    if ((position[1] - increment) >= 0):
                        # Checks if the spot is unoccupied or occupied by an enemy piece
                        if board[(position[0] + increment)][(position[1] - increment)] >= 0:
                            # Adds the spot to the list of legal moves
                            bishop_moves.append([(position[0] + increment), (position[1] - increment)])

                        # Checks if the spot is empty
                        if board[(position[0] + increment)][(position[1] - increment)] != 0:
                            # Takes note that the bishop is blocked in this direction and can't see further
                            unBlocked = False
                        increment += 1
                    else:
                        inRange = False
                except:
                    inRange = False

        else:
            # Variables used to track how far the bishop can move
            inRange = True
            unBlocked = True
            increment = 1

            # Repeatedly checks if the bishop can move to each square it can see based on the previous variables
            while inRange and unBlocked:
                # Try is used to prevent error in case the position that is being checked is out of range and stops the loop
                try:
                    # Checks if the spot is unoccupied or occupied by an enemy piece
                    if board[(position[0] + increment)][(position[1] + increment)] <= 0:
                        # Adds the spot to the list of legal moves
                        bishop_moves.append([(position[0] + increment), (position[1] + increment)])
                             
                    # Checks if the spot is empty
                    if board[(position[0] + increment)][(position[1] + increment)] != 0:
                        # Takes note that the bishop is blocked in this direction and can't see further
                        unBlocked = False
                    increment += 1
                except:
                    inRange = False

            # Variables to track the bishop's range are reset and a new one is used to for when it goes in the other direction on the same diagonal
            inRange = True
            unBlocked = True
            increment = 1

            # Repeatedly checks if the bishop can move to each square it can see based on the previous variables
            while inRange and unBlocked:
                # Try is used to prevent error in case the position that is being checked is out of range and stops the loop
                try:
                    if ((position[0] - increment) >= 0) and ((position[1] - increment) >= 0):
                        # Checks if the spot is unoccupied or occupied by an enemy piece
                        if board[(position[0] - increment)][(position[1] - increment)] <= 0:
                            # Adds the spot to the list of legal moves
                            bishop_moves.append([(position[0] - increment), (position[1] - increment)])

                        # Checks if the spot is empty
                        if board[(position[0] - increment)][(position[1] - increment)] != 0:
                            # Takes note that the bishop is blocked in this direction and can't see further
                            unBlocked = False
                        increment += 1
                    else:
                        inRange = False
                except:
                    inRange = False

            # Variables to track the bishop's range are reset
            inRange = True
            unBlocked = True
            increment = 1

            # Repeatedly checks if the bishop can move to each square it can see based on the previous variables
            while inRange and unBlocked:
                # Try is used to prevent error in case the position that is being checked is out of range and stops the loop
                try:
                    if ((position[0] - increment) >= 0):
                        # Checks if the spot is unoccupied or occupied by an enemy piece
                        if board[(position[0] - increment)][(position[1] + increment)] <= 0:
                            # Adds the spot to the list of legal moves
                            bishop_moves.append([(position[0] - increment), (position[1] + increment)])

                        # Checks if the spot is empty
                        if board[(position[0] - increment)][(position[1] + increment)] != 0:
                            # Takes note that the bishop is blocked in this direction and can't see further
                            unBlocked = False
                        increment += 1
                    else:
                        inRange = False
                except:
                    inRange = False  

            # Variables to track the bishop's range are reset
            inRange = True
            unBlocked = True
            increment = 1

            # Repeatedly checks if the bishop can move to each square it can see based on the previous variables
            while inRange and unBlocked:
                # Try is used to prevent error in case the position that is being checked is out of range and stops the loop
                try:
                    if ((position[1] - increment) >= 0):
                        # Checks if the spot is unoccupied or occupied by an enemy piece
                        if board[(position[0] + increment)][(position[1] - increment)] <= 0:
                            # Adds the spot to the list of legal moves
                            bishop_moves.append([(position[0] + increment), (position[1] - increment)])

                        # Checks if the spot is empty
                        if board[(position[0] + increment)][(position[1] - increment)] != 0:
                            # Takes note that the bishop is blocked in this direction and can't see further
                            unBlocked = False
                        increment += 1
                    else:
                        inRange = False
                except:
                    inRange = False
                        
            return bishop_moves


h1 = bishop(1)
h1_moves = h1.legal_moves([7, 2])
print(h1_moves)