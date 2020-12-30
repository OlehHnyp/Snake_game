import pygame
import data_and_func as d
import random
import sys

pygame.init()
score = 0
life = 0


def game(question, answers):
    global score, life
    life += 1
    screen = pygame.display.set_mode(d.screen_size)
    pygame.display.set_caption(d.caption)
    snake = d.set_default_snake()
    d.reserve_move_x = 1
    d.reserve_move_y = 0


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
        score_text = d.question_courier.render(f"Score: {score}", 0, d.WHITE)
        life_text = d.question_courier.render(f"Life: {life}", 0, d.WHITE)

        screen.blit(score_text, (d.screen_width-350, 5))
        screen.blit(life_text, (d.screen_width-350, 45))



        snake_head = snake[-1]

        
        

        for row in range(d.block_rows):
            for column in range(d.block_columns):
                color = d.BLUE
                if (row+column)%2 == 0:
                    color = d.YELLOW
                d.add_block(color, column, row)

        for block in snake:
            d.add_block(d.RED, block.c, block.r)

        check_answer = []
        for el in answers:
            if el not in check_answer: # and not el.snake_in_answer(snake):
                el.add_answers()
            else:
                while el in check_answer:# or el.snake_in_answer(snake):
                    el.c = random.randint(0, d.block_columns-2)
                    el.r = random.randint(0, d.block_rows-3)
                el.add_answers()
            check_answer.append(el)




        d.move_x = d.reserve_move_x
        d.move_y = d.reserve_move_y

        pygame.display.flip()
        
        new_head = d.Blocks(snake_head.c + d.move_x, snake_head.r + d.move_y)

        if not new_head.isinside():
            life -= 1
            d.reserve_move_x = 1
            d.reserve_move_y = 0
            snake = d.set_default_snake()
            new_head = d.Blocks(1, d.block_rows-1)

            if life < 0:
                print('not inside')
                pygame.quit()
                sys.exit()
        
        if new_head in snake:
            life -= 1
            d.reserve_move_x = 1
            d.reserve_move_y = 0
            snake = d.set_default_snake()
            new_head = d.Blocks(1, d.block_rows-1)
            if life < 0:
                print('nh in s')
                pygame.quit()
                sys.exit()
        
        for i, el in enumerate(answers):
            if el.snake_head_in_answer(new_head):                
                score += el.score
                question.point -= el.point
                if question.point<=0:
                    done=True
                life += el.life
                if life < 0:
                    pygame.quit()
                    sys.exit()
                answers.pop(i)

        snake.append(new_head)
        snake.pop(0)
        
        
        
        d.clock.tick(5)
    return score


for el in d.q_a_list_zip:
    game(el[0], el[1])
print(score)




    

