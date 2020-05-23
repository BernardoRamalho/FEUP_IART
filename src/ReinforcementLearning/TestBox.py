
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
board = [[0, -1, 1, -2, -3, 2, -4, 0],
         [3, 0, 0, 0, 0, 0, 0, 4],
         [-5, 0, 0, 2, 0, 0, 0, -6],
         [5, 0, 0, 0, 0, 0, 0, 0, 6],
         [7, 0, 0, 0, 0, 0, 0, 0, 8],
         [-7, 0, 0, 0, 0, 0, 0, 0, -8],
         [9, 0, 0, 0, 0, 0, 0, 0, 10],
         [0, -9, 11, -10, -11, 12, -12, 0]]


def check_valid_square_red(board, lin, col):
    inPos = board[lin][col]
    if inPos > 0:
        return False
    return True


def check_valid_square_blue(board, lin, col):
    inPos = board[lin][col]
    if inPos < 0:
        return False
    return True


def check_piece_in(board, lin, col):
    return not board[lin][col] == 0


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


def generate_valid_moves_rh(board, lin, col):
    # Initialize arrays to store positions and moves
    valid_positions = []
    total_moves = []

    # Get the piece id from the board
    piece_id = board[lin][col]

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
    piece_id = board[lin][col]

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
    piece_id = board[lin][col]

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
    piece_id = board[lin][col]

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


def generate_valid_moves_r(board):
    valid_moves = []
    for position, piece_id in np.ndenumerate(board):
        if piece_id > 0:
            if redMap[piece_id] == 'h' or redMap[piece_id] == 'H':
                valid_moves += generate_valid_moves_rh(
                    board, position[0], position[1])
            elif redMap[piece_id] != 'none':
                valid_moves += generate_valid_moves_rv(
                    board, position[0], position[1])
    return valid_moves


def generate_valid_moves_b(board):
    valid_moves = []
    for position, piece_id in np.ndenumerate(board):
        piece_id = piece_id[0]
        if piece_id < 0:
            piece_id *= -1
            if blueMap[piece_id] == 'h' or blueMap[piece_id] == 'H':
                valid_moves += generate_valid_moves_bh(
                    board, position[0], position[1])
            elif blueMap[piece_id] != 'none':
                valid_moves += generate_valid_moves_bv(
                    board, position[0], position[1])
    return valid_moves

print(board)
list_o_moves_b = generate_valid_moves_b(board)
print(list_o_moves_b)
list_o_moves_r = generate_valid_moves_r(board)
print(list_o_moves_r)

