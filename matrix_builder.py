import pygame
from game_field import*
from consts import *


def create_bord_cells():
    screen_matrix = []
    for row in range(BOARD_NUM_ROWS):
        screen_matrix.append([])
        for col in range(BOARD_NUM_COLS):
            screen_matrix[row].append(EMPTY_PLACE)
    return screen_matrix

def grid(screen_matrix, screen):
    cell_width = LENGTH_WINDOW // BOARD_NUM_COLS
    for row in range(len(screen_matrix)):
        for col in range(len(screen_matrix[row])):
            x =col*cell_width
            y= row * cell_width

            rect = pygame.Rect(x,y,cell_width-1, cell_width-1)
            pygame.draw.rect(screen,BACKGROUND_COLOR,rect)
            pygame.display.flip()
def night_mode_matrix(matrix, screen):
    cell_size = cell_width *cell_height
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            x =col*cell_width
            y= row * cell_width

            rect = pygame.Rect(x,y,cell_size-1, cell_size-1)
            pygame.draw.rect(screen,BACKGROUND_COLOR_FOR_NIGHT_MODE,rect)
    pygame.display.flip()