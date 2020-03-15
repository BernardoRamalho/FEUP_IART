import pygame
from piece import Piece


#
#
# FUNCTION DEFINITION
#
#

def create_pieces(player, player_pieces, square_side_size):
    if player == 2:
        player_pieces.append(Piece(square_side_size / 2, 1 * square_side_size + square_side_size / 2, 'h'))
        player_pieces.append(Piece(square_side_size / 2, 3 * square_side_size + square_side_size / 2, 'h'))
        player_pieces.append(Piece(square_side_size / 2, 4 * square_side_size + square_side_size / 2, 'h'))
        player_pieces.append(Piece(square_side_size / 2, 6 * square_side_size + square_side_size / 2, 'h'))

        player_pieces.append(
            Piece(7 * square_side_size + square_side_size / 2, 1 * square_side_size + square_side_size / 2, 'h'))
        player_pieces.append(
            Piece(7 * square_side_size + square_side_size / 2, 3 * square_side_size + square_side_size / 2, 'h'))
        player_pieces.append(
            Piece(7 * square_side_size + square_side_size / 2, 4 * square_side_size + square_side_size / 2, 'h'))
        player_pieces.append(
            Piece(7 * square_side_size + square_side_size / 2, 6 * square_side_size + square_side_size / 2, 'h'))

        player_pieces.append(Piece(2 * square_side_size + square_side_size / 2, square_side_size / 2, 'v'))
        player_pieces.append(Piece(5 * square_side_size + square_side_size / 2, square_side_size / 2, 'v'))

        player_pieces.append(
            Piece(2 * square_side_size + square_side_size / 2, 7 * square_side_size + square_side_size / 2, 'v'))
        player_pieces.append(
            Piece(5 * square_side_size + square_side_size / 2, 7 * square_side_size + square_side_size / 2, 'v'))

    else:
        player_pieces.append(Piece(1 * square_side_size + square_side_size / 2, square_side_size / 2, 'v'))
        player_pieces.append(Piece(3 * square_side_size + square_side_size / 2, square_side_size / 2, 'v'))
        player_pieces.append(Piece(4 * square_side_size + square_side_size / 2, square_side_size / 2, 'v'))
        player_pieces.append(Piece(6 * square_side_size + square_side_size / 2, square_side_size / 2, 'v'))

        player_pieces.append(
            Piece(1 * square_side_size + square_side_size / 2, 7 * square_side_size + square_side_size / 2, 'v'))
        player_pieces.append(
            Piece(3 * square_side_size + square_side_size / 2, 7 * square_side_size + square_side_size / 2, 'v'))
        player_pieces.append(
            Piece(4 * square_side_size + square_side_size / 2, 7 * square_side_size + square_side_size / 2, 'v'))
        player_pieces.append(
            Piece(6 * square_side_size + square_side_size / 2, 7 * square_side_size + square_side_size / 2, 'v'))

        player_pieces.append(Piece(square_side_size / 2, 2 * square_side_size + square_side_size / 2, 'h'))
        player_pieces.append(Piece(square_side_size / 2, 5 * square_side_size + square_side_size / 2, 'h'))

        player_pieces.append(
            Piece(7 * square_side_size + square_side_size / 2, 2 * square_side_size + square_side_size / 2, 'h'))
        player_pieces.append(
            Piece(7 * square_side_size + square_side_size / 2, 5 * square_side_size + square_side_size / 2, 'h'))


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


def draw_pieces(screen, pieces):
    for i in pieces[0]:
        i.draw(screen, 1)

    for i in pieces[1]:
        i.draw(screen, 2)


def event_handler(variables):
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                variables[0] = False

        if event.type == pygame.QUIT:
            variables[0] = False


def main():
    pygame.init()

    # Variable Initiation
    screen_size = 1200
    player1_pieces = []  # List containing all the pieces of player one
    player2_pieces = []  # List containing all the pieces of player two
    screen = pygame.display.set_mode((screen_size, screen_size))  # Where the game is shown
    square_side = screen_size / 8  # 8 because the board is 8x8
    run = True

    create_pieces(1, player1_pieces, square_side)
    create_pieces(2, player2_pieces, square_side)

    all_pieces = [player1_pieces, player2_pieces]

    game_variables = [run, all_pieces]  # Everything we want to change in event_handler

    while game_variables[0]:
        pygame.time.delay(100)

        event_handler(game_variables)

        draw_board(screen, square_side, screen_size)

        draw_pieces(screen, all_pieces)

        pygame.display.update()

    pygame.quit()


#
#
# SCRIPT TO RUN MAIN
#
#

if __name__ == "__main__":
    main()
