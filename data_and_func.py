import pygame
import random

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


print(print(block_rows))

def add_answers(column, row, answer):
    x = free_x/2 +(BLOCK_SIZE+INTERVAL) * column
    y = (BLOCK_SIZE+INTERVAL) * row + header_margin + free_y

    pygame.draw.rect(screen, VIOLET, [x, 
                                      y,
                                      BLOCK_SIZE*2 + INTERVAL,
                                      BLOCK_SIZE*2 + INTERVAL]
                      )
    interval1 = 20
    interval2 = 35
    if len(answer)==2:
        interval1 = 5
        text1 = answer_courier.render(answer[1], 0, WHITE)
        screen.blit(text1,(x, y + interval2))
        print('1')

    text = answer_courier.render(answer[0], 0, WHITE)
    screen.blit(text,(x, y + interval1))
                             


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

class Blocks():

    def __init__(self, column, row):
        self.c = column
        self.r = row

    def isinside(self):
        return -1<self.c<block_columns and -1<self.r<block_rows
    
    def __eq__(self, other):
        return self.c==other.c and self.r==other.r

class AnswerBlocks(Blocks):
    def __init__(self, column, row, answer,):
        self.c = column
        self.r = row
        self.answer = answer


    def snake_in_answer(self,snake):
        return -1<(snake.c-self.c)<2 and -1<(snake.r-self.r)<2
                    


snake = [Blocks(0, 9), Blocks(0, 8), Blocks(0, 7), Blocks(0, 6), Blocks(0, 5)]
move_x = reserve_move_x = 1
move_y = reserve_move_y = 0

question1 = "Eat all boolean values"

answers1 = [AnswerBlocks(2, 3, ['True']),
            AnswerBlocks(10,5, ['False']),
            # AnswerBlocks(15, 15, ['Lie']),
            AnswerBlocks(4, 5, ['Yes']),
            AnswerBlocks(15,10, ['Lie'])
            ]

