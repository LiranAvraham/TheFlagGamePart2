import pandas as pd
import os


file_name = 'data.csv'

def creat_csv():
    data = {}
    df = pd.DataFrame(data)
    if not os.path.exists(file_name):
        df.to_csv(file_name)
        print(df.head())
    return data

creat_csv()

def save_new_data(num_key, matrix,matrix_grass,solider_loc):
    data = creat_csv()
    data[num_key] = [matrix,matrix_grass,solider_loc]
    df = pd.DataFrame(data)
    df.to_csv(file_name)
    return data





save_new_data(1, [],["grass"],(1,2))
