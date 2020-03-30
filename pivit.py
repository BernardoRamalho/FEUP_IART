import pygame
from game import Game
from minimax import Minimax
import time
import heuristics_test

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


def display_result_message(winner):
    if winner == 1:
        print("Player 1 has won the game!")
    elif winner == 2:
        print("Player 2 has won the game!")
    else:
        print("We have a drawn!")


def get_game_mode():
    """Asks the user for a game mode"""
    return input("Select Game Mode:\n1. PvP\n2. PvE\n3. EvE\nDesired Mode: ")


def get_screen_width():
    """Returns the user's screen width"""
    screen_info = pygame.display.Info()
    return screen_info.current_w


def try_move_piece(game):
    """Based on the game state, tries to move the piece a player clicked"""

    if game.mouse.check_valid_square_click(game.gamestate.square_side,
                                           game.gamestate.players[game.gamestate.player_turn - 1],
                                           game.gamestate.players[game.gamestate.player_turn % 2]):
        game.gamestate.move_piece(game.mouse.piece, game.mouse.position)
        print("Player ", game.gamestate.player_turn, "moved piece to ", game.mouse.position)
        game.mouse.clickedPiece = False
        game.gamestate.change_turn()
        game.gamestate.display_turn()


def event_handler_pvp(game):
    """Responsible for receiving the user inputs and acting on them"""
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            game.mouse.button_press(event.button)
            game.mouse.transform_mouse_position(game.gamestate.square_side, event.pos)

            if game.mouse.clickedPiece:
                try_move_piece(game)

            else:
                game.mouse.check_piece_click(game.gamestate.players[game.gamestate.player_turn - 1])

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

    display_initial_message()
    mode = get_game_mode()
    game = Game(get_screen_width(), mode)  # Initiates the Game Master Class
    pygame.display.set_caption('Pivit')

    print("Let the game BEGIN!")
    game.gamestate.display_turn()
    game.draw()
    pygame.display.update()

    while game.run:
        #pygame.time.delay(100)

        if game.gamestate.mode == '1':
            event_handler_pvp(game)

        elif game.gamestate.mode == '2':
            if game.gamestate.player_turn == 1:
                event_handler_pvp(game)
            else:
                game.ai_turn(3)
        else:
            game.ai_turn(3)

        game.draw()

        pygame.display.update()

        if game.gamestate.check_end_game():
            winner = game.gamestate.get_who_wins()
            display_result_message(winner)
            game.run = False

    print("We hoped you liked the game. See you soon!")
    pygame.quit()


#
#
# SCRIPT TO RUN MAIN
#
#

if __name__ == "__main__":
    main()
