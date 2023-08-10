# Imports all here
import pygame as pg

# Generates Surfaces
class GeneratesSurface:
    def __init__(self, width, height, main_colour, board_colour, borderi):
        self.geometry = width, height
        self.surface = pg.Surface(self.geometry)
        self.surface_colour = self.surface.fill(main_colour)
        self.board_colour = self.surface.fill(board_colour, borderi)

# Instance of the class/ the boards creation
main_board = GeneratesSurface(1042, 350, (247, 255, 247), (26, 83, 92), (0, 0, 1042, 1))
display_board = GeneratesSurface(1042, 309, (247, 255, 247), (26, 83, 92), (0, 0, 1042, 1))