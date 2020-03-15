import pygame


class Piece:
    radius = 50

    def __init__(self, x_position, y_position, direction):
        self.position = [x_position, y_position]
        self.direction = direction
        self.evolved = False

    def invert_direction(self):
        self.evolved = not self.evolved

    def set_position(self, new_position):
        self.position = new_position

    def get_position(self):
        return self.position

    def draw_triangle(self, screen, triangle_number):

        if self.direction == 'h':
            if triangle_number == 1:
                point_1 = (self.position[0] - self.radius, self.position[1])
                point_2 = (self.position[0] - 5, self.position[1] - 15)
                point_3 = (self.position[0] - 5, self.position[1] + 15)

                points = [point_1, point_2, point_3]
                pygame.draw.polygon(screen, (0, 0, 0), points)

            else:
                point_1 = (self.position[0] + self.radius, self.position[1])
                point_2 = (self.position[0] + 5, self.position[1] - 15)
                point_3 = (self.position[0] + 5, self.position[1] + 15)

                points = [point_1, point_2, point_3]
                pygame.draw.polygon(screen, (0, 0, 0), points)

        elif self.direction == 'v':
            if triangle_number == 1:
                point_1 = (self.position[0], self.position[1] - self.radius)
                point_2 = (self.position[0] - 15, self.position[1] - 5)
                point_3 = (self.position[0] + 15, self.position[1] - 5)

                points = [point_1, point_2, point_3]
                pygame.draw.polygon(screen, (0, 0, 0), points)

            else:
                point_1 = (self.position[0], self.position[1] + self.radius)
                point_2 = (self.position[0] - 15, self.position[1] + 5)
                point_3 = (self.position[0] + 15, self.position[1] + 5)

                points = [point_1, point_2, point_3]
                pygame.draw.polygon(screen, (0, 0, 0), points)

    def draw(self, screen, player):

        if player == 1:
            colour = (66, 135, 245)  # blue
        else:
            colour = (254, 200, 66)  # yellow

        pygame.draw.circle(screen, colour, (int(self.position[0]), int(self.position[1])), int(self.radius))

        self.draw_triangle(screen, 1)
        self.draw_triangle(screen, 2)
