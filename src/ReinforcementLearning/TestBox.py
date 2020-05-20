# [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
class TestBox():

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

    def generate_valid_moves_BV(self, board, lin, col):
        valid_moves = []
        i = 0
        deltaLin = lin + 1
        while deltaLin < 8:
            if i % 2 == 0 and self.check_valid_square_blue(board, deltaLin, col):
    	        valid_moves.append(((lin, col), (deltaLin, col)))
            if self.check_piece_in(board, deltaLin, col):
                break
            i += 1
            deltaLin += 1

        deltaLin = lin - 1
        i = 0
        while deltaLin >= 0:
            if i % 2 == 0 and self.check_valid_square_blue(board, deltaLin, col):
                valid_moves.append(((lin, col), (deltaLin, col)))
            if self.check_piece_in(board, deltaLin, col):
                break
            i += 1
            deltaLin -= 1
        return valid_moves

board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', 'rh', ' ', 'BH', 'rh '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

test = TestBox()
print(test.generate_valid_moves_BV(board, 3, 0))
