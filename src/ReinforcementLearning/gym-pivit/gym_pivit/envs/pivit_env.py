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
        self.action_space = spaces.Discrete(64*12)
        return

    def step(self, action):
        return

    def reset(self):
        return

    def render(self, mode='human'):
        return

    def close(self):
        return

    def check_valid_square_red(self, board, lin, col):
        inpos = board[lin][col]
        if inpos == 'rh' or inpos == 'RH' or inpos == 'rv' or inpos == 'RV':
            return False
        return True

    def check_valid_square_blue(self, board, lin, col):
        inpos = board[lin][col]
        if inpos == 'bh' or inpos == 'BH' or inpos == 'bv' or inpos == 'BV':
            return False
        return True

    def check_piece_in(self, board, lin, col):
        return not board[lin][col] == ' '

    def generate_valid_moves_rh(self, board, lin, col):
        valid_moves = []
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
        return valid_moves
    
    def generate_valid_moves_rv(self, board, lin, col):
        valid_moves = []
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
        return valid_moves

    def generate_valid_moves_bh(self, board, lin, col):
        valid_moves = []
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
        return valid_moves

    def generate_valid_moves_bv(self, board, lin, col):
        valid_moves = []
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
        return valid_moves

