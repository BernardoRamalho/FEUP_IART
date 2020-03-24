import pygame
from player import Player
from mouse import Mouse


class Game:

    def __init__(self, screen_width):
        # Variable Initiation
        self.screen_size = int(screen_width / 2)
        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))  # Where the game is shown
        self.square_side = self.screen_size / 8  # 8 because the board is 8x8
        player1 = Player(1, self.square_side)
        player2 = Player(2, self.square_side)

        self.mouse = Mouse()
        self.player_turn = 1  # 1 if it's player 1 turn, 2 otherwise

        self.run = True

        self.players = [player1, player2]

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
            for p in i.pieces:

                if not p.evolved:
                    return

        self.run = False
