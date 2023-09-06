# Importing take place here
import pygame as pg
import sys
import race_track as rt
import white_board as wt
import question_answers as qs
from datetime import datetime as dt

class Game:
    def __init__(self):
        # Settings for the window
        self.WIDTH = 1042
        self.HEIGHT = 697
        self.FPS = 90

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

        # Telll the loop function if it is time for the next question as well stores te value for the next question number
        self.moving_to_next = False
        self.question_number = 0
        self.total_question_len = qs.num_questions_answers - 2
        self.current_time = 0
        self.button_pressed_time = 0
        self.next_ques_in = 2
        self.updates_ques_num = 0
        self.wrong_question_num = 0

    def looper(self):
        while True:
            for events in pg.event.get():
                if events.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if self.question_number < (len(qs.class_question_list) - 1): # Minusing 2 from the original list of question to keep it below the last question:
                    if self.moving_to_next:
                        # Checking if it is time to move to next question
                        self.current_time = dt.now()
                        self.time = (self.current_time - self.button_pressed_time)

                        if int(self.time.total_seconds()) > self.next_ques_in:
                            pass
                        else:
                            while True:
                                self.current_time = dt.now()
                                self.time = (self.current_time - self.button_pressed_time)
                                if int(self.time.total_seconds()) > self.next_ques_in:
                                    break

                        if int(self.time.total_seconds()) > self.next_ques_in:
                            qs.class_question_list[self.question_number].next_question()
                            qs.class_answer_list[self.question_number][0].next_ans()
                            qs.class_answer_list[self.question_number][1].next_ans()
                            qs.class_answer_list[self.question_number][2].next_ans()
                            qs.class_answer_list[self.question_number][3].next_ans()
                            qs.button_states[0] = False
                            qs.button_states[1] = False
                            qs.button_states[2] = False
                            qs.button_states[3] = False
                            self.question_number += 1
                            self.updates_ques_num = self.question_number
                            qs.question_spirit.add(qs.class_question_list[self.question_number])
                            qs.answers_spirit.add(qs.class_answer_list[self.question_number])
                            qs.question_ans_num = self.question_number
                            self.moving_to_next = False
    
                else:
                    self.question_number = self.question_number
                    qs.question_ans_num = self.question_number

                        
            # Putting colours on the window
            self.window.fill(self.window_bg)
            self.current_time = pg.time.get_ticks()

            # Putting the white board on the screen
            self.window.blit(wt.main_board.surface, (0, 347))
            wt.main_board.surface.blit(wt.display_board.surface, (0, 40))

            # Putting the questions on the screen
            qs.question_spirit.draw(self.window)
            qs.class_question_list[self.question_number].update()

            # Putting the options on the screen
            qs.answers_spirit.draw(self.window)
            button_pressed_1 = qs.class_answer_list[self.question_number][0].update()
            button_pressed_2 = qs.class_answer_list[self.question_number][1].update()
            button_pressed_3 = qs.class_answer_list[self.question_number][2].update()
            button_pressed_4 = qs.class_answer_list[self.question_number][3].update()

            if True in qs.button_states:
                self.moving_to_next = True
            
            if button_pressed_1 == True or button_pressed_2 == True or button_pressed_3 == True or button_pressed_4 == True:
                self.button_pressed_time = dt.now()

                if (qs.actual_que_num + 1) < len(qs.answer_check_copy):
                    if qs.answer_check_copy[len(qs.answer_check_copy)-1]:
                        qs.wrong_answer_store.pop(self.wrong_question_num)
                        if self.wrong_question_num > 0:
                            self.wrong_question_num -= 1
                    else:
                        # Making instance of questions
                        qs.class_question_list.append(qs.QuestionMaker(f"Q{len(qs.class_question_list) + 1}", qs.questions_list[qs.wrong_answer_store[self.wrong_question_num][0]][1]))

                        # Making of answers with spirits
                        qs.class_answer_list.append([qs.AnswerMaker_A("A", qs.questions_list[qs.wrong_answer_store[self.wrong_question_num][0]][2], qs.questions_list[qs.wrong_answer_store[self.wrong_question_num][0]][6], qs.opt_colr_list[0]), 
                                                qs.AnswerMaker_B("B", qs.questions_list[qs.wrong_answer_store[self.wrong_question_num][0]][3], qs.questions_list[qs.wrong_answer_store[self.wrong_question_num][0]][6], qs.opt_colr_list[1]),
                                                qs.AnswerMaker_C("C", qs.questions_list[qs.wrong_answer_store[self.wrong_question_num][0]][4], qs.questions_list[qs.wrong_answer_store[self.wrong_question_num][0]][6], qs.opt_colr_list[2]),
                                                qs.AnswerMaker_D("D", qs.questions_list[qs.wrong_answer_store[self.wrong_question_num][0]][5], qs.questions_list[qs.wrong_answer_store[self.wrong_question_num][0]][6], qs.opt_colr_list[3])
                                                ])
                        
                        self.wrong_question_num += 1
                        if self.wrong_question_num > len(qs.wrong_answer_store) - 1:
                            self.wrong_question_num = 0


            # Putting a custom cursor
            pg.mouse.set_cursor(self.cursor)

            # Updating the game
            pg.display.update()
            self.clock.tick(self.FPS)


if __name__ == "__main__":
    game = Game()
    game.looper()

# Q3,(2x + 3x) = 10, x = 2,x = 5,x = 1,x = 2.5, x = 2
# Q4,What is School Speed Zone ?,40,50 ,20 ,30,40
# Q5,New Zealand Captical ?,Welligton,Auckland,Waikto,Christchurch,Welligton
# Q6,Formula for Power ?,P = W/t,P = A/F,W = Fd,v = d/t,P = W/t