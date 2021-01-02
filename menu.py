import pygame
import pygame_menu
import main as m
import data_and_func as d

# pygame.init()

menu_theme = pygame_menu.themes.THEME_BLUE.copy()
menu_theme.background_color = (178, 255, 103)
menu_theme.title_font_color = (0, 0, 0)
menu_theme.title_background_color = (0, 255, 0)
menu = pygame_menu.Menu(300, 400, 'Welcome',
                       theme=menu_theme)

# menu.add_text_input('Name :', default='John Doe')
menu.add_button('Snake', m.snake)
menu.add_button('Python test snake', m.start_the_game)
menu.add_button('Quit', pygame_menu.events.EXIT)

while True:
    m.screen.fill(d.WHITE)

    for row in range(d.background_block_rows+2):
                for column in range(d.background_block_columns+2):
                    color = d.BLUE
                    if (row+column)%2 == 0:
                        color = d.YELLOW
                    d.draw_background(color, column, row)
    

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if menu.is_enabled():
        menu.update(events)
        menu.draw(m.screen)

    pygame.display.update()