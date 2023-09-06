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
LINE_COLOR = (26, 83, 92)

# Colours for the options
RED_COLOUR = (235, 62, 62)
ORANGE_COLOR = (255, 184, 0)
GREEN_COLOUR = (39, 239, 83)
BLUE_COLOUR = (20, 153, 228)
opt_colr_list = [RED_COLOUR, ORANGE_COLOR, GREEN_COLOUR, BLUE_COLOUR]

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
answer_check = []


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
        button_pressed = self.cliked()
        return button_pressed

    def next_ans(self):
        self.kill()

    def check_own(self):
        #  Setting up the images and their placment
        correct_icon = pg.image.load("correct  image.png").convert_alpha()
        correct_icon_pla = correct_icon.get_rect(midleft = (461, int(self.height / 2)))
        wrong_icon = pg.image.load("wrong.png").convert_alpha()
        wrong_icon_pla = wrong_icon.get_rect(midleft = (461, int(self.height / 2)))

        if self.anss == self.correct_answer:
            if len(answer_check) <= actual_que_num:
                answer_check.append(True)
            else:
                pass

            class_answer_list[question_ans_num][0].image.blit(correct_icon, correct_icon_pla)
            class_answer_list[question_ans_num][1].image.set_alpha(127)
            class_answer_list[question_ans_num][1].image.blit(wrong_icon, wrong_icon_pla)
            class_answer_list[question_ans_num][2].image.set_alpha(127)
            class_answer_list[question_ans_num][2].image.blit(wrong_icon, wrong_icon_pla)
            class_answer_list[question_ans_num][3].image.set_alpha(127)
            class_answer_list[question_ans_num][3].image.blit(wrong_icon, wrong_icon_pla)

        else:
            class_answer_list[question_ans_num][0].image.blit(wrong_icon, wrong_icon_pla)
            if len(answer_check) <= actual_que_num:
                answer_check.append(False)
            else:
                pass

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

                

    def cliked(self):
    # Getting the mouse position
        mouse_pos = pg.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0] and button_states[0] == False and button_states[1] == False and button_states[2] == False and button_states[3] == False:
                button_states[0] = True
                self.check_own()
                return True

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


class AnswerMaker_B(pg.sprite.Sprite, SettingsAnswer):
        
        def update(self):
            button_pressed = self.cliked()
            return button_pressed
        

        def next_ans(self):
            self.kill()


        def check_own(self):
            #  Setting up the images and their placment
            correct_icon = pg.image.load("correct  image.png").convert_alpha()
            correct_icon_pla = correct_icon.get_rect(midleft = (461, int(self.height / 2)))
            wrong_icon = pg.image.load("wrong.png").convert_alpha()
            wrong_icon_pla = wrong_icon.get_rect(midleft = (461, int(self.height / 2)))


            if self.anss == self.correct_answer:
                if len(answer_check) <= actual_que_num:
                    answer_check.append(True)
                else:
                    pass

                class_answer_list[question_ans_num][1].image.blit(correct_icon, correct_icon_pla)
                class_answer_list[question_ans_num][0].image.set_alpha(127)
                class_answer_list[question_ans_num][0].image.blit(wrong_icon, wrong_icon_pla)
                class_answer_list[question_ans_num][2].image.set_alpha(127)
                class_answer_list[question_ans_num][2].image.blit(wrong_icon, wrong_icon_pla)
                class_answer_list[question_ans_num][3].image.set_alpha(127)
                class_answer_list[question_ans_num][3].image.blit(wrong_icon, wrong_icon_pla)
            else:
                class_answer_list[question_ans_num][1].image.blit(wrong_icon, wrong_icon_pla)
                if len(answer_check) <= actual_que_num:
                    answer_check.append(False)
                else:
                    pass

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
                if pg.mouse.get_pressed()[0] and button_states[0] == False and button_states[1] == False and button_states[2] == False and button_states[3] == False:
                    button_states[1] = True
                    self.check_own()
                    return True


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
            button_pressed = self.cliked()
            return button_pressed
        

        def next_ans(self):
            self.kill()

        def check_own(self):
            #  Setting up the images and their placment
            correct_icon = pg.image.load("correct  image.png").convert_alpha()
            correct_icon_pla = correct_icon.get_rect(midleft = (461, int(self.height / 2)))
            wrong_icon = pg.image.load("wrong.png").convert_alpha()
            wrong_icon_pla = wrong_icon.get_rect(midleft = (461, int(self.height / 2)))


            if self.anss == self.correct_answer:
                if len(answer_check) <= actual_que_num:
                    answer_check.append(True)
                else:
                    pass

                class_answer_list[question_ans_num][2].image.blit(correct_icon, correct_icon_pla)
                class_answer_list[question_ans_num][1].image.set_alpha(127)
                class_answer_list[question_ans_num][1].image.blit(wrong_icon, wrong_icon_pla)
                class_answer_list[question_ans_num][0].image.set_alpha(127)
                class_answer_list[question_ans_num][0].image.blit(wrong_icon, wrong_icon_pla)
                class_answer_list[question_ans_num][3].image.set_alpha(127)
                class_answer_list[question_ans_num][3].image.blit(wrong_icon, wrong_icon_pla)
            else:
                class_answer_list[question_ans_num][2].image.blit(wrong_icon, wrong_icon_pla)
                if len(answer_check) <= actual_que_num:
                    answer_check.append(False)
                else:
                    pass



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


        def cliked(self):
        # Getting the mouse position
            mouse_pos = pg.mouse.get_pos()

            if self.rect.collidepoint(mouse_pos):
                if pg.mouse.get_pressed()[0] and button_states[0] == False and button_states[1] == False and button_states[2] == False and button_states[3] == False:
                    button_states[2] = True
                    self.check_own()
                    return True


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
            button_pressed = self.cliked()
            return button_pressed


        def next_ans(self):
            self.kill()

            
        def check_own(self):
            #  Setting up the images and their placment
            correct_icon = pg.image.load("correct  image.png").convert_alpha()
            correct_icon_pla = correct_icon.get_rect(midleft = (461, int(self.height / 2)))
            wrong_icon = pg.image.load("wrong.png").convert_alpha()
            wrong_icon_pla = wrong_icon.get_rect(midleft = (461, int(self.height / 2)))

            if self.anss == self.correct_answer:
                if len(answer_check) <= actual_que_num:
                    answer_check.append(True)
                    print()
                else:
                    pass


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
                if len(answer_check) <= actual_que_num:
                    answer_check.append(False)
                else:
                    pass

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
                if pg.mouse.get_pressed()[0] and button_states[0] == False and button_states[1] == False and button_states[2] == False and button_states[3] == False:
                    button_states[3] = True
                    self.check_own()
                    return True
            

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
actual_que_num = len(questions_list) - 2
class_question_list = []
class_answer_list = []
for Q_num in range(1, num_questions_answers):

    # Choosing a random colour for the options
    random.shuffle(opt_colr_list)

    # Making instance of questions
    class_question_list.append(QuestionMaker(f"Q{Q_num}", questions_list[Q_num][1]))

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


class Divider(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((1, 310))
        self.image.fill(LINE_COLOR)
        self.rect = self.image.get_rect(topleft = (521, 388))


divider_line = Divider()
line_spirit = pg.sprite.Group()
line_spirit.add(divider_line)

