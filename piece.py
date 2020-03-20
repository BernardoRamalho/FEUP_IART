import pygame


class Piece:

    def __init__(self, x_position, y_position, direction, radius):
        self.position = (x_position, y_position)
        self.direction = direction
        self.evolved = False
        self.radius = radius

    def invert_direction(self):
        if self.direction == 'v':
            self.direction == 'h'
        else:
            self.direction == 'v'

    def evolve(self):
        self.evolved = True

    def set_position(self, new_position):
        self.position = new_position

    def get_position(self):
        return self.position

    def draw_triangle(self, screen):

        space_between_triangles = self.radius * 0.1
        half_triangle_width = self.radius * 0.2

        if self.direction == 'h':
            # Draw the first triangle
            point_1 = (self.position[0] - self.radius, self.position[1])
            point_2 = (self.position[0] - space_between_triangles, self.position[1] - half_triangle_width)
            point_3 = (self.position[0] - space_between_triangles, self.position[1] + half_triangle_width)

            points = [point_1, point_2, point_3]
            pygame.draw.polygon(screen, (0, 0, 0), points)

            # Draw the second triangle
            point_1 = (self.position[0] + self.radius, self.position[1])
            point_2 = (self.position[0] + space_between_triangles, self.position[1] - half_triangle_width)
            point_3 = (self.position[0] + space_between_triangles, self.position[1] + half_triangle_width)

            points = [point_1, point_2, point_3]
            pygame.draw.polygon(screen, (0, 0, 0), points)

        elif self.direction == 'v':
            # Draw the first triangle
            point_1 = (self.position[0], self.position[1] - self.radius)
            point_2 = (self.position[0] - half_triangle_width, self.position[1] - space_between_triangles)
            point_3 = (self.position[0] + half_triangle_width, self.position[1] - space_between_triangles)

            points = [point_1, point_2, point_3]
            pygame.draw.polygon(screen, (0, 0, 0), points)

            # Draw the second triangle
            point_1 = (self.position[0], self.position[1] + self.radius)
            point_2 = (self.position[0] - half_triangle_width, self.position[1] + space_between_triangles)
            point_3 = (self.position[0] + half_triangle_width, self.position[1] + space_between_triangles)

            points = [point_1, point_2, point_3]
            pygame.draw.polygon(screen, (0, 0, 0), points)

    def draw(self, screen, player):

        if player == 1:
            colour = (66, 135, 245)  # blue
        else:
            colour = (254, 200, 66)  # yellow

        pygame.draw.circle(screen, colour, (int(self.position[0]), int(self.position[1])), int(self.radius))

        self.draw_triangle(screen)
