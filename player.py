import pygame
from piece import Piece
from collections import defaultdict


class Player:

    def __init__(self, player_nr, square_side_size):
        self.pieces = defaultdict(Piece)
        self.player_nr = player_nr
        self.create_pieces(square_side_size)

    def create_pieces(self, square_side_size):
        radius = square_side_size * 0.9 / 2

        if self.player_nr == 2:

            for i in range(1, 7):
                if i == 2 or i == 5:
                    piece = Piece(i * square_side_size + square_side_size / 2, square_side_size / 2, 'v', radius)
                    self.pieces[piece.get_position()] = piece

                    piece = Piece(i * square_side_size + square_side_size / 2,
                                  7 * square_side_size + square_side_size / 2,
                                  'v', radius)
                    self.pieces[piece.get_position()] = piece

                else:
                    piece = Piece(square_side_size / 2, i * square_side_size + square_side_size / 2, 'h', radius)
                    self.pieces[piece.get_position()] = piece

                    piece = Piece(7 * square_side_size + square_side_size / 2,
                                  i * square_side_size + square_side_size / 2,
                                  'h', radius)
                    self.pieces[piece.get_position()] = piece
        else:

            for i in range(1, 7):
                if i == 2 or i == 5:
                    piece = Piece(square_side_size / 2, i * square_side_size + square_side_size / 2, 'h', radius)
                    self.pieces[piece.get_position()] = piece

                    piece = Piece(7 * square_side_size + square_side_size / 2,
                                  i * square_side_size + square_side_size / 2,
                                  'h', radius)
                    self.pieces[piece.get_position()] = piece

                else:
                    piece = Piece(i * square_side_size + square_side_size / 2, square_side_size / 2, 'v', radius)
                    self.pieces[piece.get_position()] = piece

                    piece = Piece(i * square_side_size + square_side_size / 2,
                                  7 * square_side_size + square_side_size / 2,
                                  'v', radius)
                    self.pieces[piece.get_position()] = piece

    def draw_pieces(self, screen):

        for i in self.pieces.values():
            i.draw(screen, self.player_nr)

    def change_piece_position(self, piece, new_position):
        del self.pieces[piece.get_position()]
        piece.set_position(new_position)
        piece.invert_direction()
        self.pieces[new_position] = piece
        print("Player ", self.player_nr, "moved piece to ", piece.position)

