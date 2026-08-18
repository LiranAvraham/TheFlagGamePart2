import pandas as pd
import os

from newfolder.screen import draw_game

# import json



file_name = 'save_game_progress.csv'
data = {}

def creat_csv():
    data = {}
    df = pd.DataFrame(data)
    if not os.path.exists(file_name):
        df.to_csv(file_name)

creat_csv()

def save_new_data(num_key, matrix, matrix_grass, solider_loc, data):
    data[num_key] = [matrix, matrix_grass, solider_loc]
    df = pd.DataFrame(data)
    df.to_csv(file_name)

    return data

def return_data(num_key):
    df = pd.read_csv(file_name)
    rows = df.iloc[0:3,num_key]
    new_matrix = rows[0]
    new_grass = rows[1]
    new_solider_loc = rows[2]

    return new_matrix, new_grass, new_solider_loc

def load_game(key):
    df = pd.read_csv(file_name)
    saved_game = save_new_data().iloc[0]

    soldier_row = int(saved_game["soldier_row"])
    soldier_col = int(saved_game["soldier_col"])
    matrix = saved_game["matrix"]
    grass_matrix = saved_game["grass_matrix"]

    return draw_game(soldier_row, soldier_col, matrix, grass_matrix)