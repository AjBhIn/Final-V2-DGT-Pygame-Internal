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

# Creating a class for question
class QuestionMaker(pg.sprite.Sprite):

    def __init__(self, question_num, question,  font_style = JURA_BOLD, font_size = QUESTION_SIZE, q_contain_colr = (247, 255, 247), q_num_col = QUESTION_NUM_COLOUR, q_col = QUESTION_COLOUR):
        # Starting / Initialising pygame/ starting pygame
        pg.init()
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
        self.question_container_x = int(wt.display_board.surface.get_width()/4)
        self.question_container_y = int(wt.display_board.surface.get_height()/2)
        self.image = pg.Surface((self.width, self.height))
        self.rect = self.image.get_rect(center = (self.question_container_x, self.question_container_y))
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

    def next_question(self):
        self.kill()


# Settings for the font options and answers
opt_font_size = 28
opt_font_colr = (255, 255, 255)
JURA_MEDIUM = "Jura-Medium.ttf"

# Creating a class for answers
class AnswerMaker(pg.sprite.Sprite):
    # def opt_render(self, display):
    #     display.blit(self.opt_A_cont, self.opt_A_cont_plac)
    #     display.blit(self.opt_B_cont, self.opt_B_cont_plac)
    #     display.blit(self.opt_C_cont, self.opt_C_cont_plac)
    #     display.blit(self.opt_D_cont, self.opt_D_cont_plac)

    #     # Storing the value of the clicked button
    #     clikced_button = self.clicked_opt()

    #     # Returing the clicked button value to indicate the start of next question
    #     return clikced_button

    # # Checks if any button is clicked
    # def clicked_opt(self):
    #     # Getting the mouse position
    #     mouse_pos = pg.mouse.get_pos()

    #     # Checks if mouse is clicked on option A
    #     if self.opt_A_cont_plac.collidepoint(mouse_pos):
    #         if pg.mouse.get_pressed()[0]:
    #             self.opt_A_state = True
    #         else:
    #             if self.opt_A_state:
    #                 self.check(1)
    #                 self.opt_A_state = False
    #                 return True
    #     # Checks if mouse is clicked on option B
    #     if self.opt_B_cont_plac.collidepoint(mouse_pos):
    #         if pg.mouse.get_pressed()[0]:
    #             self.opt_B_state = True
    #         else:
    #             if self.opt_B_state:
    #                 self.check(2)
    #                 self.opt_B_state = False
    #                 return True
    #     # Checks if mouse is clicked on option C
    #     if self.opt_C_cont_plac.collidepoint(mouse_pos):
    #         if pg.mouse.get_pressed()[0]:
    #             self.opt_C_state = True
    #         else:
    #             if self.opt_C_state:
    #                 self.check(3)
    #                 self.opt_C_state = False
    #                 return True
    #     # Checks if mouse is clicked on option D
    #     if self.opt_D_cont_plac.collidepoint(mouse_pos):
    #         if pg.mouse.get_pressed()[0]:
    #             self.opt_D_state = True
    #         else:
    #             if self.opt_D_state:
    #                 self.check(4)
    #                 self.opt_D_state = False
    #                 return True


#     def check(self, button_clicked):
#         # Setting up the images and their placment
#         correct_icon = pg.image.load("correct  image.png").convert_alpha()
#         correct_icon_pla = correct_icon.get_rect(midleft = (461, int(self.height / 2)))
#         wrong_icon = pg.image.load("wrong.png").convert_alpha()
#         wrong_icon_pla = wrong_icon.get_rect(midleft = (461, int(self.height / 2)))

#         # Checking where to put the correct and wrong icon

#             # Checks if Option A is correct or wrong
#         if self.correct_ans == self.anss[0]:
#             self.opt_A_cont.blit(correct_icon, correct_icon_pla)
#             # This statment makes the container more brighter or less brighter if it is right or wrong so it is easier t see which one the user chose and which they did not
#             if button_clicked == 1:
#                 pass
#             else:
#                 self.opt_A_cont.set_alpha(127)
#         else:
#             self.opt_A_cont.blit(wrong_icon, wrong_icon_pla)
#             if button_clicked == 1:
#                 pass
#             else:
#                 self.opt_A_cont.set_alpha(127)

#             # Checks if Option B is correct or wrong
#         if self.correct_ans == self.anss[1]:
#             self.opt_B_cont.blit(correct_icon, correct_icon_pla)
#             if button_clicked == 2:
#                 pass
#             else:
#                 self.opt_B_cont.set_alpha(127)
#         else:
#             self.opt_B_cont.blit(wrong_icon, wrong_icon_pla)
#             if button_clicked == 2:
#                 pass
#             else:
#                 self.opt_B_cont.set_alpha(127)

#             # Checks if Option C is correct or wrong
#         if self.correct_ans == self.anss[2]:
#             self.opt_C_cont.blit(correct_icon, correct_icon_pla)
#             if button_clicked == 3:
#                 pass
#             else:
#                 self.opt_C_cont.set_alpha(127)
#         else:
#             self.opt_C_cont.blit(wrong_icon, wrong_icon_pla)
#             if button_clicked == 3:
#                 pass
#             else:
#                 self.opt_C_cont.set_alpha(127)

#             # Checks if Option D is correct or wrong
#         if self.correct_ans == self.anss[3]:
#             self.opt_D_cont.blit(correct_icon, correct_icon_pla)
#             if button_clicked == 4:
#                 pass
#             else:
#                 self.opt_D_cont.set_alpha(127)
#         else:
#             self.opt_D_cont.blit(wrong_icon, wrong_icon_pla)
#             if button_clicked == 4:
#                 pass
#             else:
#                 self.opt_D_cont.set_alpha(127)

        
    def __init__(self, option, answers, correct_answer, cont_placment, cont_colors, opt_font = JURA_BOLD, opt_size = opt_font_size, ans_font = JURA_MEDIUM, font_colr = opt_font_colr):
        # Calling spirit class
        super().__init__()
        self.anss = answers
        # Setting the font style for the options
        self.font_sty_opt = pg.font.Font(opt_font, opt_size)
        self.font_sty_ans = pg.font.Font(ans_font, opt_size)
        self.anitalias = True

        # Making the answer container / settings for it
        self.width = 510
        self.height = 70
        self.opt_y = int(self.height / 2)
        self.opt_x = 25
        self.ans_x = int(self.width / 2)
        self.ans_y = int(self.height / 2)
            # Option A container
        self.opt_A_state = False
        self.image = pg.Surface((self.width, self.height))
        self.image.fill(cont_colors)
        self.rect = self.image.get_rect(topleft = cont_placment)

        self.opt_A = self.font_sty_opt.render(option, self.anitalias, font_colr)
        self.opt_A_plac = self.opt_A.get_rect(center = (self.opt_x, self.opt_y))
        self.image.blit(self.opt_A, self.opt_A_plac)

        self.ans_A = self.font_sty_ans.render(answers, self.anitalias, font_colr)
        self.ans_A_plac = self.ans_A.get_rect(center = (self.ans_x, self.ans_y))
        self.image.blit(self.ans_A, self.ans_A_plac)

    def next_ans(self):
        self.kill()
        #     # Option B container
        # self.opt_B_state = False
        # self.opt_B_cont = pg.Surface((self.width, self.height))
        # self.opt_B_cont.fill(opt_colrs[1])
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


# # Creatings the answers for the questions
# Q1_Ans = AnswerMaker(["P = m/v", "F = ma", "v = d/t", "P = mv"], "P = mv")
# Q2_Ans = AnswerMaker(["P = mdd/v", "F = ma", "v = dddd/t", "P = mv"], "F = ma")

# Anss_list = [Q1_Ans, Q2_Ans]

# Creating the questions
with open("question_paper.csv") as questions:
    read_questions = csv.reader(questions)
    questions_list = list(read_questions)

# Spirits for the question and answers
question_spirit = pg.sprite.Group()
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
    class_answer_list.append([AnswerMaker("A", questions_list[Q_num][2], questions_list[Q_num][6], (527, 394), opt_colr_list[0]), 
                              AnswerMaker("B", questions_list[Q_num][3], questions_list[Q_num][6], (527, 470), opt_colr_list[1]),
                              AnswerMaker("C", questions_list[Q_num][4], questions_list[Q_num][6], (527, 546), opt_colr_list[2]),
                              AnswerMaker("D", questions_list[Q_num][5], questions_list[Q_num][6], (527, 622), opt_colr_list[3])
                              ])

# Adding the questions and answers to spirits
question_spirit.add(class_question_list[0])
answers_spirit.add(class_answer_list[0])
