# Imports
import pygame as pg

# constant variables such colour, width. height
TRACK_COLOUR = (26, 83, 92)
LINE_WIDTH = 10
LINE_HEIGHT = 2
LINE_POS_X = 0
TRACK_LANE_OPACITY = 179

# Creates lines using surfaces
class TrackLineCreator:

    def __init__(self, pos_y, width = LINE_WIDTH , height = LINE_HEIGHT, pos_x  = LINE_POS_X, rgba = TRACK_COLOUR, opacity = TRACK_LANE_OPACITY):

        # setup of line / general info about line: line colour, width, opacity, and more
        self.pos = pos_x, pos_y
        self.geometry = width, height 
        self.window_width = 1042
        self.line_space_width = 12
        self.opacity = opacity
        self.line_surface = pg.Surface(self.geometry)
        self.line_surface.fill(rgba) 
        self.line_surface.set_alpha(self.opacity) 

        # creating more than one line at a time
        self.lines = []
        # this tells the computer how many lines are needed in respect to window's width and space in between lines
        for number_of_lines in range(int(self.window_width//self.line_space_width) + 1):
            self.lines.append([self.line_surface, (number_of_lines*self.line_space_width, self.pos[1])])


#Creating the instance of each lane
first_lane = TrackLineCreator(58)
second_lane = TrackLineCreator(116)
thrid_lane = TrackLineCreator(174)
forth_lane = TrackLineCreator(232)
fifth_lane = TrackLineCreator(290)

starting_lane = TrackLineCreator(0, 1, 347, 59)
finishing_lane = TrackLineCreator(0, 1, 347, 982)
divider_lane = TrackLineCreator(0, 1, 310, 521, TRACK_COLOUR, 255) # Divider lane in the white board

# Has all the trakcs in a list as it is easy to import while using less variables
tracks = [first_lane.lines, second_lane.lines, thrid_lane.lines, forth_lane.lines, fifth_lane.lines]