import pygame
import numpy as np

def get_screen_width():
    """Returns the user's screen width"""
    screen_info = pygame.display.Info()
    return screen_info.current_w

class Gui():

    def __init__(self):
        pygame.init()
        screen_info = pygame.display.Info()
        
        # Variable Initiation
        self.screen_size = int(screen_info.current_w / 3)
        self.square_side = self.screen_size / 8
        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))

    def draw(self, board, redMap, blueMap):
        pygame.time.delay(100)
        self.drawBoard()
        self.drawPieces(board, redMap, blueMap)
        pygame.display.update()

    def drawBoard(self):
        x = 0
        y = 0

        self.screen.fill((0, 0, 0))

        for i in range(8):
            for j in range(8):

                if (i + j) % 2 != 0:
                    pygame.draw.rect(self.screen, (255, 255, 255),
                                     (x, y, self.square_side, self.square_side))

                x += self.square_side

                if x > self.screen_size - self.square_side:
                    y += self.square_side

                    x = 0

    def drawPieces(self, board, redMap, blueMap):
        for position, piece_id in np.ndenumerate(board):

            if(piece_id < 0 and blueMap[piece_id * (-1)] != 'none'):
                self.drawPiece(self.screen, -1, blueMap[piece_id * -1], position)
            elif (piece_id >0 and redMap[piece_id] != 'none'):
                self.drawPiece(self.screen, 1, redMap[piece_id], position)


    def drawPiece(self, screen, player, direction, position):
        radius = self.square_side * 0.9 / 2

        # Transfom the position into a valid position for pygame
        board_position = [position[0] * self.square_side + self.square_side / 2, position[1] * self.square_side + self.square_side / 2] 

        if player == 1:  # Red Pieces
            if direction.isupper():
                colour = (255,160,122)
            else:
                colour = (255, 0, 0)
        else: # Blue Pieces
            if direction.isupper():
                colour = (118, 182, 255)
            else:
                colour = (0, 185, 255)
            

        pygame.draw.circle(screen, colour, (int(board_position[0]), int(board_position[1])), int(radius))
        self.draw_triangle(screen, board_position, radius, direction.lower())


    def draw_triangle(self, screen, position, radius, direction):

        space_between_triangles = radius * 0.1
        half_triangle_width = radius * 0.2

        if direction == 'v':
            # Draw the first triangle
            point_1 = (position[0] - radius, position[1])
            point_2 = (position[0] - space_between_triangles, position[1] - half_triangle_width)
            point_3 = (position[0] - space_between_triangles, position[1] + half_triangle_width)

            points = [point_1, point_2, point_3]
            pygame.draw.polygon(screen, (0, 0, 0), points)

            # Draw the second triangle
            point_1 = (position[0] + radius, position[1])
            point_2 = (position[0] + space_between_triangles, position[1] - half_triangle_width)
            point_3 = (position[0] + space_between_triangles, position[1] + half_triangle_width)

            points = [point_1, point_2, point_3]
            pygame.draw.polygon(screen, (0, 0, 0), points)

        elif direction == 'h':
            # Draw the first triangle
            point_1 = (position[0], position[1] - radius)
            point_2 = (position[0] - half_triangle_width, position[1] - space_between_triangles)
            point_3 = (position[0] + half_triangle_width, position[1] - space_between_triangles)

            points = [point_1, point_2, point_3]
            pygame.draw.polygon(screen, (0, 0, 0), points)

            # Draw the second triangle
            point_1 = (position[0], position[1] + radius)
            point_2 = (position[0] - half_triangle_width, position[1] + space_between_triangles)
            point_3 = (position[0] + half_triangle_width, position[1] + space_between_triangles)

            points = [point_1, point_2, point_3]
            pygame.draw.polygon(screen, (0, 0, 0), points)
