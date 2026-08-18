import pygame

from consts import *


def create_screen():
    screen = pygame.display.set_mode((LENGTH_WINDOW, HEIGHT_WINDOW))
    pygame.display.set_caption("The Flag Game")

    return screen


def create_images():
    cell_width = LENGTH_WINDOW // BOARD_NUM_COLS
    cell_height = HEIGHT_WINDOW // BOARD_NUM_ROWS

    soldier_image = pygame.transform.scale(SOLDIER_IMAGE, (cell_width * 4, cell_height * 4))
    flag_image = pygame.transform.scale(FLAG_IMAGE, (cell_width * 4, cell_height * 3))
    mine_image = pygame.transform.scale(MINE_IMAGE, (cell_width * 3, cell_height))
    grass_image = pygame.transform.scale(GRASS_IMAGE, (cell_width * 3, cell_height*3))

    return soldier_image, flag_image, mine_image, grass_image


def draw_game(screen, matrix, grass_matrix, soldier_row, soldier_col, flag_row, flag_col, show_mines, soldier_image, flag_image, mine_image, grass_image, cell_width, cell_height):
    font = pygame.font.SysFont(None, 20)
    text_welcome = font.render(WELCOME_SCREEN, True, WHITE)
    pygame.display.flip()

    if show_mines:
        screen.fill(BACKGROUND_COLOR_FOR_NIGHT_MODE)
    else:
        screen.fill(BACKGROUND_COLOR)

    if show_mines:
        for row in range(BOARD_NUM_ROWS):
            for col in range(BOARD_NUM_COLS):
                if matrix[row][col] == MINE:
                    if col == 0 or matrix[row][col - 1] != MINE:
                        x = col * cell_width
                        y = row * cell_height
                        screen.blit(mine_image, (x, y))

    else:
        for row in range(BOARD_NUM_ROWS):
            for col in range(BOARD_NUM_COLS):
                if grass_matrix[row][col] == GRASS:
                    x = col * cell_width
                    y = row * cell_height
                    screen.blit(grass_image, (x, y))

    screen.blit(soldier_image, (soldier_col * cell_width, soldier_row * cell_height))
    screen.blit(flag_image, (flag_col * cell_width, flag_row * cell_height))
    screen.blit(text_welcome, (100, 0))

    pygame.display.flip()