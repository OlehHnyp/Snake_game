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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and d.move_y != 1:
                d.reserve_move_x = 0
                d.reserve_move_y = -1
            elif event.key == pygame.K_DOWN and d.move_y != -1:
                d.reserve_move_x = 0
                d.reserve_move_y = 1
            elif event.key == pygame.K_LEFT and d.move_x != 1:
                d.reserve_move_x = -1
                d.reserve_move_y = 0
            elif event.key == pygame.K_RIGHT and d.move_x != -1:
                d.reserve_move_x = 1
                d.reserve_move_y = 0
    
    



    screen.fill(d.WHITE)
    d.draw_margins(d.SUPER_BLUE)
    snake_head = d.snake[-1]
    
    

    for row in range(d.block_rows):
        for column in range(d.block_columns):
            color = d.BLUE
            if (row+column)%2 == 0:
                color = d.YELLOW
            d.add_block(color, column, row)
    for block in d.snake:
        d.add_block(d.RED, block.c, block.r)


    for el in d.answers1:
        d.add_answers(el.c, el.r, el.answer)

    d.move_x = d.reserve_move_x
    d.move_y = d.reserve_move_y
    
    new_head = d.Blocks(snake_head.c + d.move_x, snake_head.r + d.move_y)
    if not new_head.isinside():
        done = True
    
    if new_head in d.snake:
        done = True
    
    for i, el in enumerate(d.answers1):
        if el.snake_in_answer(new_head):
            d.answers1.pop(i)

    d.snake.append(new_head)
    d.snake.pop(0)
    
    
    pygame.display.flip()
    d.clock.tick(3)


    

