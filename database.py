import pandas as pd
import os
import csv
import json
import pygame

database_data = ["soldier_row", "soldier_col", "matrix", "grass_matrix"]
file_name = "save_game_progress.csv"
# database = pd.read_csv(file_name)

NUMBER_KEYS = {
    pygame.K_1: 1,
    pygame.K_2: 2,
    pygame.K_3: 3,
    pygame.K_4: 4,
    pygame.K_5: 5,
    pygame.K_6: 6,
    pygame.K_7: 7,
    pygame.K_8: 8,
    pygame.K_9: 9
}

def save_game(key, soldier_row, soldier_col, matrix, grass_matrix):

    game_data = {
        "soldier_row": soldier_row,
        "soldier_col": soldier_col,
        "matrix": matrix,
        "grass_matrix": grass_matrix
    }

def init_db():
    if not os.path.exists(file_name):
        database = pd.DataFrame(columns=["soldier_row", "soldier_col", "matrix", "grass_matrix"])
        database.to_csv(database, index = False)


