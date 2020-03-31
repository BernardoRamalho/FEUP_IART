import pygame
from game import Game
import console_interface

#
#
# FUNCTION DEFINITION
#
#


def transform_into_readable_position(position, game):
    square_side = game.gamestate.square_side

    return (position[0] - square_side / 2) // square_side, (position[1] - square_side / 2) // square_side


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

    console_interface.display_initial_message()
    mode = console_interface.get_game_mode()
    depth = console_interface.get_ai_depth()
    if mode == '3':
        ai_modes = console_interface.get_two_ai_modes()
    else:
        ai_modes = console_interface.get_ai_mode()
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
            console_interface.display_result_message(winner)
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
