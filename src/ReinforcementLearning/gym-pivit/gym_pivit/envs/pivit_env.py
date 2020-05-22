import gym
from gym import error, spaces, utils
from gym.utils import seeding

# Piece names:
# Player color letter [r,R or b, B], Capped if evolved + Alignment -> Evolved Red Piece Horizontally Alligned = RH

RED = 0
BLUE = 1


class PivitEnv(gym.Env):
    metadata = {'render.modes': ['human']}

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
        piece = board[lin][col]
        deltaCol = col + 1
        while deltaCol < 8:
            if (i % 2 == 0 or piece == 'RH') and self.check_valid_square_red(board, lin, deltaCol):
                valid_moves.append(((lin, col), (lin, deltaCol)))
            if self.check_piece_in(board, lin, deltaCol):
                break
            i += 1
            deltaCol += 1

        deltaCol = col - 1
        i = 0
        while deltaCol >= 0:
            if (i % 2 == 0 or piece == 'RH') and self.check_valid_square_red(board, lin, deltaCol):
                valid_moves.append(((lin, col), (lin, deltaCol)))
            if self.check_piece_in(board, lin, deltaCol):
                break
            i += 1
            deltaCol -= 1

        for m in valid_moves:
            total_moves.append({
                'piece': piece,
                'pos': m[0],
                'new_pos': m[1],
                'type': 'move'
            })

        return total_moves

    def generate_valid_moves_rv(self, board, lin, col):
        valid_moves = []
        total_moves = []
        i = 0
        piece = board[lin][col]
        deltaLin = lin + 1
        while deltaLin < 8:
            if (i % 2 == 0 or piece == 'RV') and self.check_valid_square_red(board, deltaLin, col):
                valid_moves.append(((lin, col), (deltaLin, col)))
            if self.check_piece_in(board, deltaLin, col):
                break
            i += 1
            deltaLin += 1

        deltaLin = lin - 1
        i = 0
        while deltaLin >= 0:
            if (i % 2 == 0 or piece == 'RV') and self.check_valid_square_red(board, deltaLin, col):
                valid_moves.append(((lin, col), (deltaLin, col)))
            if self.check_piece_in(board, deltaLin, col):
                break
            i += 1
            deltaLin -= 1

        for m in valid_moves:
            total_moves.append({
                'piece': piece,
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
        piece = board[lin][col]
        while deltaCol < 8:
            if (i % 2 == 0 or piece == 'BH') and self.check_valid_square_blue(board, lin, deltaCol):
                valid_moves.append(((lin, col), (lin, deltaCol)))
            if self.check_piece_in(board, lin, deltaCol):
                break
            i += 1
            deltaCol += 1

        deltaCol = col - 1
        i = 0
        while deltaCol >= 0:
            if (i % 2 == 0 or piece == 'BH') and self.check_valid_square_blue(board, lin, deltaCol):
                valid_moves.append(((lin, col), (lin, deltaCol)))
            if self.check_piece_in(board, lin, deltaCol):
                break
            i += 1
            deltaCol -= 1

        for m in valid_moves:
            total_moves.append({
                'piece': piece,
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
        piece = board[lin][col]
        while deltaLin < 8:
            if (i % 2 == 0 or piece == 'BV') and self.check_valid_square_blue(board, deltaLin, col):
                valid_moves.append(((lin, col), (deltaLin, col)))
            if self.check_piece_in(board, deltaLin, col):
                break
            i += 1
            deltaLin += 1

        deltaLin = lin - 1
        i = 0
        while deltaLin >= 0:
            if (i % 2 == 0 or piece == 'BV') and self.check_valid_square_blue(board, deltaLin, col):
                valid_moves.append(((lin, col), (deltaLin, col)))
            if self.check_piece_in(board, deltaLin, col):
                break
            i += 1
            deltaLin -= 1

        for m in valid_moves:
            total_moves.append({
                'piece': piece,
                'pos': m[0],
                'new_pos': m[1],
                'type': 'move'
            })

        return total_moves
