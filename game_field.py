import random

from consts import *


def create_matrix():
    matrix = []

    for row in range(BOARD_NUM_ROWS):
        new_row = []

        for col in range(BOARD_NUM_COLS):
            new_row.append(EMPTY_PLACE)

        matrix.append(new_row)

    return matrix


def add_flag_to_matrix(matrix):
    flag_row = BOARD_NUM_ROWS - FLAG_NUM_ROWS
    flag_col = BOARD_NUM_COLS - FLAG_NUM_COLS

    for row in range(flag_row, flag_row + FLAG_NUM_ROWS):
        for col in range(flag_col, flag_col + FLAG_NUM_COLS):
            matrix[row][col] = FLAG

    return flag_row, flag_col


def add_mines_to_matrix(matrix):
    mines_created = 0

    while mines_created < NUM_OF_MINES:
        row = random.randint(0, BOARD_NUM_ROWS - 1)
        col = random.randint(0, BOARD_NUM_COLS - MINE_NUM_COLS)

        can_place_mine = True

        for i in range(MINE_NUM_COLS):
            if matrix[row][col + i] != EMPTY_PLACE:
                can_place_mine = False

            if row < SOLDIER_NUM_ROWS and col + i < SOLDIER_NUM_COLS:
                can_place_mine = False

        if can_place_mine:
            for i in range(MINE_NUM_COLS):
                matrix[row][col + i] = MINE

            mines_created += 1


def add_grass_to_matrix(grass_matrix, matrix):
    grass_created = 0
    grass_with_mine = 0
    max_grass_with_mine = NUM_OF_GRASS // 2

    while grass_created < NUM_OF_GRASS:
        row = random.randint(0, BOARD_NUM_ROWS - 1)
        col = random.randint(0, BOARD_NUM_COLS - 1)

        if grass_matrix[row][col] != EMPTY_PLACE:
            continue

        if row < SOLDIER_NUM_ROWS and col < SOLDIER_NUM_COLS:
            continue

        if matrix[row][col] == FLAG:
            continue

        # if matrix[row][col] == FLAG:
        #     break

        if matrix[row][col] == MINE:
            if grass_with_mine < max_grass_with_mine:
                grass_matrix[row][col] = GRASS
                grass_with_mine += 1
                grass_created += 1
        else:
            grass_matrix[row][col] = GRASS
            grass_created += 1