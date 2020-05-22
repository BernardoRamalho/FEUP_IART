import gym
from gym import error, spaces, utils
action_space = spaces.Discrete(64*12)

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

def check_valid_square_red(board, lin, col):
    inPos = board[lin][col]
    if inPos > 0: return False
    return True

def check_valid_square_blue(board, lin, col):
    inPos = board[lin][col]
    if inPos < 0: return False
    return True

def check_piece_in(board, lin, col):
    return not board[lin][col] == 0

blueMap = ['none', 'v', 'v', 'v', 'v', 'h', 'h', 'h', 'h', 'v', 'v', 'v', 'v'] #CAPS if Evolved
redMap = ['none', 'v', 'v', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'v', 'v'] #CAPS if Evolved
board = [[0, -1, 1, -2, -3, 2, -4, 0],
             [3, 0, 0, 0, 0, 0, 0, 4],
             [-5, 0, 0, 0, 0, 0, 0, -6], 
             [5, 0, 0, 0, 0, 0, 0, 0, 6], 
             [7, 0, 0, 0, 0, 0, 0, 0, 8], 
             [-7, 0, 0, 0, 0, 0, 0, 0, -8],  
             [9, 0, 0, 0, 0, 0, 0, 0, 10], 
             [0, -9, 11, -10, -11, 12, -12, 0]]

           
print(action_space.sample())