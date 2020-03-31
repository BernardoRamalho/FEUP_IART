import pygame
from mouse import Mouse
from gamestate import GameState
import time
from minimax import Minimax


class Game:

    def __init__(self, screen_width, mode, depth, ai_modes):
        # Variable Initiation
        self.screen_size = int(screen_width / 2)
        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))  # Where the game is shown
        self.gamestate = GameState(mode, self.screen_size / 8, depth, ai_modes)
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

    def draw_pieces(self):
        for i in self.gamestate.players:
            i.draw_pieces(self.screen)

    def forfeit(self):
        print("\nPlayer", self.gamestate.player_turn, "has forfeited the game!")
        print("Congratz to Player", self.gamestate.player_turn % 2 + 1, "for winning the game!")
        self.run = False
