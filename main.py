# Importing take place here
import pygame as pg
import sys
import race_track as rt
import white_board as wt
import question_answers as qs
import csv

class Game:
    def __init__(self):
        # Settings for the window
        self.WIDTH = 1042
        self.HEIGHT = 697
        self.FPS = 60

        # Starting pygame
        pg.init()

        # Setting up the window
        self.window = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption("QUIZ RACE")
        self.ICON_IMAGE = pg.image.load("icon.png")
        pg.display.set_icon(self.ICON_IMAGE)
        self.clock = pg.time.Clock()

        # Colours for the window
        self.window_bg = (78, 205, 196)

        # Custom cursor
        self.image_of_cursor = pg.image.load("cursor (1).png") # image of the cursor
        self.image_of_cursor_rotate = pg.transform.rotozoom(self.image_of_cursor, 30, 1)  # rotating the image
        self.cursor = pg.cursors.Cursor((11, 12), self.image_of_cursor_rotate) # putting the image in cursor widget

        self.next_que = pg.USEREVENT + 1
        pg.time.set_timer(self.next_que, 2000)

        # Checks if it is time to run to the next question
    def next_question(self):
        pg.event.post(pg.event.Event(self.next_que))

    def looper(self):
        while True:
            for events in pg.event.get():
                if events.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                
                if events.type == self.next_que:
                    qs.class_question_list[0].next_question()
                    qs.class_answer_list[0][0].next_ans()
                    qs.class_answer_list[0][1].next_ans()
                    qs.class_answer_list[0][2].next_ans()
                    qs.class_answer_list[0][3].next_ans()
                    qs.question_spirit.add(qs.class_question_list[1])
                    qs.answers_spirit.add(qs.class_answer_list[1])

            # Putting colours on the window
            self.window.fill(self.window_bg)

                # Putting the tracks on the screen
            for each_lane in rt.tracks:
                for each_step in each_lane:
                    self.window.blit(each_step[0], each_step[1])
                    self.window.blit(rt.starting_lane.line_surface, rt.starting_lane.pos)
                    self.window.blit(rt.finishing_lane.line_surface, rt.finishing_lane.pos)

            # Putting the white board on the screen
            self.window.blit(wt.main_board.surface, (0, 347))
            wt.main_board.surface.blit(wt.display_board.surface, (0, 40))
            wt.display_board.surface.blit(rt.divider_lane.line_surface, rt.divider_lane.pos)

            # Putting the questions on the screen
            qs.question_spirit.draw(wt.display_board.surface)

            # Putting the options on the screen
            qs.answers_spirit.draw(self.window)

            # if self.next_quest_ind:
            #     self.next_question()

            # Putting a custom cursor
            pg.mouse.set_cursor(self.cursor)

            # Updating the game
            pg.display.update()
            self.clock.tick(self.FPS)


if __name__ == "__main__":
    game = Game()
    game.looper()
