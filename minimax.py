import sys
from piece import Piece
from gamestate import GameState
from collections import defaultdict

class Minimax:
	
	#Player 1 -> Max, Player 2 -> Min
	def __init__(self, mode, square_side):
		self.gamestate = GameState(mode, square_side)

	def max_win(self):
		if self.gamestate.check_end_game() and len(self.gamestate.players[0].pieces) > len(self.gamestate.players[1].pieces): return True#sys.maxsize
		elif len(self.gamestate.players[0].pieces) > 0 and len(self.gamestate.players[1].pieces) <= 0: return True
		return False

	def min_win(self):
		if self.gamestate.check_end_game() and len(self.gamestate.players[0].pieces) > len(self.gamestate.players[1].pieces): return True
		elif len(self.gamestate.players[1].pieces) > 0 and len(self.gamestate.players[0].pieces) <= 0: return True
		return False
	
	def vulnerable_pos(self, check_x, check_y, oponent, gamestate):
		#abs(self.position[1] - y) % (2 * square_side) == 0 nova pos - pos antiga % 
		
		#Vertical check
		var_x = gamestate.square_side
		pos_checked = 1
		while check_x - var_x > 0:
			if pos_checked % 2 == 0:
				if [check_x - var_x, check_y] in gamestate.players[oponent].pieces:
					if gamestate.players[oponent].pieces[[check_x - var_x, check_y]].evolved and gamestate.players[oponent].pieces[[check_x - var_x, check_y]].direction == "h":
						return True
			else:
				if [check_x - var_x, check_y] in gamestate.players[oponent].pieces:
					if gamestate.players[oponent].pieces[[check_x - var_x, check_y]].direction == "h":
						return True
			pos_checked += 1
			var_x += gamestate.square_side
		
		var_x = gamestate.square_side
		pos_checked = 1
		while check_x + var_x > gamestate.square_side * 8:
			if pos_checked % 2 == 0:
				if [check_x + var_x, check_y] in gamestate.players[oponent].pieces:
					if gamestate.players[oponent].pieces[[check_x + var_x, check_y]].evolved and gamestate.players[oponent].pieces[[check_x + var_x, check_y]].direction == "h":
						return True
			else:
				if [check_x + var_x, check_y] in gamestate.players[oponent].pieces:
					if gamestate.players[oponent].pieces[[check_x + var_x, check_y]].direction == "h":
						return True
			pos_checked += 1
			var_x += gamestate.square_side




test = Minimax(1, 120)
#Test Constructor
print("Testing Constructor\n")
print("P1: ", test.gamestate.players[0].pieces, "\n\n")
print("P2: ", test.gamestate.players[1].pieces, "\n\n")

#Test max_win
print("Testing max_win\n")
piece = Piece(180, 60, "h", 50)
piece.evolve()
test.gamestate.players[0].pieces = defaultdict(Piece)
test.gamestate.players[0].pieces[piece.get_position()] = piece
test.gamestate.players[1].pieces = defaultdict(Piece)
print("P1: ", test.gamestate.players[0].pieces)
print("P2: ", test.gamestate.players[1].pieces)
print("max_win: ", test.max_win(), "\n")

#Test min_win
print("Testing min_win\n")
piece = Piece(180, 60, "h", 50)
piece.evolve()
test.gamestate.players[0].pieces = defaultdict(Piece)
test.gamestate.players[1].pieces = defaultdict(Piece)
test.gamestate.players[1].pieces[piece.get_position()] = piece
print("P1: ", test.gamestate.players[0].pieces)
print("P2: ", test.gamestate.players[1].pieces)
print("min_win: ", test.min_win(), "\n")


