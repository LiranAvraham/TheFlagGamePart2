import pygame

from consts import *


def move_soldier(event, soldier_row, soldier_col, show_mines):
    if not show_mines:
        if event.key == pygame.K_UP:
            if soldier_row > 0:
                soldier_row -= 1

        elif event.key == pygame.K_DOWN:
            if soldier_row + SOLDIER_NUM_ROWS < BOARD_NUM_ROWS:
                soldier_row += 1

        elif event.key == pygame.K_LEFT:
            if soldier_col > 0:
                soldier_col -= 1

        elif event.key == pygame.K_RIGHT:
            if soldier_col + SOLDIER_NUM_COLS < BOARD_NUM_COLS:
                soldier_col += 1

    return soldier_row, soldier_col


def check_soldier_location(matrix, soldier_row, soldier_col):
    legs_row = soldier_row + SOLDIER_NUM_ROWS - 1

    for col in range(soldier_col, soldier_col + SOLDIER_NUM_COLS):
        if matrix[legs_row][col] == MINE:
            return MINE

        elif matrix[legs_row][col] == FLAG:
            return FLAG

    return EMPTY_PLACE