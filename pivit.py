import pygame
from game import Game
from gamestate import GameState
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
    print("If you want a suggestion from the AI you can click 'd'.")
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


def transform_into_readable_position(position, game):
    square_side = game.gamestate.square_side

    return (position[0] - square_side / 2) // square_side, (position[1] - square_side / 2) // square_side


def get_game_mode():
    """Asks the user for a game mode"""
    mode = input("Select Game Mode:\n1. PvP\n2. PvE\n3. EvE\nDesired Mode: ")

    if mode != '1' and mode != '2' and mode != '3':
        return ask_game_mode_again()
    else:
        return mode


def ask_game_mode_again():
    mode = input("Please select a valida Game Mode:\n1. PvP\n2. PvE\n3. EvE\nDesired Mode: ")

    if mode != '1' and mode != '2' and mode != '3':
        return ask_game_mode_again()
    else:
        return mode


def get_ai_depth():
    """Asks the user for the depth to be used for the AI"""
    print("Please choose the depth to which the AI should search.")
    print("The bigger the depth the more time it will take for the AI to choose a move. You can choose between 1 and "
          "17.")
    print("We recommend choosing 3 or 4. 3 will take, in average, around 2 seconds and 4 will take , in average,"
          "around 45 seconds.")
    print("In our testing, in depth 5 it took between 3:30 minutes and 2:30 minutes. We couldn't access further then 5"
          " depth so adventure at your own risk.\n")
    print("All those times will vary depends on your computer's power.")
    depth = int(input("Desired Depth: "))

    if depth < 1 or depth > 17:
        return ask_depth_again()
    else:
        return depth


def ask_depth_again():
    print("You inserted an invalid depth.")
    depth = int(input("Please insert a value between 1 and 17: "))

    if depth < 1 or depth > 17:
        return ask_depth_again()
    else:
        return depth


def get_ai_mode():
    print("Please select the ai mode you desire:")
    ai_mode = input("1.Aggressive\n2.Defensive\n3.Neutral\nDesired mode:")

    if ai_mode != '1' and ai_mode != '2' and ai_mode != '3':
        return ask_ai_mode_again()
    else:
        return ai_mode, 0


def ask_ai_mode_again():
    print("Please select a valid ai mode:")
    ai_mode = input("1.Aggressive\n2.Defensive\n3.Neutral\nDesired mode:")

    if ai_mode != '1' and ai_mode != '2' and ai_mode != '3':
        return ask_ai_mode_again()
    else:
        return ai_mode, 0


def get_two_ai_modes():
    print("Mode for the 1st AI")
    ai_mode1 = get_ai_mode()
    print("Mode for the 2nd AI")
    ai_mode2 = get_ai_mode()

    return ai_mode1, ai_mode2


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
        print("Player ", game.gamestate.player_turn, "moved piece to ",
              transform_into_readable_position(game.mouse.position, game))
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

            elif event.key == pygame.K_r:
                print("Pieced selected reverted.")
                game.mouse.clickedPiece = False

            elif event.key == pygame.K_f:
                game.forfeit()

            elif event.key == pygame.K_d:
                suggested_move = game.gamestate.ai_player2.play(game.gamestate, 3)
                suggested_move[0] = transform_into_readable_position(suggested_move[0], game)
                suggested_move[1] = transform_into_readable_position(suggested_move[1], game)
                print("The AI suggest you move the piece at position", suggested_move[0], "to", suggested_move[1], ".")

        # Closed Window
        if event.type == pygame.QUIT:
            game.run = False


def event_handler_ai(game):
    """Responsible for receiving the user inputs and acting on them"""
    for event in pygame.event.get():
        # Key pressed
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_q:
                game.run = False

        # Closed Window
        if event.type == pygame.QUIT:
            game.run = False


def main():
    pygame.init()

    display_initial_message()
    mode = get_game_mode()
    depth = get_ai_depth()
    if mode == '3':
        ai_modes = get_two_ai_modes()
    else:
        ai_modes = get_ai_mode()
    game = Game(get_screen_width(), mode, depth, ai_modes)  # Initiates the Game Master Class
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
                event_handler_ai(game)
                game.gamestate.ai_turn(game.gamestate.ai_player2)
        else:
            event_handler_ai(game)
            if game.gamestate.player_turn == 1:
                game.gamestate.ai_turn(game.gamestate.ai_player1)
            else:
                game.gamestate.ai_turn(game.gamestate.ai_player2)

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
