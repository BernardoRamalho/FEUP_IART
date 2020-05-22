import gym
from gym import error, spaces, utils
from gym.utils import seeding

import numpy as np

# Piece names:
# Player color letter [r,R or b, B], Capped if evolved + Alignment -> Evolved Red Piece Horizontally Alligned = RH

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

RED = 0
BLUE = 1


class PivitEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    ids_to_pieces = {v: k for k, v in pieces_to_ids.items()}

    def setup(self):
        self.blueMap = ['none', 'v', 'v', 'v', 'v', 'h', 'h', 'h', 'h', 'v', 'v', 'v', 'v'] #CAPS if Evolved
        self.redMap = ['none', 'v', 'v', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'v', 'v'] #CAPS if Evolved
        self.board = [[0, -1, 1, -2, -3, 2, -4, 0],
                     [3, 0, 0, 0, 0, 0, 0, 4],
                     [-5, 0, 0, 0, 0, 0, 0, -6], 
                     [5, 0, 0, 0, 0, 0, 0, 0, 6], 
                     [7, 0, 0, 0, 0, 0, 0, 0, 8], 
                     [-7, 0, 0, 0, 0, 0, 0, 0, -8],  
                     [9, 0, 0, 0, 0, 0, 0, 0, 10], 
                     [0, -9, 11, -10, -11, 12, -12, 0]]

    def __init__(self):
        self.observation_space = spaces.Box(-12, 12, (8, 8))  # board 8x8
        self.action_space = spaces.Discrete(64 * 12)
        return

    def step(self, action):
        return

    def reset(self):
        self.setup()
        return

    def render(self, mode='human'):
        return

    def close(self):
        return

    ##################
    # Logic Function #
    ##################

    @staticmethod
    def check_valid_square_red(board, lin, col):
        inPos = board[lin][col]
        if inPos > 0: return False
        return True

    @staticmethod
    def check_valid_square_blue(board, lin, col):
        inPos = board[lin][col]
        if inPos < 0: return False
        return True

    @staticmethod
    def check_piece_in(board, lin, col):
        return not board[lin][col] == 0

    @staticmethod
    def check_piece_in_corner(lin, col):
        return (lin == 0 and col == 0) or (lin == 0 and col == 7) or (lin == 7 and col == 7) or (lin == 7 and col == 0)

    @staticmethod
    def move_to_action(move):
        piece_id = move['piece_id']
        new_pos = move['new_pos']
        return 64*(abs(piece_id) - 1) + (new_pos[0] * 8 + new_pos[1]).item()

    @staticmethod
    def action_to_move(action, player):
        square = action % 64
        column = square % 8
        row = (square - column) // 8
        piece_id = (action - square) // 64 + 1
        return {
            'piece_id': piece_id * player,
            'new_pos': np.array([int(row), int(column)]),
        }

    def check_piece_evolved(self, id):
        if id > 0 and (self.redMap[id] == 'H' or self.redMap[id] == 'V'): 
            return True
        elif id < 0 and (self.blueMap[id*(-1)] == 'H' or self.blueMap[id*(-1)] == 'V'): 
            return True
        return False
    
    def get_piece_orientation(self, id):
        if id > 0: return self.redMap[id]
        return self.blueMap[id*(-1)]

    #####################
    # Movement Function #
    #####################
    def generate_valid_moves_rh(self, board, lin, col):
        valid_moves = []
        total_moves = []
        i = 0
        piece_id = board[lin][col]
        deltaCol = col + 1
        while deltaCol < 8:
            if (i % 2 == 0 or self.ids_to_pieces[piece_id] == 'RH') and self.check_valid_square_red(board, lin, deltaCol):
                valid_moves.append(((lin, col), (lin, deltaCol)))
            if self.check_piece_in(board, lin, deltaCol):
                break
            i += 1
            deltaCol += 1

        deltaCol = col - 1
        i = 0
        while deltaCol >= 0:
            if (i % 2 == 0 or self.ids_to_pieces[piece_id] == 'RH') and self.check_valid_square_red(board, lin, deltaCol):
                valid_moves.append(((lin, col), (lin, deltaCol)))
            if self.check_piece_in(board, lin, deltaCol):
                break
            i += 1
            deltaCol -= 1

        for m in valid_moves:
            total_moves.append({
                'piece': piece_id,
                'pos': m[0],
                'new_pos': m[1],
                'type': 'move'
            })

        return total_moves

    def generate_valid_moves_rv(self, board, lin, col):
        valid_moves = []
        total_moves = []
        i = 0
        piece_id = board[lin][col]
        deltaLin = lin + 1
        while deltaLin < 8:
            if (i % 2 == 0 or self.ids_to_pieces[piece_id] == 'RV') and self.check_valid_square_red(board, deltaLin, col):
                valid_moves.append(((lin, col), (deltaLin, col)))
            if self.check_piece_in(board, deltaLin, col):
                break
            i += 1
            deltaLin += 1

        deltaLin = lin - 1
        i = 0
        while deltaLin >= 0:
            if (i % 2 == 0 or self.ids_to_pieces[piece_id] == 'RV') and self.check_valid_square_red(board, deltaLin, col):
                valid_moves.append(((lin, col), (deltaLin, col)))
            if self.check_piece_in(board, deltaLin, col):
                break
            i += 1
            deltaLin -= 1

        for m in valid_moves:
            total_moves.append({
                'piece': piece_id,
                'pos': m[0],
                'new_pos': m[1],
                'type': 'move'
            })

        return total_moves

    def generate_valid_moves_bh(self, board, lin, col):
        valid_moves = []
        total_moves = []
        i = 0
        deltaCol = col + 1
        piece_id = board[lin][col]
        while deltaCol < 8:
            if (i % 2 == 0 or self.ids_to_pieces[piece_id] == 'BH') and self.check_valid_square_blue(board, lin, deltaCol):
                valid_moves.append(((lin, col), (lin, deltaCol)))
            if self.check_piece_in(board, lin, deltaCol):
                break
            i += 1
            deltaCol += 1

        deltaCol = col - 1
        i = 0
        while deltaCol >= 0:
            if (i % 2 == 0 or self.ids_to_pieces[piece_id] == 'BH') and self.check_valid_square_blue(board, lin, deltaCol):
                valid_moves.append(((lin, col), (lin, deltaCol)))
            if self.check_piece_in(board, lin, deltaCol):
                break
            i += 1
            deltaCol -= 1

        for m in valid_moves:
            total_moves.append({
                'piece': piece_id,
                'pos': m[0],
                'new_pos': m[1],
                'type': 'move'
            })

        return total_moves

    def generate_valid_moves_bv(self, board, lin, col):
        valid_moves = []
        total_moves = []
        i = 0
        deltaLin = lin + 1
        piece_id = board[lin][col]
        while deltaLin < 8:
            if (i % 2 == 0 or self.ids_to_pieces[piece_id] == 'BV') and self.check_valid_square_blue(board, deltaLin, col):
                valid_moves.append(((lin, col), (deltaLin, col)))
            if self.check_piece_in(board, deltaLin, col):
                break
            i += 1
            deltaLin += 1

        deltaLin = lin - 1
        i = 0
        while deltaLin >= 0:
            if (i % 2 == 0 or self.ids_to_pieces[piece_id] == 'BV') and self.check_valid_square_blue(board, deltaLin, col):
                valid_moves.append(((lin, col), (deltaLin, col)))
            if self.check_piece_in(board, deltaLin, col):
                break
            i += 1
            deltaLin -= 1

        for m in valid_moves:
            total_moves.append({
                'piece': piece_id,
                'pos': m[0],
                'new_pos': m[1],
                'type': 'move'
            })

        return total_moves

