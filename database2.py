import pandas as pd
import os


file_name = 'data.csv'
data = {}
def creat_csv():
    df = pd.DataFrame(data)
    if not os.path.exists(file_name):
        df.to_csv(file_name)
        print(df.head())
    return data

creat_csv()

def save_new_data(num_key, matrix,matrix_grass,solider_loc, data):
    data[num_key] = [matrix,matrix_grass,solider_loc]
    df = pd.DataFrame(data)
    df.to_csv(file_name)

def return_data(num_key):
    df = pd.read_csv(file_name)
    rows = df.iloc[0:3,num_key]
    new_matrix = rows[0]
    new_grass = rows[1]
    new_solider_loc =rows[2]
    return new_matrix,new_grass,new_solider_loc





save_new_data(1, [],["grass"],(1,2))
