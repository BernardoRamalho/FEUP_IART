import pygame


class Piece:

    radius = 50

    def __init__(self, x_position, y_position, direction):
        self.x = x_position
        self.y = y_position
        self.direction = direction
        self.evolved = False


    def invert_direction(self):
        self.evolved = not self.evolved

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def get_y(self):
        return self.y

    def get_x(self):
        return self.x

    def draw(self, screen, player, square_side):

        if player == 1:
            colour = (66, 135, 245)  # blue
        else:
            colour = (254, 200, 66)  # yellow

        pygame.draw.circle(screen, colour, (int(self.x + square_side / 2), int(self.y + square_side / 2)), self.radius)
