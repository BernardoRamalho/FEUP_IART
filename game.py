from collections import defaultdict

import pygame
from player import Player
from mouse import Mouse
import movement


class Game:

    def __init__(self, screen_width):
        # Variable Initiation
        self.screen_size = int(screen_width / 2)
        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))  # Where the game is shown
        self.square_side = self.screen_size / 8  # 8 because the board is 8x8
        player1 = Player(1, self.square_side)
        player2 = Player(2, self.square_side)

        self.mouse = Mouse(self)
        self.player_turn = 1  # 1 if it's player 1 turn, 2 otherwise

        self.run = True

        self.players = [player1, player2]

        self.mode = 0

    def draw(self):
        self.draw_board()
        self.draw_pieces()

    def draw_board(self):
        x = 0
        y = 0

        self.screen.fill((0, 0, 0))

        for i in range(8):
            for j in range(8):

                if (i + j) % 2 != 0:
                    pygame.draw.rect(self.screen, (255, 255, 255), (x, y, self.square_side, self.square_side))

                x += self.square_side

                if x > self.screen_size - self.square_side:
                    y += self.square_side

                    x = 0

    def draw_pieces(self):
        for i in self.players:
            i.draw_pieces(self.screen)

    def check_end_game(self):

        for i in self.players:
            for p in i.pieces.values():

                if not p.evolved:
                    return

        self.run = False

    def move_piece(self, piece, new_position, player_nr):  # change_piece_position
        del self.players[player_nr - 1].pieces[piece.get_position()]
        piece.set_position(new_position)
        piece.invert_direction()
        piece.selected = False

        if self.mouse.check_edge_square(self.square_side):
            piece.evolve()
            if self.mode == 1 or self.mode == 2: print("Player ", player_nr, "evolved a piece.")

        self.players[player_nr - 1].pieces[new_position] = piece

        opponent = 0
        if player_nr == 1:
            opponent = 1
        if new_position in self.players[opponent].pieces:
            del self.players[opponent].pieces[new_position]
            if self.mode == 1 or self.mode == 2:
                print("Player ", player_nr, "ate a piece from the opponent")

        if self.mode == 1 or self.mode == 2:
            print("Player ", player_nr, "moved piece to ", piece.position)

    def generate_valid_moves(self, player_nr):
        opponent = 1

        if player_nr == 1:
            opponent = 2

        possible_positions = defaultdict(list)
        for i in self.players[player_nr - 1].pieces.values():

            if i.direction == 'v': # Generate all the possible y positions
                movement.generate_all_y_movements(self.players[player_nr - 1], self.players[opponent - 1], i,
                                                  self.square_side, possible_positions)

            else: # Generate all the possible x positions
                movement.generate_all_x_movements(self.players[player_nr - 1], self.players[opponent - 1], i,
                                                  self.square_side, possible_positions)
