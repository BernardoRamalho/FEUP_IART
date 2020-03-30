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
    print("\n#################")
    print("Welcome to Pivit!")
    print("#################\n")
    print("Made by Bernardo Ramalho and Pedro Pereira for IART 2020.\n")
    print("Before we start here are some general rules of the game:")
    print("1.Player 1 has the blue pieces and Player 2 has the red pieces.")
    print("2.The point of the game is it to have more evolved pieces then your opponent at the end of the game.")
    print("3.The game ends when there are no more unenvolved pieces. To evolve a piece you just have to get it to one "
          "of the corners of the board.")
    print("4.Pieces can move in the direction their arrows point to and to a square of different colour then the one "
          "they are in. Unless they are evolved, in which case they can move to any square in that direction.")
    print("5.The last thing in mind is that you cannot jump over pieces but you can eat pieces by moving one of your "
          "pieces to an enemy occupied square.")
    print("\nBasic Commands:")
    print("To move just click on a piece and then click on the square you want to move it to.")
    print("If you select the wrong piece, you can click 'r' to reset.")
    print("If you want to exit the game click 'q'.")
    print("You can also use 'f' to forfeit a match.")
    print("\nWe give you three game modes for you to enjoy the game:")
    print("1. PvP or Player vs Player. This is where you can battle against your friends.")
    print("2. PvE or Player vs Environment. This is where you can face against our AI in case you don't have any "
          "friends.")
    print("3. EvE or Environment vs Environment. This is a mode for you to sit back and relax while you watch some AI "
          "vs AI action.")
    print("\nWe hope you have fun and enjoy our game!\n")


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

            if event.key == pygame.K_f:
                game.forfeit()

        # Closed Window
        if event.type == pygame.QUIT:
            game.run = False


def main():
    pygame.init()

    display_initial_message()
    mode = get_game_mode()
    game = Game(get_screen_width(), mode)  # Initiates the Game Master Class
    pygame.display.set_caption('Pivit')

    print("\nLet the game BEGIN!")
    game.gamestate.display_turn()
    game.draw()
    pygame.display.update()

    while game.run:
        pygame.time.delay(100)

        if game.gamestate.mode == '1':
            event_handler_pvp(game)

        elif game.gamestate.mode == '2':
            if game.gamestate.player_turn == 1:
                event_handler_pvp(game)
            else:
                game.ai_turn(5)
        else:

            game.ai_turn(5)

        game.draw()

        pygame.display.update()

        if game.gamestate.check_end_game():
            winner = game.gamestate.get_who_wins()
            display_result_message(winner)
            game.run = False

    print("\nWe hoped you liked the game. See you soon!")
    pygame.quit()


#
#
# SCRIPT TO RUN MAIN
#
#

if __name__ == "__main__":
    main()
