from collections import defaultdict
import pygame
from player import Player
from mouse import Mouse
from gamestate import GameState
import movement


class Game:

    def __init__(self, screen_width, mode):
        # Variable Initiation
        self.screen_size = int(screen_width / 2)
        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))  # Where the game is shown
        self.gamestate = GameState(mode, self.screen_size / 8)

        self.mouse = Mouse(self.gamestate)
        self.run = True

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
                    pygame.draw.rect(self.screen, (255, 255, 255),
                                     (x, y, self.gamestate.square_side, self.gamestate.square_side))

                x += self.gamestate.square_side

                if x > self.screen_size - self.gamestate.square_side:
                    y += self.gamestate.square_side

                    x = 0

    def display_turn(self):
        print("Turn ", self.gamestate.turn, ":", sep='')

    def draw_pieces(self):
        for i in self.gamestate.players:
            i.draw_pieces(self.screen)

    def change_turn(self):
        if self.gamestate.player_turn == 2 and len(self.gamestate.players[0].pieces):
            self.gamestate.player_turn = 1
        elif self.gamestate.player_turn == 1 and len(self.gamestate.players[1].pieces):
            self.gamestate.player_turn = 2

        self.mouse.clickedPiece = False
        self.gamestate.turn += 1
