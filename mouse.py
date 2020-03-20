import pygame


class Mouse:

    def __init__(self):
        self.position = pygame.mouse.get_pos()
        self.buttons = [0, 0, 0, 0, 1]  # Buttons 1, 2, 3, mouse_wheel roll up, mouse_wheel roll down, apple mouse
        # squeeze

    def set_position(self, new_position):
        self.position = new_position

    def button_press(self, button):
        self.buttons[button] = 1

    def button_release(self, button):
        self.buttons[button] = 0

    def check_mouse_piece_click(self, player, square_side):

        for i in player.pieces.values():
            minimum_x, minimum_y = i.position[0] - square_side / 2 / 2, i.position[1] - square_side / 2 / 2
            maximum_x, maximum_y = i.position[0] + square_side / 2 / 2, i.position[1] + square_side / 2 / 2

            if minimum_x < self.position[0] < maximum_x and minimum_y < self.position[1] < maximum_y:
                print("Click Piece at ", i.position)
