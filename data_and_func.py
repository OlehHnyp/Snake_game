import pygame

WHITE = (255, 255, 255)
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
free_x = screen_width % (BLOCK_SIZE+INTERVAL)
free_y = screen_height % (BLOCK_SIZE+INTERVAL)
header_margin = 3*(BLOCK_SIZE+INTERVAL)
question_margin = header_margin + free_y
block_columns = screen_width // (BLOCK_SIZE+INTERVAL)
block_rows = (screen_height-header_margin) // (BLOCK_SIZE+INTERVAL)

print(screen_width)



def add_block(screen, color, column, row):
    pygame.draw.rect(screen, color,
                     [free_x/2 +(BLOCK_SIZE+INTERVAL) * column,
                      (BLOCK_SIZE+INTERVAL) * row + header_margin + free_y,
                      BLOCK_SIZE,
                      BLOCK_SIZE]
                      )


def draw_margins(screen, color):
    pygame.draw.rect(screen, color, (0, 0, screen_width, question_margin))
    pygame.draw.rect(screen, color, (0, question_margin, free_x/2, screen_height-question_margin))
    pygame.draw.rect(screen, color, (screen_width - free_x/2, question_margin, free_x/2, screen_height-question_margin))

class Blocks():

    def __init__(self, column, row, n=1):
        self.c = column
        self.r = row
        self.n = n

snake = [Blocks(8, 9), Blocks(9, 9)]
move_x = 1
move_y = 0

