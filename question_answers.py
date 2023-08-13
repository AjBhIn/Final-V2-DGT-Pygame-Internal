from typing import Any
import pygame as pg
import white_board as wt
import random
import csv

# Settings for the font
JURA_BOLD = "Jura-Bold.ttf"
QUESTION_SIZE = 30
QUESTION_NUM_COLOUR = (255, 107, 107)
QUESTION_COLOUR = (0,0,0)

# Colours for the options
RED_COLOUR = (235, 62, 62)
YELLOW_COLOUR = (255, 215, 20)
GREEN_COLOUR = (39, 239, 83)
BLUE_COLOUR = (20, 153, 228)
opt_colr_list = [RED_COLOUR, YELLOW_COLOUR, GREEN_COLOUR, BLUE_COLOUR]

pg.init()

# Creating a class for question
class QuestionMaker(pg.sprite.Sprite):

    def next_question(self):
        self.kill()

    def __init__(self, question_num, question,  font_style = JURA_BOLD, font_size = QUESTION_SIZE, q_contain_colr = (247, 255, 247), q_num_col = QUESTION_NUM_COLOUR, q_col = QUESTION_COLOUR):
        # Starting / Initialising pygame/ starting pygame
        super().__init__()
        
        # Setting up the font style
        self.font_style = pg.font.Font(font_style, font_size)
        self.question_num_width = self.font_style.size(question_num)[0]
        self.question_width = self.font_style.size(question)[0]
        self.anitalias = True

        # Setting for the question container
        self.ques_container_col = q_contain_colr
        self.height = 32
        self.width = 30 + self.question_width + self.question_num_width
        # self.question_container_x = int(wt.display_board.surface.get_width()/4)
        # self.question_container_y = int(wt.display_board.surface.get_height()/2)
        self.image = pg.Surface((self.width, self.height))
        self.rect = self.image.get_rect(center = (250, 545))
        self.image.fill(self.ques_container_col)

        # Question num
        self.question_num = self.font_style.render(question_num,self.anitalias, q_num_col)
        self.question_num_placment = self.question_num.get_rect(midleft = (10, (self.height/2)))
        self.image.blit(self.question_num, self.question_num_placment)

        # Question
        self.question_x = 20 + self.question_num_width
        self.question = self.font_style.render(question, self.anitalias, q_col)
        self.question_placment = self.question.get_rect(midleft = (self.question_x, (self.height/2)))
        self.image.blit(self.question, self.question_placment)


# Settings for the font options and answers
opt_font_size = 28
opt_font_colr = (255, 255, 255)
JURA_MEDIUM = "Jura-Medium.ttf"
button_states = [False, False, False, False]

class SettingsAnswer:
        
    def __init__(self, opt_font = JURA_BOLD, opt_size = opt_font_size, ans_font = JURA_MEDIUM, font_colr = opt_font_colr):
        # Setting the font style for the options
        self.font_sty_opt = pg.font.Font(opt_font, opt_size)
        self.font_sty_ans = pg.font.Font(ans_font, opt_size)
        self.anitalias = True
        self.font_colr = font_colr

        # Making the answer container / settings for it
        self.width = 510
        self.height = 70
        self.opt_y = int(self.height / 2)
        self.opt_x = 25
        self.ans_x = int(self.width / 2)
        self.ans_y = int(self.height / 2)

# Creating a class for answers
class AnswerMaker_A(pg.sprite.Sprite, SettingsAnswer):

    def update(self):
        self.cliked()

    def next_ans(self):
        self.kill()

    def check_own(self):
        #  Setting up the images and their placment
        correct_icon = pg.image.load("correct  image.png").convert_alpha()
        correct_icon_pla = correct_icon.get_rect(midleft = (461, int(self.height / 2)))
        wrong_icon = pg.image.load("wrong.png").convert_alpha()
        wrong_icon_pla = wrong_icon.get_rect(midleft = (461, int(self.height / 2)))

        if self.anss == self.correct_answer:
            class_answer_list[question_ans_num][0].image.blit(correct_icon, correct_icon_pla)
            class_answer_list[question_ans_num][1].image.set_alpha(127)
            class_answer_list[question_ans_num][1].image.blit(wrong_icon, wrong_icon_pla)
            class_answer_list[question_ans_num][2].image.set_alpha(127)
            class_answer_list[question_ans_num][2].image.blit(wrong_icon, wrong_icon_pla)
            class_answer_list[question_ans_num][3].image.set_alpha(127)
            class_answer_list[question_ans_num][3].image.blit(wrong_icon, wrong_icon_pla)
        else:
            class_answer_list[question_ans_num][0].image.blit(wrong_icon, wrong_icon_pla)
            if class_answer_list[question_ans_num][1].anss == self.correct_answer:
                class_answer_list[question_ans_num][1].image.set_alpha(127)
                class_answer_list[question_ans_num][1].image.blit(correct_icon, correct_icon_pla)
            else:
                class_answer_list[question_ans_num][1].image.set_alpha(127)
                class_answer_list[question_ans_num][1].image.blit(wrong_icon, wrong_icon_pla) 

            if class_answer_list[question_ans_num][2].anss == self.correct_answer:
                class_answer_list[question_ans_num][2].image.set_alpha(127)
                class_answer_list[question_ans_num][2].image.blit(correct_icon, correct_icon_pla)
            else:
                class_answer_list[question_ans_num][2].image.set_alpha(127)
                class_answer_list[question_ans_num][2].image.blit(wrong_icon, wrong_icon_pla) 

            if class_answer_list[question_ans_num][3].anss == self.correct_answer:
                class_answer_list[question_ans_num][3].image.set_alpha(127)
                class_answer_list[question_ans_num][3].image.blit(correct_icon, correct_icon_pla)
            else:
                class_answer_list[question_ans_num][3].image.set_alpha(127)
                class_answer_list[question_ans_num][3].image.blit(wrong_icon, wrong_icon_pla)


        # if value == "A":
        #     if self.anss == self.correct_answer:
        #         class_answer_list[question_ans_num][0].image.blit(correct_icon, correct_icon_pla)
        #         class_answer_list[question_ans_num][1].image.set_alpha(127)
        #         class_answer_list[question_ans_num][1].image.blit(wrong_icon, wrong_icon_pla)
        #         class_answer_list[question_ans_num][2].image.set_alpha(127)
        #         class_answer_list[question_ans_num][2].image.blit(wrong_icon, wrong_icon_pla)
        #         class_answer_list[question_ans_num][3].image.set_alpha(127)
        #         class_answer_list[question_ans_num][3].image.blit(wrong_icon, wrong_icon_pla)
        #     else:
        #         class_answer_list[question_ans_num][0].image.blit(wrong_icon, wrong_icon_pla)
        #         if class_answer_list[question_ans_num][1].anss == self.correct_answer:
        #             class_answer_list[question_ans_num][1].image.set_alpha(127)
        #             class_answer_list[question_ans_num][1].image.blit(correct_icon, correct_icon_pla)
        #         else:
        #             class_answer_list[question_ans_num][1].image.set_alpha(127)
        #             class_answer_list[question_ans_num][1].image.blit(wrong_icon, wrong_icon_pla) 

        #         if class_answer_list[question_ans_num][2].anss == self.correct_answer:
        #             class_answer_list[question_ans_num][2].image.set_alpha(127)
        #             class_answer_list[question_ans_num][2].image.blit(correct_icon, correct_icon_pla)
        #         else:
        #             class_answer_list[question_ans_num][2].image.set_alpha(127)
        #             class_answer_list[question_ans_num][2].image.blit(wrong_icon, wrong_icon_pla) 

        #         if class_answer_list[question_ans_num][3].anss == self.correct_answer:
        #             class_answer_list[question_ans_num][3].image.set_alpha(127)
        #             class_answer_list[question_ans_num][3].image.blit(correct_icon, correct_icon_pla)
        #         else:
        #             class_answer_list[question_ans_num][3].image.set_alpha(127)
        #             class_answer_list[question_ans_num][3].image.blit(wrong_icon, wrong_icon_pla)


    #     if value == "B":
    #         if self.anss == self.correct_answer:
    #             class_answer_list[question_ans_num][1].image.blit(correct_icon, correct_icon_pla)
    #             class_answer_list[question_ans_num][0].image.set_alpha(127)
    #             class_answer_list[question_ans_num][0].image.blit(wrong_icon, wrong_icon_pla)
    #             class_answer_list[question_ans_num][2].image.set_alpha(127)
    #             class_answer_list[question_ans_num][2].image.blit(wrong_icon, wrong_icon_pla)
    #             class_answer_list[question_ans_num][3].image.set_alpha(127)
    #             class_answer_list[question_ans_num][3].image.blit(wrong_icon, wrong_icon_pla)
    #         else:
    #             class_answer_list[question_ans_num][1].image.blit(wrong_icon, wrong_icon_pla)
    #             if class_answer_list[question_ans_num][0].anss == self.correct_answer:
    #                 class_answer_list[question_ans_num][0].image.set_alpha(127)
    #                 class_answer_list[question_ans_num][0].image.blit(correct_icon, correct_icon_pla)
    #             else:
    #                 class_answer_list[question_ans_num][0].image.set_alpha(127)
    #                 class_answer_list[question_ans_num][0].image.blit(wrong_icon, wrong_icon_pla) 

    #             if class_answer_list[question_ans_num][2].anss == self.correct_answer:
    #                 class_answer_list[question_ans_num][2].image.set_alpha(127)
    #                 class_answer_list[question_ans_num][2].image.blit(correct_icon, correct_icon_pla)
    #             else:
    #                 class_answer_list[question_ans_num][2].image.set_alpha(127)
    #                 class_answer_list[question_ans_num][2].image.blit(wrong_icon, wrong_icon_pla) 

    #             if class_answer_list[question_ans_num][3].anss == self.correct_answer:
    #                 class_answer_list[question_ans_num][3].image.set_alpha(127)
    #                 class_answer_list[question_ans_num][3].image.blit(correct_icon, correct_icon_pla)
    #             else:
    #                 class_answer_list[question_ans_num][3].image.set_alpha(127)
    #                 class_answer_list[question_ans_num][3].image.blit(wrong_icon, wrong_icon_pla) 


    #     if value == "C":
    #         if self.anss == self.correct_answer:
    #             class_answer_list[question_ans_num][2].image.blit(correct_icon, correct_icon_pla)
    #             class_answer_list[question_ans_num][0].image.set_alpha(127)
    #             class_answer_list[question_ans_num][0].image.blit(wrong_icon, wrong_icon_pla)
    #             class_answer_list[question_ans_num][1].image.set_alpha(127)
    #             class_answer_list[question_ans_num][1].image.blit(wrong_icon, wrong_icon_pla)
    #             class_answer_list[question_ans_num][3].image.set_alpha(127)
    #             class_answer_list[question_ans_num][3].image.blit(wrong_icon, wrong_icon_pla)
    #         else:
    #             class_answer_list[question_ans_num][2].image.blit(wrong_icon, wrong_icon_pla)
    #             if class_answer_list[question_ans_num][0].anss == self.correct_answer:
    #                 class_answer_list[question_ans_num][0].image.set_alpha(127)
    #                 class_answer_list[question_ans_num][0].image.blit(correct_icon, correct_icon_pla)
    #             else:
    #                 class_answer_list[question_ans_num][0].image.set_alpha(127)
    #                 class_answer_list[question_ans_num][0].image.blit(wrong_icon, wrong_icon_pla) 

    #             if class_answer_list[question_ans_num][1].anss == self.correct_answer:
    #                 class_answer_list[question_ans_num][1].image.set_alpha(127)
    #                 class_answer_list[question_ans_num][1].image.blit(correct_icon, correct_icon_pla)
    #             else:
    #                 class_answer_list[question_ans_num][1].image.set_alpha(127)
    #                 class_answer_list[question_ans_num][1].image.blit(wrong_icon, wrong_icon_pla) 

    #             if class_answer_list[question_ans_num][3].anss == self.correct_answer:
    #                 class_answer_list[question_ans_num][3].image.set_alpha(127)
    #                 class_answer_list[question_ans_num][3].image.blit(correct_icon, correct_icon_pla)
    #             else:
    #                 class_answer_list[question_ans_num][3].image.set_alpha(127)
    #                 class_answer_list[question_ans_num][3].image.blit(wrong_icon, wrong_icon_pla) 


    #     if value == "D":
    #         if self.anss == self.correct_answer:
    #             class_answer_list[question_ans_num][3].image.blit(correct_icon, correct_icon_pla)
    #             class_answer_list[question_ans_num][0].image.set_alpha(127)
    #             class_answer_list[question_ans_num][0].image.blit(wrong_icon, wrong_icon_pla)
    #             class_answer_list[question_ans_num][1].image.set_alpha(127)
    #             class_answer_list[question_ans_num][1].image.blit(wrong_icon, wrong_icon_pla)
    #             class_answer_list[question_ans_num][2].image.set_alpha(127)
    #             class_answer_list[question_ans_num][2].image.blit(wrong_icon, wrong_icon_pla)
    #         else:
    #             class_answer_list[question_ans_num][3].image.blit(wrong_icon, wrong_icon_pla)
    #             if class_answer_list[question_ans_num][0].anss == self.correct_answer:
    #                 class_answer_list[question_ans_num][0].image.set_alpha(127)
    #                 class_answer_list[question_ans_num][0].image.blit(correct_icon, correct_icon_pla)
    #             else:
    #                 class_answer_list[question_ans_num][0].image.set_alpha(127)
    #                 class_answer_list[question_ans_num][0].image.blit(wrong_icon, wrong_icon_pla) 

    #             if class_answer_list[question_ans_num][1].anss == self.correct_answer:
    #                 class_answer_list[question_ans_num][1].image.set_alpha(127)
    #                 class_answer_list[question_ans_num][1].image.blit(correct_icon, correct_icon_pla)
    #             else:
    #                 class_answer_list[question_ans_num][1].image.set_alpha(127)
    #                 class_answer_list[question_ans_num][1].image.blit(wrong_icon, wrong_icon_pla) 

    #             if class_answer_list[question_ans_num][2].anss == self.correct_answer:
    #                 class_answer_list[question_ans_num][2].image.set_alpha(127)
    #                 class_answer_list[question_ans_num][2].image.blit(correct_icon, correct_icon_pla)
    #             else:
    #                 class_answer_list[question_ans_num][2].image.set_alpha(127)
    #                 class_answer_list[question_ans_num][2].image.blit(wrong_icon, wrong_icon_pla) 
                

    def cliked(self):
    # Getting the mouse position
        mouse_pos = pg.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            # print("Button A Hover")
            # if pg.mouse.get_pressed()[0] and self.opt_A_state == False and self.opt_B_state == False and self.opt_C_state == False and self.opt_D_state == False:
            #     self.opt_A_state = True
            #     print("Ok A")
            if pg.mouse.get_pressed()[0] and button_states[0] == False and button_states[1] == False and button_states[2] == False and button_states[3] == False:
                button_states[0] = True
                print(button_states)
                self.check_own()
                print("Ok A")

    #         elif pg.mouse.get_pressed()[0] and self.option == "B" and self.opt_state == False:
    #             self.opt_state = True
    #             print("Ok B")

    #         elif pg.mouse.get_pressed()[0] and self.option == "C" and self.opt_state == False:
    #             self.opt_state = True
    #             print("Ok C")

    #         elif pg.mouse.get_pressed()[0] and self.option == "D" and self.opt_state == False:
    #             self.opt_state = True
    #             print("Ok D")
            #     if self.option == "A":
            #         self.opt_A_state = True
            #         self.opt_B_state = False
            #         self.opt_C_state = False
            #         self.opt_D_state = False
            #     if self.option == "B":
            #         self.opt_A_state = False
            #         self.opt_B_state = True
            #         self.opt_C_state = False
            #         self.opt_D_state = False
            #     if self.option == "C":
            #         self.opt_A_state = False
            #         self.opt_B_state = False
            #         self.opt_C_state = True
            #         self.opt_D_state = False
            #     if self.option == "D":
            #         self.opt_A_state = False
            #         self.opt_B_state = False
            #         self.opt_C_state = False
            #         self.opt_D_state = True
            # else:
            #     if self.opt_A_state:
            #             print("option A Pressed")
            #             self.check("A")
            #             self.opt_A_state = False
            #             self.opt_B_state = False
            #             self.opt_C_state = False
            #             self.opt_D_state = False
            #     elif self.opt_B_state:
            #             print("option B Pressed")
            #             self.check("B")
            #             self.opt_A_state = False
            #             self.opt_B_state = False
            #             self.opt_C_state = False
            #             self.opt_D_state = False
            #     elif self.opt_C_state:
            #             print("option C Pressed")
            #             self.check("C")
            #             self.opt_A_state = False
            #             self.opt_B_state = False
            #             self.opt_C_state = False
            #             self.opt_D_state = False
            #     elif self.opt_D_state:
            #             print("option D Pressed")
            #             self.check("D")
            #             self.opt_A_state = False
            #             self.opt_B_state = False
            #             self.opt_C_state = False
            #             self.opt_D_state = False

    def __init__(self, option, answers, correct_answer, cont_colors):
        # Calling spirit class
        super().__init__()
        SettingsAnswer.__init__(self)

        self.option = option
        # Answers and correct container
        self.anss = answers
        self.correct_answer = correct_answer
            # Option container
        self.image = pg.Surface((self.width, self.height))
        self.image.fill(cont_colors)
        self.rect = self.image.get_rect(topleft = (527, 394))

        self.opt_A = self.font_sty_opt.render(self.option, self.anitalias, self.font_colr)
        self.opt_A_plac = self.opt_A.get_rect(center = (self.opt_x, self.opt_y))
        self.image.blit(self.opt_A, self.opt_A_plac)

        self.ans_A = self.font_sty_ans.render(answers, self.anitalias, self.font_colr)
        self.ans_A_plac = self.ans_A.get_rect(center = (self.ans_x, self.ans_y))
        self.image.blit(self.ans_A, self.ans_A_plac)

        #     # Option B container
        # self.opt_B_state = False
        # self.opt_B_cont = pg.Surface((self.width, self.height))
        # self.opt_B_cont.fill(cont_colors)
        # self.opt_B_cont_plac = self.opt_B_cont.get_rect(topleft = (527, 470))
        # self.opt_B = self.font_sty_opt.render("B", self.anitalias, font_colr)
        # self.opt_B_plac = self.opt_B.get_rect(center = (self.opt_x, self.opt_y))
        # self.opt_B_cont.blit(self.opt_B, self.opt_B_plac)
        # self.ans_B = self.font_sty_ans.render(answers[1], self.anitalias, font_colr)
        # self.ans_B_plac = self.ans_B.get_rect(center = (self.ans_x, self.ans_y))
        # self.opt_B_cont.blit(self.ans_B, self.ans_B_plac)
        #     # Option C container
        # self.opt_C_state = False
        # self.opt_C_cont = pg.Surface((self.width, self.height))
        # self.opt_C_cont.fill(opt_colrs[2])
        # self.opt_C_cont_plac = self.opt_C_cont.get_rect(topleft = (527, 546))
        # self.opt_C = self.font_sty_opt.render("C", self.anitalias, font_colr)
        # self.opt_C_plac = self.opt_C.get_rect(center = (self.opt_x, self.opt_y))
        # self.opt_C_cont.blit(self.opt_C, self.opt_C_plac)
        # self.ans_C = self.font_sty_ans.render(answers[2], self.anitalias, font_colr)
        # self.ans_C_plac = self.ans_C.get_rect(center = (self.ans_x, self.ans_y))
        # self.opt_C_cont.blit(self.ans_C, self.ans_C_plac)
        #     # Option D container
        # self.opt_D_state = False
        # self.opt_D_cont = pg.Surface((self.width, self.height))
        # self.opt_D_cont.fill(opt_colrs[3])
        # self.opt_D_cont_plac = self.opt_D_cont.get_rect(topleft = (527, 622))
        # self.opt_D = self.font_sty_opt.render("D", self.anitalias, font_colr)
        # self.opt_D_plac = self.opt_D.get_rect(center = (self.opt_x, self.opt_y))
        # self.opt_D_cont.blit(self.opt_D, self.opt_D_plac)
        # self.ans_D = self.font_sty_ans.render(answers[3], self.anitalias, font_colr)
        # self.ans_D_plac = self.ans_D.get_rect(center = (self.ans_x, self.ans_y))
        # self.opt_D_cont.blit(self.ans_D, self.ans_D_plac)



class AnswerMaker_B(pg.sprite.Sprite, SettingsAnswer):
        
        def update(self):
            self.cliked()
        
        def next_ans(self):
            self.kill()

        def check_own(self):
            #  Setting up the images and their placment
            correct_icon = pg.image.load("correct  image.png").convert_alpha()
            correct_icon_pla = correct_icon.get_rect(midleft = (461, int(self.height / 2)))
            wrong_icon = pg.image.load("wrong.png").convert_alpha()
            wrong_icon_pla = wrong_icon.get_rect(midleft = (461, int(self.height / 2)))


            if self.anss == self.correct_answer:
                class_answer_list[question_ans_num][1].image.blit(correct_icon, correct_icon_pla)
                class_answer_list[question_ans_num][0].image.set_alpha(127)
                class_answer_list[question_ans_num][0].image.blit(wrong_icon, wrong_icon_pla)
                class_answer_list[question_ans_num][2].image.set_alpha(127)
                class_answer_list[question_ans_num][2].image.blit(wrong_icon, wrong_icon_pla)
                class_answer_list[question_ans_num][3].image.set_alpha(127)
                class_answer_list[question_ans_num][3].image.blit(wrong_icon, wrong_icon_pla)
            else:
                class_answer_list[question_ans_num][1].image.blit(wrong_icon, wrong_icon_pla)
                if class_answer_list[question_ans_num][0].anss == self.correct_answer:
                    class_answer_list[question_ans_num][0].image.set_alpha(127)
                    class_answer_list[question_ans_num][0].image.blit(correct_icon, correct_icon_pla)
                else:
                    class_answer_list[question_ans_num][0].image.set_alpha(127)
                    class_answer_list[question_ans_num][0].image.blit(wrong_icon, wrong_icon_pla) 

                if class_answer_list[question_ans_num][2].anss == self.correct_answer:
                    class_answer_list[question_ans_num][2].image.set_alpha(127)
                    class_answer_list[question_ans_num][2].image.blit(correct_icon, correct_icon_pla)
                else:
                    class_answer_list[question_ans_num][2].image.set_alpha(127)
                    class_answer_list[question_ans_num][2].image.blit(wrong_icon, wrong_icon_pla) 

                if class_answer_list[question_ans_num][3].anss == self.correct_answer:
                    class_answer_list[question_ans_num][3].image.set_alpha(127)
                    class_answer_list[question_ans_num][3].image.blit(correct_icon, correct_icon_pla)
                else:
                    class_answer_list[question_ans_num][3].image.set_alpha(127)
                    class_answer_list[question_ans_num][3].image.blit(wrong_icon, wrong_icon_pla)

        def check_everyone(self):
            #  Setting up the images and their placment
            correct_icon = pg.image.load("correct  image.png").convert_alpha()
            correct_icon_pla = correct_icon.get_rect(midleft = (461, int(self.height / 2)))
            wrong_icon = pg.image.load("wrong.png").convert_alpha()
            wrong_icon_pla = wrong_icon.get_rect(midleft = (461, int(self.height / 2)))

            if self.anss == self.correct_answer:
                self.image.blit(correct_icon, correct_icon_pla)
                self.image.set_alpha(127)
            else:
                self.image.blit(wrong_icon, wrong_icon_pla)
                self.image.set_alpha(127)

        def cliked(self):
        # Getting the mouse position
            mouse_pos = pg.mouse.get_pos()

            if self.rect.collidepoint(mouse_pos):
                # print("Button B Hover")
                # self.opt_A_state = True
                # print(self.opt_A_state)
                # if pg.mouse.get_pressed()[0] and self.opt_B_state == False and self.opt_C_state == False and self.opt_D_state == False and self.opt_A_state == False:
                #     self.opt_B_state = True
                #     print("Ok B")
                if pg.mouse.get_pressed()[0] and button_states[0] == False and button_states[1] == False and button_states[2] == False and button_states[3] == False:
                    button_states[1] = True
                    self.check_own()
                    print("Ok B")

        def __init__(self, option, answers, correct_answer, cont_colors):
        # Calling spirit class
            super().__init__()
            SettingsAnswer.__init__(self)

            self.option = option
            # Answers and correct container
            self.anss = answers
            self.correct_answer = correct_answer
                # Option container
            self.image = pg.Surface((self.width, self.height))
            self.image.fill(cont_colors)
            self.rect = self.image.get_rect(topleft = (527, 470))

            self.opt_B = self.font_sty_opt.render(self.option, self.anitalias, self.font_colr)
            self.opt_B_plac = self.opt_B.get_rect(center = (self.opt_x, self.opt_y))
            self.image.blit(self.opt_B, self.opt_B_plac)

            self.ans_B = self.font_sty_ans.render(answers, self.anitalias, self.font_colr)
            self.ans_B_plac = self.ans_B.get_rect(center = (self.ans_x, self.ans_y))
            self.image.blit(self.ans_B, self.ans_B_plac)


class AnswerMaker_C(pg.sprite.Sprite, SettingsAnswer):
        
        def update(self):
            self.cliked()
        
        def next_ans(self):
            self.kill()


        def check_own(self):
            #  Setting up the images and their placment
            correct_icon = pg.image.load("correct  image.png").convert_alpha()
            correct_icon_pla = correct_icon.get_rect(midleft = (461, int(self.height / 2)))
            wrong_icon = pg.image.load("wrong.png").convert_alpha()
            wrong_icon_pla = wrong_icon.get_rect(midleft = (461, int(self.height / 2)))


            if self.anss == self.correct_answer:
                class_answer_list[question_ans_num][2].image.blit(correct_icon, correct_icon_pla)
                class_answer_list[question_ans_num][1].image.set_alpha(127)
                class_answer_list[question_ans_num][1].image.blit(wrong_icon, wrong_icon_pla)
                class_answer_list[question_ans_num][0].image.set_alpha(127)
                class_answer_list[question_ans_num][0].image.blit(wrong_icon, wrong_icon_pla)
                class_answer_list[question_ans_num][3].image.set_alpha(127)
                class_answer_list[question_ans_num][3].image.blit(wrong_icon, wrong_icon_pla)
            else:
                class_answer_list[question_ans_num][2].image.blit(wrong_icon, wrong_icon_pla)
                if class_answer_list[question_ans_num][1].anss == self.correct_answer:
                    class_answer_list[question_ans_num][1].image.set_alpha(127)
                    class_answer_list[question_ans_num][1].image.blit(correct_icon, correct_icon_pla)
                else:
                    class_answer_list[question_ans_num][1].image.set_alpha(127)
                    class_answer_list[question_ans_num][1].image.blit(wrong_icon, wrong_icon_pla) 

                if class_answer_list[question_ans_num][0].anss == self.correct_answer:
                    class_answer_list[question_ans_num][0].image.set_alpha(127)
                    class_answer_list[question_ans_num][0].image.blit(correct_icon, correct_icon_pla)
                else:
                    class_answer_list[question_ans_num][0].image.set_alpha(127)
                    class_answer_list[question_ans_num][0].image.blit(wrong_icon, wrong_icon_pla) 

                if class_answer_list[question_ans_num][3].anss == self.correct_answer:
                    class_answer_list[question_ans_num][3].image.set_alpha(127)
                    class_answer_list[question_ans_num][3].image.blit(correct_icon, correct_icon_pla)
                else:
                    class_answer_list[question_ans_num][3].image.set_alpha(127)
                    class_answer_list[question_ans_num][3].image.blit(wrong_icon, wrong_icon_pla)

        def check_everyone(self):
            #  Setting up the images and their placment
            correct_icon = pg.image.load("correct  image.png").convert_alpha()
            correct_icon_pla = correct_icon.get_rect(midleft = (461, int(self.height / 2)))
            wrong_icon = pg.image.load("wrong.png").convert_alpha()
            wrong_icon_pla = wrong_icon.get_rect(midleft = (461, int(self.height / 2)))

            if self.anss == self.correct_answer:
                self.image.blit(correct_icon, correct_icon_pla)
                self.image.set_alpha(127)
            else:
                self.image.blit(wrong_icon, wrong_icon_pla)
                self.image.set_alpha(127)


        def cliked(self):
        # Getting the mouse position
            mouse_pos = pg.mouse.get_pos()

            if self.rect.collidepoint(mouse_pos):
                # print("Button C Hover")
                if pg.mouse.get_pressed()[0] and button_states[0] == False and button_states[1] == False and button_states[2] == False and button_states[3] == False:
                    button_states[2] = True
                    self.check_own()
                    print("Ok C")

        def __init__(self, option, answers, correct_answer, cont_colors):
        # Calling spirit class
            super().__init__()
            SettingsAnswer.__init__(self)

            self.option = option
            # Answers and correct container
            self.anss = answers
            self.correct_answer = correct_answer
                # Option container
            self.image = pg.Surface((self.width, self.height))
            self.image.fill(cont_colors)
            self.rect = self.image.get_rect(topleft = (527, 546))

            self.opt_C = self.font_sty_opt.render(self.option, self.anitalias, self.font_colr)
            self.opt_C_plac = self.opt_C.get_rect(center = (self.opt_x, self.opt_y))
            self.image.blit(self.opt_C, self.opt_C_plac)

            self.ans_C = self.font_sty_ans.render(answers, self.anitalias, self.font_colr)
            self.ans_C_plac = self.ans_C.get_rect(center = (self.ans_x, self.ans_y))
            self.image.blit(self.ans_C, self.ans_C_plac)

class AnswerMaker_D(pg.sprite.Sprite, SettingsAnswer):
        
        def update(self):
            self.cliked()

        def next_ans(self):
            self.kill()

            
        def check_own(self):
            #  Setting up the images and their placment
            correct_icon = pg.image.load("correct  image.png").convert_alpha()
            correct_icon_pla = correct_icon.get_rect(midleft = (461, int(self.height / 2)))
            wrong_icon = pg.image.load("wrong.png").convert_alpha()
            wrong_icon_pla = wrong_icon.get_rect(midleft = (461, int(self.height / 2)))

            if self.anss == self.correct_answer:
                class_answer_list[question_ans_num][3].image.blit(correct_icon, correct_icon_pla)
                class_answer_list[question_ans_num][1].image.set_alpha(127)
                class_answer_list[question_ans_num][1].image.blit(wrong_icon, wrong_icon_pla)
                class_answer_list[question_ans_num][1].image.blit(wrong_icon, wrong_icon_pla)
                class_answer_list[question_ans_num][2].image.set_alpha(127)
                class_answer_list[question_ans_num][2].image.blit(wrong_icon, wrong_icon_pla)
                class_answer_list[question_ans_num][0].image.set_alpha(127)
                class_answer_list[question_ans_num][0].image.blit(wrong_icon, wrong_icon_pla)
            else:
                class_answer_list[question_ans_num][3].image.blit(wrong_icon, wrong_icon_pla)
                if class_answer_list[question_ans_num][1].anss == self.correct_answer:
                    class_answer_list[question_ans_num][1].image.set_alpha(127)
                    class_answer_list[question_ans_num][1].image.blit(correct_icon, correct_icon_pla)
                else:
                    class_answer_list[question_ans_num][1].image.set_alpha(127)
                    class_answer_list[question_ans_num][1].image.blit(wrong_icon, wrong_icon_pla) 

                if class_answer_list[question_ans_num][2].anss == self.correct_answer:
                    class_answer_list[question_ans_num][2].image.set_alpha(127)
                    class_answer_list[question_ans_num][2].image.blit(correct_icon, correct_icon_pla)
                else:
                    class_answer_list[question_ans_num][2].image.set_alpha(127)
                    class_answer_list[question_ans_num][2].image.blit(wrong_icon, wrong_icon_pla) 

                if class_answer_list[question_ans_num][0].anss == self.correct_answer:
                    class_answer_list[question_ans_num][0].image.set_alpha(127)
                    class_answer_list[question_ans_num][0].image.blit(correct_icon, correct_icon_pla)
                else:
                    class_answer_list[question_ans_num][0].image.set_alpha(127)
                    class_answer_list[question_ans_num][0].image.blit(wrong_icon, wrong_icon_pla)


        def cliked(self):
        # Getting the mouse position
            mouse_pos = pg.mouse.get_pos()

            if self.rect.collidepoint(mouse_pos):
                # print("Button D Hover")
                if pg.mouse.get_pressed()[0] and button_states[0] == False and button_states[1] == False and button_states[2] == False and button_states[3] == False:
                    button_states[3] = True
                    self.check_own()
                    print("Ok D")
            

        def __init__(self, option, answers, correct_answer, cont_colors):
        # Calling spirit class
            super().__init__()
            SettingsAnswer.__init__(self)

            self.option = option
            # Answers and correct container
            self.anss = answers
            self.correct_answer = correct_answer
                # Option container
            self.image = pg.Surface((self.width, self.height))
            self.image.fill(cont_colors)
            self.rect = self.image.get_rect(topleft = (527, 622))

            self.opt_D = self.font_sty_opt.render(self.option, self.anitalias, self.font_colr)
            self.opt_D_plac = self.opt_D.get_rect(center = (self.opt_x, self.opt_y))
            self.image.blit(self.opt_D, self.opt_D_plac)

            self.ans_D = self.font_sty_ans.render(answers, self.anitalias, self.font_colr)
            self.ans_D_plac = self.ans_D.get_rect(center = (self.ans_x, self.ans_y))
            self.image.blit(self.ans_D, self.ans_D_plac)

# Creating the questions
with open("question_paper.csv") as questions:
    read_questions = csv.reader(questions)
    questions_list = list(read_questions)

# Spirits for the question and answers
question_spirit = pg.sprite.GroupSingle()
answers_spirit = pg.sprite.Group()

# Question makers spirit version
num_questions_answers = len(questions_list)
class_question_list = []
class_answer_list = []
for Q_num in range(1, num_questions_answers):

    # Choosing a random colour for the options
    random.shuffle(opt_colr_list)

    # Making instance of questions
    class_question_list.append(QuestionMaker(questions_list[Q_num][0], questions_list[Q_num][1]))

    # Making of answers with spirits
    class_answer_list.append([AnswerMaker_A("A", questions_list[Q_num][2], questions_list[Q_num][6], opt_colr_list[0]), 
                              AnswerMaker_B("B", questions_list[Q_num][3], questions_list[Q_num][6], opt_colr_list[1]),
                              AnswerMaker_C("C", questions_list[Q_num][4], questions_list[Q_num][6], opt_colr_list[2]),
                              AnswerMaker_D("D", questions_list[Q_num][5], questions_list[Q_num][6], opt_colr_list[3])
                              ])

question_ans_num = 0
# Adding the questions and answers to spirits
question_spirit.add(class_question_list[question_ans_num])
answers_spirit.add(class_answer_list[question_ans_num])


