import pygame
from piece import Piece


def create_pieces(player, player_pieces, square_side_size):
    if player == 2:
        player_pieces.append(Piece(0, 1 * square_side_size, 'v'))
        player_pieces.append(Piece(0, 3 * square_side_size, 'v'))
        player_pieces.append(Piece(0, 4 * square_side_size, 'v'))
        player_pieces.append(Piece(0, 6 * square_side_size, 'v'))

        player_pieces.append(Piece(7 * square_side_size, 1 * square_side_size, 'v'))
        player_pieces.append(Piece(7 * square_side_size, 3 * square_side_size, 'v'))
        player_pieces.append(Piece(7 * square_side_size, 4 * square_side_size, 'v'))
        player_pieces.append(Piece(7 * square_side_size, 6 * square_side_size, 'v'))

        player_pieces.append(Piece(2 * square_side_size, 0, 'h'))
        player_pieces.append(Piece(5 * square_side_size, 0, 'h'))

        player_pieces.append(Piece(2 * square_side_size, 7 * square_side_size, 'h'))
        player_pieces.append(Piece(5 * square_side_size, 7 * square_side_size, 'h'))

    else:
        player_pieces.append(Piece(1 * square_side_size, 0, 'h'))
        player_pieces.append(Piece(3 * square_side_size, 0, 'h'))
        player_pieces.append(Piece(4 * square_side_size, 0, 'h'))
        player_pieces.append(Piece(6 * square_side_size, 0, 'h'))

        player_pieces.append(Piece(1 * square_side_size, 7 * square_side_size, 'h'))
        player_pieces.append(Piece(3 * square_side_size, 7 * square_side_size, 'h'))
        player_pieces.append(Piece(4 * square_side_size, 7 * square_side_size, 'h'))
        player_pieces.append(Piece(6 * square_side_size, 7 * square_side_size, 'h'))

        player_pieces.append(Piece(0, 2 * square_side_size, 'v'))
        player_pieces.append(Piece(0, 5 * square_side_size, 'v'))

        player_pieces.append(Piece(7 * square_side_size, 2 * square_side_size, 'v'))
        player_pieces.append(Piece(7 * square_side_size, 5 * square_side_size, 'v'))


pygame.init()

screen_size = 1200

screen = pygame.display.set_mode((screen_size, screen_size))

run = True
paint = False

player1_pieces = []
player2_pieces = []

square_side = screen_size / 8

create_pieces(1, player1_pieces, square_side)

create_pieces(2, player2_pieces, square_side)

while run:
    pygame.time.delay(100)

    x = 0
    y = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0, 0, 0))

    for i in range(64):

        if paint:
            paint = False
            pygame.draw.rect(screen, (255, 255, 255), (x, y, square_side, square_side))
        else:
            paint = True

        x += square_side

        if x > screen_size - square_side:
            y += square_side

            x = 0

            if paint:
                paint = False
            else:
                paint = True

    for i in player1_pieces:
       i.draw(screen, 1, square_side)

    for i in player2_pieces:
        i.draw(screen, 2, square_side)

    pygame.display.update()

pygame.quit()
