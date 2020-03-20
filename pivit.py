import pygame
from piece import Piece
from player import Player
from collections import defaultdict


# Basic Information About Structure the Game
# 1º- The Pieces are saved in a dictionary which the key is a tuple containing the position of the piece and the value
# is the key itself;
# 2º- You can exit the Game by pressing the key q;
# 3º- I already made a function to change the position of a key but haven't implemented the event to do so.


#
#
# FUNCTION DEFINITION
#
#

def get_screen_width():
    screen_info = pygame.display.Info()
    return screen_info.current_w


def draw_board(screen, square_side, screen_size):
    x = 0
    y = 0

    screen.fill((0, 0, 0))

    for i in range(8):
        for j in range(8):

            if (i + j) % 2 != 0:
                pygame.draw.rect(screen, (255, 255, 255), (x, y, square_side, square_side))

            x += square_side

            if x > screen_size - square_side:
                y += square_side

                x = 0


def draw_pieces(screen, players):
    for i in players:
        i.draw_pieces(screen)


def event_handler(variables):
    for event in pygame.event.get():

        # Key pressed
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_q:
                variables[0] = False

        # Closed Window
        if event.type == pygame.QUIT:
            variables[0] = False


def main():
    pygame.init()

    # Variable Initiation
    screen_size = int(get_screen_width() / 2)
    screen = pygame.display.set_mode((screen_size, screen_size))  # Where the game is shown
    square_side = screen_size / 8  # 8 because the board is 8x8
    player1 = Player(1, square_side)
    player2 = Player(2, square_side)

    run = True

    players = [player1, player2]

    game_variables = [run, players]  # Everything we want to change in event_handler

    while game_variables[0]:
        pygame.time.delay(100)

        event_handler(game_variables)

        draw_board(screen, square_side, screen_size)

        draw_pieces(screen, players)

        pygame.display.update()

    pygame.quit()


#
#
# SCRIPT TO RUN MAIN
#
#

if __name__ == "__main__":
    main()
