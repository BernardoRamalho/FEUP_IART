from player import Player

class GameState:
	def __init__(self, mode, square_side):
		self.square_side = square_side
		player1 = Player(1, self.square_side)
		player2 = Player(2, self.square_side)
		self.player_turn = 1
		self.players = [player1, player2]
		self.mode = mode
		self.min_pos = square_side/2
		self.max_pos = square_side * 8 - square_side/2

	def check_end_game(self):

		for i in self.players:
			for p in i.pieces.values():
				if not p.evolved: return False
		return True
	
	def check_edge_square(self, position, square_side):
		if position[0] == square_side / 2 or position[0] == square_side * 8 - square_side / 2:
			if position[1] == square_side / 2 or position[1] == square_side * 8 - square_side / 2:
				return True
	
	def move_piece(self, piece, new_position, player_nr):
		del self.players[player_nr - 1].pieces[piece.get_position()]
		piece.set_position(new_position)
		piece.invert_direction()
		piece.selected = False

		if self.check_edge_square(new_position, self.square_side):
			piece.evolve()
			if self.mode == 1 or self.mode == 2: print("Player ", player_nr, "evolved a piece.")
		
		self.players[player_nr - 1].pieces[new_position] = piece

		oponent = 0
		if player_nr == 1: oponent = 1
		if new_position in self.players[oponent].pieces:
			del self.players[oponent].pieces[new_position]
			if self.mode == 1 or self.mode == 2: print("Player ", player_nr, "ate a piece from the opponent")

		if self.mode == 1 or self.mode == 2: print("Player ", player_nr, "moved piece to ", piece.position)

