import pygame
from piece import Piece
from collections import defaultdict


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
