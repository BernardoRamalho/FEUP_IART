import sys
import math
from piece import Piece
from gamestate import GameState
from collections import defaultdict

class Minimax:
	
	#Player 1 -> Max, Player 2 -> Min
	def __init__(self, mode, square_side):
		self.gamestate = GameState(mode, square_side)

	def test_max_win(self):
		print("Testing max_win\n")
		piece = Piece(180, 60, "h", 50)
		piece.evolve()
		self.gamestate.players[0].pieces = defaultdict(Piece)
		self.gamestate.players[0].pieces[piece.get_position()] = piece
		self.gamestate.players[1].pieces = defaultdict(Piece)
		print("P1: ", self.gamestate.players[0].pieces)
		print("P2: ", self.gamestate.players[1].pieces)
		print("max_win: ", self.max_win(), "\n")

	def max_win(self):
		if self.gamestate.check_end_game() and len(self.gamestate.players[0].pieces) > len(self.gamestate.players[1].pieces): return True#sys.maxsize
		elif len(self.gamestate.players[0].pieces) > 0 and len(self.gamestate.players[1].pieces) <= 0: return True
		return False

	def test_min_win(self):
		print("Testing min_win\n")
		piece = Piece(180, 60, "h", 50)
		piece.evolve()
		self.gamestate.players[0].pieces = defaultdict(Piece)
		self.gamestate.players[1].pieces = defaultdict(Piece)
		self.gamestate.players[1].pieces[piece.get_position()] = piece
		print("P1: ", self.gamestate.players[0].pieces)
		print("P2: ", self.gamestate.players[1].pieces)
		print("min_win: ", self.min_win(), "\n")


	def min_win(self):
		if self.gamestate.check_end_game() and len(self.gamestate.players[0].pieces) > len(self.gamestate.players[1].pieces): return True
		elif len(self.gamestate.players[1].pieces) > 0 and len(self.gamestate.players[0].pieces) <= 0: return True
		return False
	
	def test_vul_pos_left(self):
		print("Testing vulnerable pos left")
		piece1 = Piece(300, 60, "h", 50)
		piece2 = Piece(180, 60, "h", 50)
		piece25 = Piece(180, 60, "v", 50)
		piece3 = Piece(420, 60, "h", 50)

		#self.gamestate.players[1].pieces[piece3.get_position()] = piece3
		#Test 1st Return
		print("Test 1st Return")
		self.gamestate.players[0].pieces = defaultdict(Piece)
		self.gamestate.players[1].pieces = defaultdict(Piece)

		self.gamestate.players[0].pieces[piece1.get_position()] = piece1 #Not Vulnerable
		self.gamestate.players[0].pieces[piece2.get_position()] = piece2

		print("P1: ", self.gamestate.players[0].pieces)
		print("P2: ", self.gamestate.players[1].pieces)
		print(self.vuln_pos_left(300, 60, 0, 1))

		#Test 2nd Return
		print("Test 2nd Return")
		self.gamestate.players[0].pieces = defaultdict(Piece)
		self.gamestate.players[1].pieces = defaultdict(Piece)

		self.gamestate.players[0].pieces[piece3.get_position()] = piece3 #vulnerable
		piece2.evolve()
		self.gamestate.players[1].pieces[piece2.get_position()] = piece2

		print("P1: ", self.gamestate.players[0].pieces)
		print("P2: ", self.gamestate.players[1].pieces)
		print(self.vuln_pos_left(300, 60, 0, 1))

		#Test 3rd Return
		print("Test 3rd Return")
		self.gamestate.players[0].pieces = defaultdict(Piece)
		self.gamestate.players[1].pieces = defaultdict(Piece)

		self.gamestate.players[0].pieces[piece1.get_position()] = piece1 #vulnerable
		self.gamestate.players[1].pieces[piece2.get_position()] = piece2

		print("P1: ", self.gamestate.players[0].pieces)
		print("P2: ", self.gamestate.players[1].pieces)
		print(self.vuln_pos_left(300, 60, 0, 1))

		#Test 4th Return
		print("Test 4th Return")
		self.gamestate.players[0].pieces = defaultdict(Piece)
		self.gamestate.players[1].pieces = defaultdict(Piece)

		self.gamestate.players[0].pieces[piece1.get_position()] = piece1 #Not vulnerable
		self.gamestate.players[1].pieces[piece25.get_position()] = piece25

		print("P1: ", self.gamestate.players[0].pieces)
		print("P2: ", self.gamestate.players[1].pieces)
		print(self.vuln_pos_left(300, 60, 0, 1))



		#Test Last Return
		print("Test 5th Return")
		self.gamestate.players[0].pieces = defaultdict(Piece)
		self.gamestate.players[1].pieces = defaultdict(Piece)

		self.gamestate.players[0].pieces[piece1.get_position()] = piece1 #Not vulnerable
		#self.gamestate.players[1].pieces[piece2.get_position()] = piece2

		print("P1: ", self.gamestate.players[0].pieces)
		print("P2: ", self.gamestate.players[1].pieces)
		print(self.vuln_pos_left(300, 60, 0, 1))

	def vuln_pos_left(self, check_x, check_y, player, oponent):
		pos_counter = 1	
		check_x -= self.gamestate.square_side	
		while check_x > self.gamestate.min_pos:
			if (check_x, check_y) in self.gamestate.players[player].pieces.keys(): return False #It's being protected by another friendly piece

			if (check_x, check_y) in self.gamestate.players[oponent].pieces.keys():
				if pos_counter % 2 == 0 and self.gamestate.players[oponent].pieces[(check_x, check_y)].evolved and self.gamestate.players[oponent].pieces[(check_x, check_y)].direction == "h" : return True
				elif pos_counter % 2 != 0 and self.gamestate.players[oponent].pieces[(check_x, check_y)].direction == "h" : return True
				else: return False #It's being protected by an enemy piece who cant't reach it and blocks others in that line

			check_x -= self.gamestate.square_side
			pos_counter += 1

		return False

	def test_vul_pos_right(self):
		print("Testing vulnerable pos right")
		piece1 = Piece(300, 60, "h", 50)
		piece2 = Piece(180, 60, "h", 50)
		piece25 = Piece(420, 60, "v", 50)
		piece3 = Piece(420, 60, "h", 50)

		#self.gamestate.players[1].pieces[piece3.get_position()] = piece3
		#Test 1st Return
		print("Test 1st Return")
		self.gamestate.players[0].pieces = defaultdict(Piece)
		self.gamestate.players[1].pieces = defaultdict(Piece)

		self.gamestate.players[0].pieces[piece1.get_position()] = piece1 
		self.gamestate.players[0].pieces[piece2.get_position()] = piece2 #Not Vulnerable

		print("P1: ", self.gamestate.players[0].pieces)
		print("P2: ", self.gamestate.players[1].pieces)
		print(self.vuln_pos_right(180, 60, 0, 1))

		#Test 2nd Return
		print("Test 2nd Return")
		self.gamestate.players[0].pieces = defaultdict(Piece)
		self.gamestate.players[1].pieces = defaultdict(Piece)

		self.gamestate.players[0].pieces[piece2.get_position()] = piece2 #vulnerable
		piece3.evolve()
		self.gamestate.players[1].pieces[piece3.get_position()] = piece3

		print("P1: ", self.gamestate.players[0].pieces)
		print("P2: ", self.gamestate.players[1].pieces)
		print(self.vuln_pos_right(180, 60, 0, 1))

		#Test 3rd Return
		print("Test 3rd Return")
		self.gamestate.players[0].pieces = defaultdict(Piece)
		self.gamestate.players[1].pieces = defaultdict(Piece)

		self.gamestate.players[0].pieces[piece3.get_position()] = piece3 #vulnerable
		self.gamestate.players[1].pieces[piece1.get_position()] = piece1

		print("P1: ", self.gamestate.players[0].pieces)
		print("P2: ", self.gamestate.players[1].pieces)
		print(self.vuln_pos_right(300, 60, 1, 0))

		#Test 4th Return
		print("Test 4th Return")
		self.gamestate.players[0].pieces = defaultdict(Piece)
		self.gamestate.players[1].pieces = defaultdict(Piece)

		self.gamestate.players[0].pieces[piece1.get_position()] = piece1 #Not vulnerable
		self.gamestate.players[1].pieces[piece25.get_position()] = piece25

		print("P1: ", self.gamestate.players[0].pieces)
		print("P2: ", self.gamestate.players[1].pieces)
		print(self.vuln_pos_right(300, 60, 0, 1))

		#Test Last Return
		print("Test 5th Return")
		self.gamestate.players[0].pieces = defaultdict(Piece)
		self.gamestate.players[1].pieces = defaultdict(Piece)

		self.gamestate.players[0].pieces[piece1.get_position()] = piece1 #Not vulnerable
		#self.gamestate.players[1].pieces[piece2.get_position()] = piece2

		print("P1: ", self.gamestate.players[0].pieces)
		print("P2: ", self.gamestate.players[1].pieces)
		print(self.vuln_pos_right(300, 60, 0, 1))
			
	def vuln_pos_right(self, check_x, check_y, player, oponent):
		pos_counter = 1
		check_x += self.gamestate.square_side
		while check_x <= self.gamestate.max_pos:
			if (check_x, check_y) in self.gamestate.players[player].pieces.keys(): return False #It's being protected by another friendly piece

			if (check_x, check_y) in self.gamestate.players[oponent].pieces.keys():
				if pos_counter % 2 == 0 and self.gamestate.players[oponent].pieces[(check_x, check_y)].evolved and self.gamestate.players[oponent].pieces[(check_x, check_y)].direction == "h" : return True
				elif pos_counter % 2 != 0 and self.gamestate.players[oponent].pieces[(check_x, check_y)].direction == "h" : return True
				else: return False #It's being protected by an enemy piece who cant't reach it and blocks others in that line

			check_x += self.gamestate.square_side
			pos_counter += 1
		return False


	def test_vul_pos_top(self):
		print("Testing vulnerable pos top")
		piece1 = Piece(60, 300, "v", 50)
		piece2 = Piece(60, 180, "v", 50)
		piece25 = Piece(60, 180, "h", 50)
		piece3 = Piece(60, 420, "v", 50)

		#self.gamestate.players[1].pieces[piece3.get_position()] = piece3
		#Test 1st Return
		print("Test 1st Return")
		self.gamestate.players[0].pieces = defaultdict(Piece)
		self.gamestate.players[1].pieces = defaultdict(Piece)

		self.gamestate.players[0].pieces[piece1.get_position()] = piece1 #Not Vulnerable
		self.gamestate.players[0].pieces[piece2.get_position()] = piece2

		print("P1: ", self.gamestate.players[0].pieces)
		print("P2: ", self.gamestate.players[1].pieces)
		print(self.vuln_pos_top(60, 300, 0, 1))

		#Test 2nd Return
		print("Test 2nd Return")
		self.gamestate.players[0].pieces = defaultdict(Piece)
		self.gamestate.players[1].pieces = defaultdict(Piece)

		self.gamestate.players[0].pieces[piece2.get_position()] = piece2 
		piece2.evolve()
		self.gamestate.players[1].pieces[piece3.get_position()] = piece3 #vulnerable

		print("P1: ", self.gamestate.players[0].pieces)
		print("P2: ", self.gamestate.players[1].pieces)
		print(self.vuln_pos_top(60, 420, 1, 0))

		#Test 3rd Return
		print("Test 3rd Return")
		self.gamestate.players[0].pieces = defaultdict(Piece)
		self.gamestate.players[1].pieces = defaultdict(Piece)
		piece2.evolved = False
		self.gamestate.players[0].pieces[piece1.get_position()] = piece1 #vulnerable
		self.gamestate.players[1].pieces[piece2.get_position()] = piece2

		print("P1: ", self.gamestate.players[0].pieces)
		print("P2: ", self.gamestate.players[1].pieces)
		print(self.vuln_pos_top(60, 300, 0, 1))

		#Test 4th Return
		print("Test 4th Return")
		self.gamestate.players[0].pieces = defaultdict(Piece)
		self.gamestate.players[1].pieces = defaultdict(Piece)

		self.gamestate.players[0].pieces[piece2.get_position()] = piece25 
		piece25.evolve()
		self.gamestate.players[1].pieces[piece3.get_position()] = piece3 #Not Vulnerable

		print("P1: ", self.gamestate.players[0].pieces)
		print("P2: ", self.gamestate.players[1].pieces)
		print(self.vuln_pos_top(60, 420, 1, 0))

		#Test Last Return
		print("Test 5th Return")
		self.gamestate.players[0].pieces = defaultdict(Piece)
		self.gamestate.players[1].pieces = defaultdict(Piece)

		self.gamestate.players[0].pieces[piece1.get_position()] = piece1 #Not vulnerable
		#self.gamestate.players[1].pieces[piece2.get_position()] = piece2

		print("P1: ", self.gamestate.players[0].pieces)
		print("P2: ", self.gamestate.players[1].pieces)
		print(self.vuln_pos_top(300, 60, 0, 1))

	def vuln_pos_top(self, check_x, check_y, player, oponent):
		pos_counter = 1	
		check_y -= self.gamestate.square_side	
		while check_y >= self.gamestate.min_pos:
			if (check_x, check_y) in self.gamestate.players[player].pieces.keys(): return False #It's being protected by another friendly piece

			if (check_x, check_y) in self.gamestate.players[oponent].pieces.keys():
				if pos_counter % 2 == 0 and self.gamestate.players[oponent].pieces[(check_x, check_y)].evolved and self.gamestate.players[oponent].pieces[(check_x, check_y)].direction == "v" : return True
				elif pos_counter % 2 != 0 and self.gamestate.players[oponent].pieces[(check_x, check_y)].direction == "v" : return True
				else: return False #It's being protected by an enemy piece who cant't reach it and blocks others in that line

			check_y -= self.gamestate.square_side
			pos_counter += 1

		return False


	def test_vul_pos_bot(self):
		print("Testing vulnerable pos bot")
		piece1 = Piece(60, 300, "v", 50)
		piece2 = Piece(60, 180, "v", 50)
		piece25 = Piece(60, 420, "h", 50)
		piece3 = Piece(60, 420, "v", 50)

		#self.gamestate.players[1].pieces[piece3.get_position()] = piece3
		#Test 1st Return
		print("Test 1st Return")
		self.gamestate.players[0].pieces = defaultdict(Piece)
		self.gamestate.players[1].pieces = defaultdict(Piece)

		self.gamestate.players[0].pieces[piece1.get_position()] = piece1 
		self.gamestate.players[0].pieces[piece2.get_position()] = piece2 #Not Vulnerable

		print("P1: ", self.gamestate.players[0].pieces)
		print("P2: ", self.gamestate.players[1].pieces)
		print(self.vuln_pos_bot(60, 180, 0, 1))

		#Test 2nd Return
		print("Test 2nd Return")
		self.gamestate.players[0].pieces = defaultdict(Piece)
		self.gamestate.players[1].pieces = defaultdict(Piece)

		self.gamestate.players[0].pieces[piece2.get_position()] = piece2 #vulnerable
		piece3.evolve()
		self.gamestate.players[1].pieces[piece3.get_position()] = piece3

		print("P1: ", self.gamestate.players[0].pieces)
		print("P2: ", self.gamestate.players[1].pieces)
		print(self.vuln_pos_bot(60, 180, 0, 1))

		#Test 3rd Return
		print("Test 3rd Return")
		self.gamestate.players[0].pieces = defaultdict(Piece)
		self.gamestate.players[1].pieces = defaultdict(Piece)

		self.gamestate.players[0].pieces[piece3.get_position()] = piece3 #vulnerable
		self.gamestate.players[1].pieces[piece1.get_position()] = piece1

		print("P1: ", self.gamestate.players[0].pieces)
		print("P2: ", self.gamestate.players[1].pieces)
		print(self.vuln_pos_bot(60, 300, 1, 0))

		#Test 4th Return
		print("Test 4th Return")
		self.gamestate.players[0].pieces = defaultdict(Piece)
		self.gamestate.players[1].pieces = defaultdict(Piece)

		self.gamestate.players[0].pieces[piece1.get_position()] = piece1 #Not vulnerable
		self.gamestate.players[1].pieces[piece25.get_position()] = piece25

		print("P1: ", self.gamestate.players[0].pieces)
		print("P2: ", self.gamestate.players[1].pieces)
		print(self.vuln_pos_bot(60, 300, 0, 1))

		#Test Last Return
		print("Test 5th Return")
		self.gamestate.players[0].pieces = defaultdict(Piece)
		self.gamestate.players[1].pieces = defaultdict(Piece)

		self.gamestate.players[0].pieces[piece1.get_position()] = piece1 #Not vulnerable
		#self.gamestate.players[1].pieces[piece2.get_position()] = piece2

		print("P1: ", self.gamestate.players[0].pieces)
		print("P2: ", self.gamestate.players[1].pieces)
		print(self.vuln_pos_bot(60, 30, 0, 1))

	def vuln_pos_bot(self, check_x, check_y, player, oponent):
		pos_counter = 1	
		check_y += self.gamestate.square_side	
		while check_y < self.gamestate.max_pos:
			if (check_x, check_y) in self.gamestate.players[player].pieces.keys(): return False #It's being protected by another friendly piece

			if (check_x, check_y) in self.gamestate.players[oponent].pieces.keys():
				if pos_counter % 2 == 0 and self.gamestate.players[oponent].pieces[(check_x, check_y)].evolved and self.gamestate.players[oponent].pieces[(check_x, check_y)].direction == "v" : return True
				elif pos_counter % 2 != 0 and self.gamestate.players[oponent].pieces[(check_x, check_y)].direction == "v" : return True
				else: return False #It's being protected by an enemy piece who cant't reach it and blocks others in that line

			check_y += self.gamestate.square_side
			pos_counter += 1

		return False

	
	def vulnerable_position(self, check_x, check_y, player, oponent):
		return self.vuln_pos_left(check_x, check_y, player, oponent) or self.vuln_pos_right(check_x, check_y, player, oponent) or self.vuln_pos_top(check_x, check_y, player, oponent) or self.vuln_pos_bot(check_x, check_y, player, oponent) 


	def calc_dist_to_nearest_evol(self, check_x, check_y):
		point_0 = (self.gamestate.min_pos, self.gamestate.min_pos)
		point_1 = (self.gamestate.min_pos, self.gamestate.max_pos)
		point_2 = (self.gamestate.max_pos, self.gamestate.min_pos)
		point_3 = (self.gamestate.max_pos, self.gamestate.max_pos)

		d0 = math.floor(math.sqrt(pow(check_x - point_0[0],2) + pow(check_y - point_0[1],2)))
		d1 = math.floor(math.sqrt(pow(check_x - point_1[0],2) + pow(check_y - point_1[1],2)))
		d2 = math.floor(math.sqrt(pow(check_x - point_2[0],2) + pow(check_y - point_2[1],2)))
		d3 = math.floor(math.sqrt(pow(check_x - point_3[0],2) + pow(check_y - point_3[1],2)))

		return min([d0, d1, d2, d3])


	#def value_my_pieces()
	#def value_max_pieces(self, player, oponent):
		#value_counter = 0
		#for piece in self.gamestate.players[player].pieces.values():
			#if(self.vulnerable_position(piece.get_position()[0], piece.get_position()[1], player, oponent)): continue

		#return value_counter
		
test = Minimax(1, 120)
#Test Constructor
#print("Testing Constructor\n")
#print("P1: ", test.gamestate.players[0].pieces, "\n\n")
#print("P2: ", test.gamestate.players[1].pieces, "\n\n")
#Test max_win
#test.test_max_win()

#Test min_win
#test.test_min_win()

#Test vulnerable_pos_left
#test.test_vul_pos_left()

#Test vulnerable_pos_right
#test.test_vul_pos_right()

#Test vulnerable_pos_top
#test.test_vul_pos_top()

#Test vulnerable_pos_bot
#test.test_vul_pos_bot()



#print("Should say true: ",test.vulnerable_pos_left(300, 60, 1, 0, test.gamestate))
