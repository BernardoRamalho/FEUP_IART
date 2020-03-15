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

    def draw_triangle(self, screen, triangle_number):

        if self.direction == 'h':
            if triangle_number == 1:
                point_1 = (self.x - self.radius, self.y)
                point_2 = (self.x - 5, self.y - 15)
                point_3 = (self.x - 5, self.y + 15)

                points = [point_1, point_2, point_3]
                pygame.draw.polygon(screen, (0, 0, 0), points)

            else:
                point_1 = (self.x + self.radius, self.y)
                point_2 = (self.x + 5, self.y - 15)
                point_3 = (self.x + 5, self.y + 15)

                points = [point_1, point_2, point_3]
                pygame.draw.polygon(screen, (0, 0, 0), points)

        elif self.direction == 'v':
            if triangle_number == 1:
                point_1 = (self.x, self.y - self.radius)
                point_2 = (self.x - 15, self.y - 5)
                point_3 = (self.x + 15, self.y - 5)

                points = [point_1, point_2, point_3]
                pygame.draw.polygon(screen, (0, 0, 0), points)

            else:
                point_1 = (self.x, self.y + self.radius)
                point_2 = (self.x - 15, self.y + 5)
                point_3 = (self.x + 15, self.y + 5)

                points = [point_1, point_2, point_3]
                pygame.draw.polygon(screen, (0, 0, 0), points)

    def draw(self, screen, player):

        if player == 1:
            colour = (66, 135, 245)  # blue
        else:
            colour = (254, 200, 66)  # yellow

        pygame.draw.circle(screen, colour, (int(self.x), int(self.y)), int(self.radius))

        self.draw_triangle(screen, 1)
        self.draw_triangle(screen, 2)
