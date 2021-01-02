import pygame
import random
import sys
import time
import pygame_menu

import data_and_func as d

pygame.init()
screen = pygame.display.set_mode(d.screen_size)


def snake():    
    score = 0
    done = False
    pygame.display.set_caption(d.caption)
    d.snake = [d.Blocks(0, d.block_rows-1), 
               d.Blocks(0, d.block_rows-1),
               d.Blocks(0, d.block_rows-1),
               d.Blocks(0, d.block_rows-1),
               d.Blocks(1, d.block_rows-1)]
    
    d.reserve_move_x = 1
    d.reserve_move_y = 0



    

    while not done:
        speed = len(d.snake)//4
        score_text = d.question_courier.render(f"Score: {score}", 0, d.WHITE)
        snake_head = d.snake[-1]

        screen.fill(d.WHITE)
        d.draw_margins(d.SUPER_BLUE)
        screen.blit(score_text, (d.screen_width-350, 5))

        for row in range(d.block_rows):
            for column in range(d.block_columns):
                color = d.BLUE
                if (row+column)%2 == 0:
                    color = d.YELLOW
                d.add_block(color, column, row)

        for block in d.snake:
            d.add_block(d.RED, block.c, block.r)

        while d.food in d.snake:
            d.food.c = random.randint(0, d.block_columns-1)
            d.food.r = random.randint(0, d.block_rows-1)
        d.add_block(d.GREEN, d.food.c, d.food.r)
        
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

        d.move_x = d.reserve_move_x
        d.move_y = d.reserve_move_y

        pygame.display.flip()
        d.move_sound.play()
        
        new_head = d.Blocks(snake_head.c + d.move_x, snake_head.r + d.move_y)

        if not new_head.isinside():
            d.reserve_move_x = 1
            d.reserve_move_y = 0
            done = True            
            d.crash_sound.play()
            time.sleep(1)
        
        if new_head in d.snake:
            d.reserve_move_x = 1
            d.reserve_move_y = 0
            done = True            
            d.selfcrash_sound.play()
            time.sleep(1)

        if new_head == d.food:
            score += 1
            d.snake.insert(0,d.food)
            d.right_sound.play()

        d.snake.append(new_head)
        d.snake.pop(0)
        
        d.clock.tick(2+speed)

    d.game_over_sound.play()
    d.screen.fill(d.WHITE)
    for row in range(d.background_block_rows+2):
                for column in range(d.background_block_columns+2):
                    color = d.BLUE
                    if (row+column)%2 == 0:
                        color = d.YELLOW
                    d.draw_background(color, column, row)

    pygame.draw.rect(d.screen, d.GREEN,
                    ((d.screen_width-500)//2,
                    (d.screen_height-150)//2,
                    500,
                    150)
                    )
    text1 = d.final_score_courier.render(f"GAME OVER!", 0, d.WHITE)
    text2 = d.final_score_courier.render(f"Your score is {score}", 0, d.WHITE)
    d.screen.blit(text1,
                ((d.screen_width-300)//2,
                (d.screen_height-120)//2,)
                )
    d.screen.blit(text2,
                ((d.screen_width-460)//2,
                (d.screen_height)//2,)
                )

    pygame.display.flip()

    time.sleep(3)
    return score




def start_the_game():
    score = 0
    life = 0
    done = False
    d.snake = [d.Blocks(0, d.block_rows-1), 
               d.Blocks(0, d.block_rows-1),
               d.Blocks(0, d.block_rows-1),
               d.Blocks(0, d.block_rows-1),
               d.Blocks(1, d.block_rows-1)]

    def test(question, answers):
        nonlocal life, score, done
        life += 1
        speed = len(d.snake)//5
        pygame.display.set_caption(d.caption)
        d.snake = d.set_default_snake(d.snake)
        d.reserve_move_x = 1
        d.reserve_move_y = 0

        while not done:
            score_text = d.question_courier.render(f"Score: {score}", 0, d.WHITE)
            life_text = d.question_courier.render(f"Life: {life}", 0, d.WHITE)
            snake_head = d.snake[-1]
            check_answer = []

            screen.fill(d.WHITE)
            d.draw_margins(d.SUPER_BLUE)
            question.add_question()
            screen.blit(score_text, (d.screen_width-350, 5))
            screen.blit(life_text, (d.screen_width-350, 45))
            
            for row in range(d.block_rows):
                for column in range(d.block_columns):
                    color = d.BLUE
                    if (row+column)%2 == 0:
                        color = d.YELLOW
                    d.add_block(color, column, row)

            for el in answers:
                if el not in check_answer: # and not el.snake_in_answer(snake):
                    el.add_answers()
                else:
                    while el in check_answer:# or el.snake_in_answer(snake):
                        el.c = random.randint(0, d.block_columns-2)
                        el.r = random.randint(0, d.block_rows-3)
                    el.add_answers()
                check_answer.append(el)

            for block in d.snake:
                d.add_block(d.RED, block.c, block.r)
            
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

            d.move_x = d.reserve_move_x
            d.move_y = d.reserve_move_y

            pygame.display.flip()
            d.move_sound.play()
            
            new_head = d.Blocks(snake_head.c + d.move_x, snake_head.r + d.move_y)

            if not new_head.isinside():
                life -= 1
                d.reserve_move_x = 1
                d.reserve_move_y = 0
                d.snake = d.set_default_snake(d.snake)
                new_head = d.Blocks(1, d.block_rows-1)

                if life < 0:
                    done = True
                
                d.crash_sound.play()
                time.sleep(1)
            
            if new_head in d.snake:
                life -= 1
                d.reserve_move_x = 1
                d.reserve_move_y = 0
                d.snake = d.set_default_snake(d.snake)
                new_head = d.Blocks(1, d.block_rows-1)

                if life < 0:
                    done = True
                
                d.selfcrash_sound.play()
                time.sleep(1)

            for i, el in enumerate(answers):
                if el.snake_head_in_answer(new_head):                
                    score += el.score
                    if score < 0:
                        score = 0
                    d.snake.append(new_head)
                    question.point -= el.point
                    if question.point<=0:
                        pygame.display.flip()
                        d.next_level_sound.play()
                        time.sleep(1)
                        return score
                    life += el.life
                    if life < 0:
                        done = True
                    d.right_sound.play() if el.score>0 else d.wrong_sound.play()
                    answers.pop(i)

            d.snake.append(new_head)
            d.snake.pop(0)
            
            d.clock.tick(2+speed)
        return score
        
    for el in d.q_a_list_zip:
        test(el[0], el[1])

    d.game_over_sound.play()
    d.screen.fill(d.WHITE)
    for row in range(d.background_block_rows+2):
                for column in range(d.background_block_columns+2):
                    color = d.BLUE
                    if (row+column)%2 == 0:
                        color = d.YELLOW
                    d.draw_background(color, column, row)

    pygame.draw.rect(d.screen, d.GREEN,
                    ((d.screen_width-500)//2,
                    (d.screen_height-150)//2,
                    500,
                    150)
                    )
    text1 = d.final_score_courier.render(f"GAME OVER!", 0, d.WHITE)
    text2 = d.final_score_courier.render(f"Your score is {score}", 0, d.WHITE)
    d.screen.blit(text1,
                ((d.screen_width-300)//2,
                (d.screen_height-120)//2,)
                )
    d.screen.blit(text2,
                ((d.screen_width-460)//2,
                (d.screen_height)//2,)
                )

    pygame.display.flip()

    time.sleep(3)




    

