import numpy as np

pieces_to_ids = {
    # Red Uninvolved Pieces
    'r1': 1, 'r2': 2, 'r3': 3, 'r4': 4,
    'r5': 5, 'r6': 6, 'r7': 7, 'r8': 8,
    'r9': 9, 'r10': 10, 'r11': 11, 'r12': 12,
    # Red Envolved Pieces
    'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4,
    'R5': 5, 'R6': 6, 'R7': 7, 'R8': 8,
    'R9': 9, 'R10': 10, 'R11': 11, 'R12': 12,
    # Blue Unevolved Pieces
    'b1': -1, 'b2': -2, 'b3': -3, 'b4': -4,
    'b5': -5, 'b6': -6, 'b7': -7, 'b8': -8,
    'b9': -9, 'b10': -10, 'b11': -11, 'b12': -12,
    # Blue Evolved
    'B1': -1, 'B2': -2, 'B3': -3, 'B4': -4,
    'B5': -5, 'B6': -6, 'B7': -7, 'B8': -8,
    'B9': -9, 'B10': -10, 'B11': -11, 'B12': -12,
}

blueMap = ['none', 'v', 'v', 'v', 'v', 'h', 'h',
           'h', 'h', 'v', 'v', 'v', 'v']  # CAPS if Evolved
redMap = ['none', 'v', 'v', 'h', 'h', 'h', 'h',
          'h', 'h', 'h', 'h', 'v', 'v']  # CAPS if Evolved
board = np.array([[0, -1, 1, -2, -3, 2, -4, 0],
         [3, 0, 0, 0, 0, 0, 0, 4],
         [-5, 0, 0, 0, 0, 0, 0, -6],
         [5, 0, 0, 0, 0, 0, 0, 6],
         [7, 0, 0, 0, 0, 0, 0, 8],
         [-7, 0, 0, 0, 0, 0, 0, -8],
         [9, 0, 0, 0, 0, 0, 0, 10],
         [0, -9, 11, -10, -11, 12, -12, 0]])


def check_valid_square_red(board, lin, col):
    inPos = board[lin, col]
    if inPos > 0:
        return False
    return True


def check_valid_square_blue(board, lin, col):
    inPos = board[lin, col]
    if inPos < 0:
        return False
    return True


def check_piece_in(board, lin, col):
    return not board[lin, col] == 0


def check_piece_evolved(id):
    if id > 0 and (redMap[id] == 'H' or redMap[id] == 'V'):
        return True
    elif id < 0 and (blueMap[id*(-1)] == 'H' or blueMap[id*(-1)] == 'V'):
        return True
    return False


def get_piece_orientation(id):
    if id > 0:
        return redMap[id]
    return blueMap[id*(-1)]

def check_piece_in_corner(lin, col):
    return (lin == 0 and col == 0) or (lin == 0 and col == 7) or (lin == 7 and col == 7) or (lin == 7 and col == 0)



def generate_valid_moves_rh(board, lin, col):
    # Initialize arrays to store positions and moves
    valid_positions = []
    total_moves = []

    # Get the piece id from the board
    piece_id = board[lin, col]

    # Initialize variables to help navigate the board
    i = 0
    deltaCol = col + 1

    # Check Positions to the Right
    while deltaCol < 8:
        if (i % 2 == 0 or check_piece_evolved(piece_id)) and check_valid_square_red(board, lin, deltaCol):
            valid_positions.append(((lin, col), (lin, deltaCol)))

        if check_piece_in(board, lin, deltaCol):
            break

        i += 1
        deltaCol += 1

    # Reinitialize the variables to help navigate the board the opposite way
    deltaCol = col - 1
    i = 0

    # Check Positions to the Left
    while deltaCol >= 0:
        if (i % 2 == 0 or check_piece_evolved(piece_id)) and check_valid_square_red(board, lin, deltaCol):
            valid_positions.append(((lin, col), (lin, deltaCol)))

        if check_piece_in(board, lin, deltaCol):
            break

        i += 1
        deltaCol -= 1

    # Transforme Positions into moves
    for m in valid_positions:
        total_moves.append({
            'piece': piece_id,
            'pos': m[0],
            'new_pos': m[1],
            'type': 'move'
        })

    return total_moves


def generate_valid_moves_rv(board, lin, col):
    # Initialize arrays to store positions and moves
    valid_positions = []
    total_moves = []

    # Get the piece id from the board
    piece_id = board[lin, col]

    # Initialize variables to help navigate the board
    i = 0
    deltaLin = lin + 1

    # Check Upper Positions
    while deltaLin < 8:
        if (i % 2 == 0 or check_piece_evolved(piece_id)) and check_valid_square_red(board, deltaLin, col):
            valid_positions.append(((lin, col), (deltaLin, col)))

        if check_piece_in(board, deltaLin, col):
            break

        i += 1
        deltaLin += 1

    # Reinitialize the variables to help navigate the board the opposite way
    deltaLin = lin - 1
    i = 0

    # Check Down Positions
    while deltaLin >= 0:
        if (i % 2 == 0 or check_piece_evolved(piece_id)) and check_valid_square_red(board, deltaLin, col):
            valid_positions.append(((lin, col), (deltaLin, col)))

        if check_piece_in(board, deltaLin, col):
            break

        i += 1
        deltaLin -= 1

    # Transforme Positions into moves
    for m in valid_positions:
        total_moves.append({
            'piece': piece_id,
            'pos': m[0],
            'new_pos': m[1],
            'type': 'move'
        })

    return total_moves


def generate_valid_moves_bh(board, lin, col):
    # Initialize arrays to store positions and moves
    valid_positions = []
    total_moves = []

    # Get the piece id from the board
    piece_id = board[lin, col]

    # Initialize variables to help navigate the board
    i = 0
    deltaCol = col + 1

    # Check Positions to the Right
    while deltaCol < 8:

        if (i % 2 == 0 or check_piece_evolved(piece_id)) and check_valid_square_blue(board, lin, deltaCol):
            valid_positions.append(((lin, col), (lin, deltaCol)))

        if check_piece_in(board, lin, deltaCol):
            break

        i += 1
        deltaCol += 1

    # Reinitialize the variables to help navigate the board the opposite way
    deltaCol = col - 1
    i = 0

    # Check Positions to the Left
    while deltaCol >= 0:

        if (i % 2 == 0 or check_piece_evolved(piece_id)) and check_valid_square_blue(board, lin, deltaCol):
            valid_positions.append(((lin, col), (lin, deltaCol)))

        if check_piece_in(board, lin, deltaCol):
            break

        i += 1
        deltaCol -= 1

    # Transforme Positions into moves
    for m in valid_positions:
        total_moves.append({
            'piece': piece_id,
            'pos': m[0],
            'new_pos': m[1],
            'type': 'move'
        })

    return total_moves


def generate_valid_moves_bv(board, lin, col):
    # Initialize arrays to store positions and moves
    valid_positions = []
    total_moves = []

    # Get the piece id from the board
    piece_id = board[lin, col]

    # Initialize variables to help navigate the board
    i = 0
    deltaLin = lin + 1

    # Check Upper Positions
    while deltaLin < 8:

        if (i % 2 == 0 or check_piece_evolved(piece_id)) and check_valid_square_blue(board, deltaLin, col):
            valid_positions.append(((lin, col), (deltaLin, col)))

        if check_piece_in(board, deltaLin, col):
            break

        i += 1
        deltaLin += 1

    # Reinitialize the variables to help navigate the board the opposite way
    deltaLin = lin - 1
    i = 0

    # Check Down Positions
    while deltaLin >= 0:

        if (i % 2 == 0 or check_piece_evolved(piece_id)) and check_valid_square_blue(board, deltaLin, col):
            valid_positions.append(((lin, col), (deltaLin, col)))

        if check_piece_in(board, deltaLin, col):
            break

        i += 1
        deltaLin -= 1

    # Transforme Positions into moves
    for m in valid_positions:
        total_moves.append({
            'piece': piece_id,
            'pos': m[0],
            'new_pos': m[1],
            'type': 'move'
        })

    return total_moves


# def generate_valid_moves_r(board):
#     valid_moves = []
#     #for position, piece_id in np.ndenumerate(board):
#         #if piece_id > 0:
#             if redMap[piece_id] == 'h' or redMap[piece_id] == 'H':
#                 valid_moves += generate_valid_moves_rh(
#                     board, position[0], position[1])
#             elif redMap[piece_id] != 'none':
#                 valid_moves += generate_valid_moves_rv(
#                     board, position[0], position[1])
#     return valid_moves


def generate_valid_moves_b(board):
    valid_moves = []

    for position, piece_id in np.ndenumerate(board):
        if piece_id < 0:
            piece_id *= -1
            if blueMap[piece_id] == 'h' or blueMap[piece_id] == 'H':
                valid_moves += generate_valid_moves_bh(board, position[0], position[1])

            elif blueMap[piece_id] != 'none':
                valid_moves += generate_valid_moves_bv(board, position[0], position[1])

            else: print(piece_id)

    return valid_moves

# Inverts the orientation of the piece
def pivot(piece_id):
    if piece_id > 0:
        if redMap[piece_id] == 'v':
            redMap[piece_id] = 'h'
        elif redMap[piece_id] == 'h':
            redMap[piece_id] = 'v'
        elif redMap[piece_id] == 'V':
            redMap[piece_id] = 'H'
        elif redMap[piece_id] == 'H':
            redMap[piece_id] = 'V'
    else:
        piece_id *= -1
        if blueMap[piece_id] == 'v':
            blueMap[piece_id] = 'h'
        elif blueMap[piece_id] == 'h':
            blueMap[piece_id] = 'v'
        elif blueMap[piece_id] == 'V':
            blueMap[piece_id] = 'H'
        elif blueMap[piece_id] == 'H':
            blueMap[piece_id] = 'V'

# Evolves a piece
def evolve(piece_id):
    if piece_id > 0:
        redMap[piece_id].upper()
    else:
        blueMap[piece_id].upper()

# Removes a piece from the game
def kill(piece_id):
    if piece_id > 0:
        redMap[piece_id] = 'none'
    else:
        blueMap[piece_id] = 'none'

# Checks if the game is over
def isDone():
    for redStatus, blueStatus in zip(redMap, blueMap):
        if (redStatus != 'none' and redStatus.islower()) or (blueStatus != 'none' and blueStatus.islower()) :
            return False
    return True


# Searches for a piece in the board
def get_piece_position(id):
    for position, piece_id in np.ndenumerate(board):
        if piece_id == id:
            return position

def move_to_action(move):
    piece_id = move['piece_id']
    new_pos = move['new_pos']
    return 64*(abs(piece_id) - 1) + (new_pos[0] * 8 + new_pos[1])

def action_to_move(action, player):
    square = action % 64
    column = square % 8
    row = (square - column) // 8
    piece_id = (action - square) // 64 + 1
    return {
        'piece_id': piece_id * player,
        'new_pos': np.array([int(row), int(column)]),
    }

def player_move(action, player):
        move = action_to_move(action, player)

        # Save move attributes for easier use
        piece_id = move['piece_id']
        pos = get_piece_position(piece_id)
        new_pos = move['new_pos']

        # Check if there is an enemy piece in the new position
        if check_piece_in(board, new_pos[0], new_pos[1]):
            kill(board[new_pos[0], new_pos[1]]) 

        # Move the piece to the new square
        board[new_pos[0], new_pos[1]] = board[pos[0], pos[1]]
        board[pos[0], pos[1]] = '0'

        if check_piece_in_corner(new_pos[0], new_pos[1]):
            evolve[piece_id]

        pivot(piece_id)

move = {'piece_id': 1,
        'new_pos': (4, 2)
        }

action = move_to_action(move)

print(board)
player_move(action, 1)
print(board)

#print(generate_valid_moves_b(board))
#print(board)
#print("\n")
#list_o_moves_b = generate_valid_moves_b(board)
#print(list_o_moves_b)
#list_o_moves_r = generate_valid_moves_r(board)
#print(list_o_moves_r)

