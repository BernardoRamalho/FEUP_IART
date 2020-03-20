import pygame
from game import Game


# Basic Information About Structure the Game
# 1º- Game object as every variable that we need;
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


def event_handler(game):
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            game.mouse.button_press(event.button)
            game.mouse.set_position(event.pos)
            game.mouse.check_mouse_piece_click(game.players[game.player_turn - 1], game.square_side)

        if event.type == pygame.MOUSEBUTTONUP:
            game.mouse.button_release(event.button)

        # Key pressed
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_q:
                game.run = False

        # Closed Window
        if event.type == pygame.QUIT:
            game.run = False


def main():
    pygame.init()

    game = Game(get_screen_width())

    while game.run:
        pygame.time.delay(100)

        event_handler(game)

        game.draw()

        pygame.display.update()

    pygame.quit()


#
#
# SCRIPT TO RUN MAIN
#
#

if __name__ == "__main__":
    main()
