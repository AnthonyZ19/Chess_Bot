board = [[-5, -3, -3.25, -9, -10, -3.25, -3, -5],
         [-1, -1, -1,    -1,  -1, -1,    -1, -1],
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
        bishop_moves = []

        if self.side == -1:
            inRange = True
            unBlocked = True
            increment = 1

            while inRange and unBlocked:
                try:
                    if board[(position[0] + increment)][(position[1] + increment)] >= 0:
                        bishop_moves.append([(position[0] + increment), (position[1] + increment)])
                        
                    if board[(position[0] + increment)][(position[1] + increment)] != 0:
                        unBlocked = False
                        if board[(position[0] + increment)][(position[1] + increment)] > 0:
                            bishop_moves.append([(position[0] + increment), (position[1] + increment)])
                    increment += 1
                except:
                    inRange = False


            inRange = True
            unBlocked = True
            increment2 = -1

            while inRange and unBlocked:
                try:
                    if board[(position[0] + increment2)][(position[1] + increment2)] >= 0:
                        bishop.append([(position[0] + increment2), (position[1] + increment2)])

                    if board[(position[0] + increment2)][(position[1] + increment2)] != 0:
                        unBlocked = False
                        if board[(position[0] + increment2)][(position[1] + increment2)] > 0:
                            bishop_moves.append([(position[0] + increment2), (position[1] + increment2)])
                    increment2 -= 1
                except:
                    inRange = False

            inRange = True
            unBlocked = True
            increment = 1
            increment2 = -1

            while inRange and unBlocked:
                try:
                    if board[(position[0] + increment2)][(position[1] + increment)] >= 0:
                        bishop.append([(position[0] + increment2), (position[1] + increment)])

                    if board[(position[0] + increment2)][(position[1] + increment)] != 0:
                        unBlocked = False
                        if board[(position[0] + increment2)][(position[1] + increment)] > 0:
                            bishop_moves.append([(position[0] + increment2), (position[1] + increment)])
                    increment += 1
                    increment2 -= 1
                except:
                    inRange = False  

            inRange = True
            unBlocked = True
            increment = 1
            increment2 = -1

            while inRange and unBlocked:
                try:
                    if board[(position[0] + increment)][(position[1] + increment2)] >= 0:
                        bishop.append([(position[0] + increment), (position[1] + increment2)])

                    if board[(position[0] + increment)][(position[1] + increment2)] != 0:
                        unBlocked = False
                        if board[(position[0] + increment)][(position[1] + increment2)] > 0:
                            bishop_moves.append([(position[0] + increment), (position[1] + increment2)])
                    increment += 1
                    increment2 -= 1
                except:
                    inRange = False
            
            return bishop_moves


h1 = bishop(-1)
h1_moves = h1.legal_moves([0, 2])
print(h1_moves)