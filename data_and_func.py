import pygame
import random
import copy
import sys


WHITE = (255, 255, 255)
VIOLET = (204,0,204)
YELLOW = (255, 255, 153)
BLUE = (204, 255, 229)
SUPER_BLUE = (51, 153, 255)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLOCK_SIZE = 35
INTERVAL = 2

pygame.init()


clock = pygame.time.Clock()
caption = "The SNAKE game"
screen_width = pygame.display.Info().current_w 
screen_height = pygame.display.Info().current_h 
screen_size = [screen_width, screen_height]
screen = pygame.display.set_mode(screen_size)
free_x = screen_width % (BLOCK_SIZE+INTERVAL)
free_y = screen_height % (BLOCK_SIZE+INTERVAL)
header_margin = 3*(BLOCK_SIZE+INTERVAL)
question_margin = header_margin + free_y
block_columns = screen_width // (BLOCK_SIZE+INTERVAL)
block_rows = (screen_height-header_margin) // (BLOCK_SIZE+INTERVAL)
background_block_columns = screen_width // (BLOCK_SIZE+INTERVAL)
background_block_rows = (screen_height) // (BLOCK_SIZE+INTERVAL)
answer_courier =  pygame.font.SysFont('courier', 20)
r_column = random.randint(0, block_columns-2)
r_row = random.randint(0, block_rows-3)
question_courier = pygame.font.SysFont('palatinolinotype', 45, bold=True)
final_score_courier = pygame.font.SysFont('courier', 45, bold=True)
move_sound = pygame.mixer.Sound(r'C:\Users\User\Downloads\377017__elmasmalo1__notification-pop.wav')
right_sound = pygame.mixer.Sound(r'C:\Users\User\Downloads\right.wav')
wrong_sound = pygame.mixer.Sound(r'C:\Users\User\Downloads\wrong.wav')
next_level_sound = pygame.mixer.Sound(r'C:\Users\User\Downloads\next_level2.wav')
crash_sound = pygame.mixer.Sound(r'C:\Users\User\Downloads\crash.wav')
selfcrash_sound = pygame.mixer.Sound(r'C:\Users\User\Downloads\selfcrash.wav')
game_over_sound = pygame.mixer.Sound(r'C:\Users\User\Downloads\game_over.wav')
menu_music = pygame.mixer.Sound(r'C:\Users\User\Downloads\172707__axtoncrolley__nodens-field-song.mp3')
pause_music = pygame.mixer.Sound(r'C:\Users\User\Downloads\265191__b-lamerichs__short-loops-26-02-2015-3.mp3')
borders = 1
speed = None

menu_music.set_volume(0.3)
pause_music.set_volume(0.3)
move_sound.set_volume(0.08)
next_level_sound.set_volume(0.4)
right_sound.set_volume(0.4)

                             

def add_block(color, column, row):
    pygame.draw.rect(screen, color,
                     [free_x/2 +(BLOCK_SIZE+INTERVAL) * column,
                      (BLOCK_SIZE+INTERVAL) * row + header_margin + free_y,
                      BLOCK_SIZE,
                      BLOCK_SIZE]
                      )

def draw_background(color, column, row):
    pygame.draw.rect(screen, color,
                     [(BLOCK_SIZE+INTERVAL) * column,
                      (BLOCK_SIZE+INTERVAL) * row,
                      BLOCK_SIZE,
                      BLOCK_SIZE]
                      )    


def draw_margins(color):
    pygame.draw.rect(screen, color, (0, 0, screen_width, question_margin))
    pygame.draw.rect(screen, color, (0, question_margin, free_x/2, screen_height-question_margin))
    pygame.draw.rect(screen, color, (screen_width - free_x/2+1, question_margin, free_x/2, screen_height-question_margin))

def set_default_snake(x, n=0):
    snake = []
    for i in range(len(x)+n):
        snake.append(Blocks(0, block_rows-1))
    return snake

def set_no_borders(new_head):
    if new_head.r == block_rows or new_head.r < 0:
        new_head.r = abs(block_rows - abs(new_head.r))
    elif new_head.c == block_columns or new_head.c < 0:
        new_head.c = abs(block_columns - abs(new_head.c))
    return new_head

def set_borders(value, mode):
    global borders
    borders = mode

def set_speed(value, mode):
    global speed
    speed = mode



class Blocks:

    def __init__(self, column, row):
        self.c = column
        self.r = row

    def isinside(self):
        return -1<self.c<block_columns and -1<self.r<block_rows
    
    def __eq__(self, other):
        return self.c==other.c and self.r==other.r

class AnswerBlocks:

    color = VIOLET
    def __init__(self, answer, point, score, life=0, column=r_column, row=r_row):
        self.c = column
        self.r = row
        self.answer = answer
        self.point = point
        self.score = score
        self.life = life
        self.len = len


    def snake_head_in_answer(self, snake):
        return -1<(snake.c-self.c)<2 and -1<(snake.r-self.r)<2

    # def snake_in_answer(self, snake):
    #     for el in snake:
    #         if self.snake_head_in_answer(el):
    #             return True
    #     return False

    
    

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

        text = answer_courier.render(self.answer[0], 0, WHITE)
        screen.blit(text,(x, y + interval1))
                    
    def __eq__(self, other):
        return abs(self.c- other.c)<3 and abs(self.r- other.r)<3


class Questions:
    
    def __init__(self, point, question):
        self.point = point
        self.question = question

    def add_question(self):
        interval1 = 25
        interval2 = 35

        if len(self.question)==2:
            interval1 = 5
            text1 = question_courier.render(self.question[1], 0, WHITE)
            screen.blit(text1,(20, 10 + interval2))

        text = question_courier.render(self.question[0], 0, WHITE)
        screen.blit(text,(20, 0 + interval1))



snake = [Blocks(0, block_rows-1),
         Blocks(0, block_rows-1), 
         Blocks(0, block_rows-1), 
         (0, block_rows-1), 
         Blocks(1, block_rows-1)]
default_snake = copy.deepcopy(snake)
move_x = reserve_move_x = 1
move_y = reserve_move_y = 0
food = Blocks(r_column, r_row)





