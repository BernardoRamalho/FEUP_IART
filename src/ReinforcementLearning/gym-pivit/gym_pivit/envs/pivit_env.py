import gym
from gym import error, spaces, utils
from gym.utils import seeding

# Piece names:
# Player color letter [r,R or b, B], Capped if evolved + Alignment -> Evolved Red Piece Horizontally Alligned = RH

pieces_to_ids = {
    # Red Uninvolved Pieces
    'rH1': 1, 'rH2': 2, 'rH3': 3, 'rH4': 4,
    'rV1': 5, 'rV2': 6, 'rV3': 7, 'rV4': 8,
    'rH5': 9, 'rH6': 10, 'rH7': 11, 'rH8': 12,
    # Red Evolved Pieces
    'RH1': 1, 'RH2': 2, 'RH3': 3, 'RH4': 4,
    'RV1': 5, 'RV2': 6, 'RV3': 7, 'RV4': 8,
    'RH5': 9, 'RH6': 10, 'RH7': 11, 'RH8': 12,
    # Blue Uninvolved Pieces
    'bV1': 1, 'bV2': 2, 'bV3': 3, 'bV4': 4,
    'bH1': 5, 'bH2': 6, 'bH3': 7, 'bH4': 8,
    'bV5': 9, 'bV6': 10, 'bV7': 11, 'bV8': 12,
    # Blue Evolved Pieces
    'BV1': 1, 'BV2': 2, 'BV3': 3, 'BV4': 4,
    'BH1': 5, 'BH2': 6, 'BH3': 7, 'BH4': 8,
    'BV5': 9, 'BV6': 10, 'BV7': 11, 'BV8': 12,
}

RED = 0
BLUE = 1


class PivitEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    ids_to_pieces = {v: k for k, v in pieces_to_ids.items()}

    def __init__(self):

        self.observation_space = spaces.Box(-12, 12, (8, 8))  # board 8x8
        self.action_space = spaces.Discrete(64 * 12)
        return

    def step(self, action):
        return

    def reset(self):
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
        if inPos == 'rh' or inPos == 'RH' or inPos == 'rv' or inPos == 'RV':
            return False
        return True

    @staticmethod
    def check_valid_square_blue(board, lin, col):
        inPos = board[lin][col]
        if inPos == 'bh' or inPos == 'BH' or inPos == 'bv' or inPos == 'BV':
            return False
        return True

    @staticmethod
    def check_piece_in(board, lin, col):
        return not board[lin][col] == ' '

    @staticmethod
    def check_piece_in_corner(lin, col):
        return (lin == 0 and col == 0) or (lin == 0 and col == 7) or (lin == 7 and col == 7) or (lin == 7 and col == 0)

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
            if self.check_piece_id_in(board, lin, deltaCol):
                break
            i += 1
            deltaCol += 1

        deltaCol = col - 1
        i = 0
        while deltaCol >= 0:
            if (i % 2 == 0 or self.ids_to_pieces[piece_id] == 'RH') and self.check_valid_square_red(board, lin, deltaCol):
                valid_moves.append(((lin, col), (lin, deltaCol)))
            if self.check_piece_id_in(board, lin, deltaCol):
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
            if self.check_piece_id_in(board, deltaLin, col):
                break
            i += 1
            deltaLin += 1

        deltaLin = lin - 1
        i = 0
        while deltaLin >= 0:
            if (i % 2 == 0 or self.ids_to_pieces[piece_id] == 'RV') and self.check_valid_square_red(board, deltaLin, col):
                valid_moves.append(((lin, col), (deltaLin, col)))
            if self.check_piece_id_in(board, deltaLin, col):
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
            if self.check_piece_id_in(board, lin, deltaCol):
                break
            i += 1
            deltaCol += 1

        deltaCol = col - 1
        i = 0
        while deltaCol >= 0:
            if (i % 2 == 0 or self.ids_to_pieces[piece_id] == 'BH') and self.check_valid_square_blue(board, lin, deltaCol):
                valid_moves.append(((lin, col), (lin, deltaCol)))
            if self.check_piece_id_in(board, lin, deltaCol):
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
            if self.check_piece_id_in(board, deltaLin, col):
                break
            i += 1
            deltaLin += 1

        deltaLin = lin - 1
        i = 0
        while deltaLin >= 0:
            if (i % 2 == 0 or self.ids_to_pieces[piece_id] == 'BV') and self.check_valid_square_blue(board, deltaLin, col):
                valid_moves.append(((lin, col), (deltaLin, col)))
            if self.check_piece_id_in(board, deltaLin, col):
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
