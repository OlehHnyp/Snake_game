import pygame
import data_and_func as d



pygame.init()

screen = pygame.display.set_mode(d.screen_size)
pygame.display.set_caption(d.caption)



done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(d.WHITE)
    d.draw_margins(screen, d.SUPER_BLUE)

    for row in range(d.block_rows):
        for column in range(d.block_columns):
            color = d.BLUE
            if (row+column)%2 == 0:
                color = d.YELLOW
            d.add_block(screen, color, column, row)
    
    for block in d.snake:
        d.add_block(screen, d.RED, block.c, block.r)
    
    snake_head = d.snake[-1]
    new_head = d.Blocks(snake_head.c + d.move_x, snake_head.r + d.move_y)
    d.snake.append(new_head)
    d.snake.pop(0)
    print(d.snake)
    
    pygame.display.flip()
    d.clock.tick(2)


    

