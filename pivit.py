import pygame
from game import Game


# Basic Information About Structure the Game
# 1º- Game object as every variable that we need;
# 2º- You can exit the Game by pressing the key q;
# 3º- You can reset the piece you picked by pressing the key r;



#
#
# FUNCTION DEFINITION
#
#

def display_initial_message():
    print("Welcome to Pivit!")
    print("Made by Bernardo Ramalho and Pedro Pereira for IART 2020.")
    print("Player 1 as the blue pieces and player 2 as the yellow pieces")
    print("To play the game just click on a piece and then click on the square you want to move it to.")
    print("If you select the wrong piece, you can click 'r' to reset. If you want to exit the game click 'q'.")
    print("We hope you have fun!")

def get_game_mode():
    return input("Select Game Mode:\n1. PvP\n2. PvE\n3. EvE\n")


def get_screen_width():
    screen_info = pygame.display.Info()
    return screen_info.current_w


def try_move_piece(game):
    if game.player_turn == 1:

        if game.mouse.check_valid_square_click(game.square_side, game.players[0], game.players[1]):
            game.move_piece(game.mouse.piece, game.mouse.position, 1)
            game.player_turn = 2
            game.mouse.clickedPiece = False
    else:

        if game.mouse.check_valid_square_click(game.square_side, game.players[1], game.players[0]):
            game.move_piece(game.mouse.piece, game.mouse.position, 2)
            game.player_turn = 1
            game.mouse.clickedPiece = False


def event_handler_pvp(game):
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            game.mouse.button_press(event.button)
            game.mouse.transform_mouse_position(game.square_side, event.pos)

            if game.mouse.clickedPiece:
                try_move_piece(game)

            else:
                game.mouse.check_piece_click(game.players[game.player_turn - 1])

        if event.type == pygame.MOUSEBUTTONUP:
            game.mouse.button_release(event.button)

        # Key pressed
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_q:
                game.run = False

            if event.key == pygame.K_r:
                print("Pieced selected reverted.")
                game.mouse.clickedPiece = False

        # Closed Window
        if event.type == pygame.QUIT:
            game.run = False


def main():
    pygame.init()

    game = Game(get_screen_width())
    mode = get_game_mode()
    display_initial_message()

    while game.run:
        pygame.time.delay(100)

        if mode == 1: event_handler_pvp(game)

        else:  event_handler_pvp(game)

        game.draw()

        pygame.display.update()

        game.check_end_game()

    pygame.quit()


#
#
# SCRIPT TO RUN MAIN
#
#

if __name__ == "__main__":
    main()
