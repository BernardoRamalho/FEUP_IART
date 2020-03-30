from player import Player
import movement
from collections import defaultdict


class GameState:
    def __init__(self, mode, square_side):
        self.square_side = square_side
        player1 = Player(1, self.square_side)
        player2 = Player(2, self.square_side)
        self.player_turn = 1
        self.players = [player1, player2]
        self.mode = mode
        self.min_pos = square_side / 2
        self.max_pos = square_side * 8 - square_side / 2
        self.turn = 1

    def check_end_game(self):

        for i in self.players:
            for p in i.pieces.values():
                if not p.evolved:
                    return False
        return True

    def get_who_wins(self):
        if len(self.players[0].pieces) > len(self.players[1].pieces):  # Player 1 Wins
            return 1
        elif len(self.players[0].pieces) < len(self.players[1].pieces):  # Player 2 Wins
            return 2
        else:  # Drawn
            return 3

    def check_edge_square(self, position, square_side):
        if position[0] == square_side / 2 or position[0] == square_side * 8 - square_side / 2:
            if position[1] == square_side / 2 or position[1] == square_side * 8 - square_side / 2:
                return True

    def move_piece(self, piece, new_position):
        del self.players[self.player_turn - 1].pieces[piece.get_position()]
        piece.set_position(new_position)
        piece.invert_direction()
        piece.selected = False

        if self.check_edge_square(new_position, self.square_side):
            piece.evolve()
            # print("Player ", self.player_turn, "evolved a piece.")

        self.players[self.player_turn - 1].pieces[new_position] = piece

        opponent = self.player_turn % 2

        if new_position in self.players[opponent].pieces:
            del self.players[opponent].pieces[new_position]
            # print("Player ", self.player_turn, "ate a piece from the opponent")

        # print("Player ", self.player_turn, "moved piece to ", piece.position)

    def generate_valid_moves(self, player):
        opponent = player % 2

        possible_positions = defaultdict(list)
        for i in self.players[player - 1].pieces.values():

            if i.direction == 'v':  # Generate all the possible y positions
                movement.generate_all_y_movements(self.players[player - 1], self.players[opponent], i,
                                                  self.square_side, possible_positions)

            else:  # Generate all the possible x positions
                movement.generate_all_x_movements(self.players[player - 1], self.players[opponent], i,
                                                  self.square_side, possible_positions)
        return possible_positions

    def print_info(self):
        print(self.players[self.player_turn - 1].pieces.keys())

    def change_turn(self):
        if self.player_turn == 2 and len(self.players[0].pieces):
            self.player_turn = 1
        elif self.player_turn == 1 and len(self.players[1].pieces):
            self.player_turn = 2

        self.turn += 1


    def display_turn(self):
        print("\nTurn ", self.turn, ":", sep='')
