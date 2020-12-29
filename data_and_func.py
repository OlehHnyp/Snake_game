import pygame
import random
import pprint


WHITE = (255, 255, 255)
VIOLET = (138,43,226)
YELLOW = (255, 255, 102)
BLUE = (102, 178, 255)
SUPER_BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLOCK_SIZE = 35
INTERVAL = 2

pygame.init()


clock = pygame.time.Clock()
caption = "The SNAKE game"
screen_width = pygame.display.Info().current_w -100
screen_height = pygame.display.Info().current_h -100
screen_size = [screen_width, screen_height]
screen = pygame.display.set_mode(screen_size)
free_x = screen_width % (BLOCK_SIZE+INTERVAL)
free_y = screen_height % (BLOCK_SIZE+INTERVAL)
header_margin = 3*(BLOCK_SIZE+INTERVAL)
question_margin = header_margin + free_y
block_columns = screen_width // (BLOCK_SIZE+INTERVAL)
block_rows = (screen_height-header_margin) // (BLOCK_SIZE+INTERVAL)
answer_courier =  pygame.font.SysFont('courier', 20)
r_column = random.randint(0, block_columns-2)
r_row = random.randint(0, block_rows-2)
question_courier = pygame.font.SysFont('courier', 45, bold=True)


print(print(block_rows))


                             


def add_block(color, column, row):
    pygame.draw.rect(screen, color,
                     [free_x/2 +(BLOCK_SIZE+INTERVAL) * column,
                      (BLOCK_SIZE+INTERVAL) * row + header_margin + free_y,
                      BLOCK_SIZE,
                      BLOCK_SIZE]
                      )


def draw_margins(color):
    pygame.draw.rect(screen, color, (0, 0, screen_width, question_margin))
    pygame.draw.rect(screen, color, (0, question_margin, free_x/2, screen_height-question_margin))
    pygame.draw.rect(screen, color, (screen_width - free_x/2, question_margin, free_x/2, screen_height-question_margin))

class Blocks:

    def __init__(self, column, row):
        self.c = column
        self.r = row

    def isinside(self):
        return -1<self.c<block_columns and -1<self.r<block_rows
    
    def __eq__(self, other):
        return self.c==other.c and self.r==other.r

class AnswerBlocks(Blocks):

    color = VIOLET
    def __init__(self, answer, column=r_column, row=r_row):
        self.c = column
        self.r = row
        self.answer = answer


    def snake_head_in_answer(self, snake):
        return -1<(snake.c-self.c)<2 and -1<(snake.r-self.r)<2

    def snake_in_answer(self, snake):
        for el in snake:
            if self.snake_head_in_answer(el):
                return True
        return False

    
    

    def add_answers(self):
        x = free_x/2 +(BLOCK_SIZE+INTERVAL) * self.c
        y = (BLOCK_SIZE+INTERVAL) * self.r + header_margin + free_y

        pygame.draw.rect(screen, self.color, [x, 
                                        y,
                                        BLOCK_SIZE*2 + INTERVAL,
                                        BLOCK_SIZE*2 + INTERVAL]
                        )
        interval1 = 20
        interval2 = 35
        if len(self.answer)==2:
            interval1 = 5
            text1 = answer_courier.render(self.answer[1], 0, WHITE)
            screen.blit(text1,(x, y + interval2))
            print('1')

        text = answer_courier.render(self.answer[0], 0, WHITE)
        screen.blit(text,(x, y + interval1))
                    
    def __eq__(self, other):
        return abs(self.c- other.c)<2 and abs(self.r- other.r)<2


class Questions:
    
    def __init__(self, point, question, answers=None):
        self.point = point
        self.question = question
        self.answers = answers

    def add_question(self):
        interval1 = 25
        interval2 = 35

        if len(self.question)==2:
            interval1 = 5
            text1 = question_courier.render(self.question[1], 0, WHITE)
            screen.blit(text1,(20, 10 + interval2))

        text = question_courier.render(self.question[0], 0, WHITE)
        screen.blit(text,(20, 0 + interval1))



snake = [Blocks(0, 9), Blocks(0, 8), Blocks(0, 7), Blocks(0, 6), Blocks(0, 5)]
move_x = reserve_move_x = 1
move_y = reserve_move_y = 0



answers1 = [AnswerBlocks(['True']),
            AnswerBlocks(['False']),
            AnswerBlocks(['Yes']),
            AnswerBlocks(['Yes']),
            AnswerBlocks(['Yes']),
            AnswerBlocks(['Yes']),
            AnswerBlocks(['Yes']),
            AnswerBlocks(['Yes']),
            AnswerBlocks(['Yes']),
            AnswerBlocks(['Yes']),
            AnswerBlocks(['Yes']),
            AnswerBlocks(['Yes']),
            AnswerBlocks(['Yes']),
            AnswerBlocks(['Yes']),
            AnswerBlocks(['Yes']),
            AnswerBlocks(['Lie'])
            ]

question1 = Questions(1,["Eat all boolean values", "lkasjfklsjgl"])



answers2 = [AnswerBlocks(['list']),
            AnswerBlocks(['float']),
            AnswerBlocks(['int']),
            AnswerBlocks(['str']),
            AnswerBlocks(['set']),
            ]

question2 = Questions(1,["Eat all mutable types"])


questions = [question1, question2]
answers = [answers1, answers2]
q_a_list_zip = list(zip(questions, answers))