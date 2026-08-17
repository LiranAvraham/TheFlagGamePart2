from turtledemo import clock

import pygame
import sys

from consts import *
from game_field import *
from soldier import *
from screen import *
from matrix_builder import *
import database

pygame.init()

screen = create_screen()

# create game matrix
matrix = create_matrix()

# create grass matrix
grass_matrix = create_matrix()

flag_row, flag_col = add_flag_to_matrix(matrix)

add_mines_to_matrix(matrix)
add_grass_to_matrix(grass_matrix, matrix)

soldier_row = 0
soldier_col = 0

# calculate matrix cells
cell_width = LENGTH_WINDOW // BOARD_NUM_COLS
cell_height = HEIGHT_WINDOW // BOARD_NUM_ROWS

# create images of soldier, flag, mine, grass
soldier_image, flag_image, mine_image, grass_image = create_images()

# font for win message
font = pygame.font.SysFont("Arial", 50)

winner_dialog = font.render("You won", True, BACKGROUND_COLOR_FOR_NIGHT_MODE)
loser_dialog = font.render("You lost", True, BACKGROUND_COLOR_FOR_NIGHT_MODE)

show_mines = False
show_mines_start_time = 0

running = True
while running:

    # go through pygame events
    for event in pygame.event.get():
        # close window

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                i=0
                time_event = pygame.time.Clock()
                while i<5:
                    time_event.tick(10)
                print(time_event)
                show_mines = True
                show_mines_start_time = pygame.time.get_ticks()
                night_mode_matrix(matrix, screen)
                pygame.display.flip()

                soldier_image = pygame.transform.scale(SOLDIER_IMAGE_NIGHT, (cell_width*4, cell_height*4))

            soldier_row, soldier_col = move_soldier(event, soldier_row, soldier_col, show_mines)

    if show_mines:

        current_time = pygame.time.get_ticks()

        if current_time - show_mines_start_time >= 1000:
            show_mines = False
            soldier_image = pygame.transform.scale(SOLDIER_IMAGE, (cell_width * 4, cell_height * 4))

    soldier_location = check_soldier_location(matrix, soldier_row, soldier_col)

    if soldier_location == MINE:
        screen.blit(loser_dialog, (50, 50))
        pygame.display.flip()
        pygame.time.wait(3000)


        running = False

    elif soldier_location== FLAG:
        screen.blit(winner_dialog, (100, 100))
        pygame.display.flip()
        pygame.time.wait(3000)

        running = False
    draw_game(screen, matrix, grass_matrix, soldier_row, soldier_col, flag_row, flag_col, show_mines, soldier_image, flag_image, mine_image, grass_image, cell_width, cell_height)
    pygame.display.flip()
pygame.quit()
sys.exit()