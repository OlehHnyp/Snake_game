import pygame
import data_and_func as d
import random
import sys

pygame.init()



def game(question, answers):
    screen = pygame.display.set_mode(d.screen_size)
    pygame.display.set_caption(d.caption)


    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
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

        question.add_question()

        snake_head = d.snake[-1]

        
        

        for row in range(d.block_rows):
            for column in range(d.block_columns):
                color = d.BLUE
                if (row+column)%2 == 0:
                    color = d.YELLOW
                d.add_block(color, column, row)
        for block in d.snake:
            d.add_block(d.RED, block.c, block.r)

        check_answer = []
        for el in answers:
            if el not in check_answer and not el.snake_in_answer(d.snake):
                el.add_answers()
            else:
                while el in check_answer or el.snake_in_answer(d.snake):
                    el.c = random.randint(0, d.block_columns-2)
                    el.r = random.randint(0, d.block_rows-2)
                el.add_answers()
            check_answer.append(el)




        d.move_x = d.reserve_move_x
        d.move_y = d.reserve_move_y
        
        new_head = d.Blocks(snake_head.c + d.move_x, snake_head.r + d.move_y)
        if not new_head.isinside():
            done = True
        
        if new_head in d.snake:
            done = True
        
        for i, el in enumerate(answers):
            if el.snake_head_in_answer(new_head):
                question.point -= el.point
                if question.point<=0:
                    done=True
                answers.pop(i)

        d.snake.append(new_head)
        d.snake.pop(0)
        
        
        pygame.display.flip()
        d.clock.tick(3)

for el in d.q_a_list_zip:
        game(el[0], el[1])




    

