"""
Docstring for datamaster

This isn't really a docstring but ...

The purpose of this code is to concatenate the game logs download
from retrosheet into one master file. 

The master file has a heading row and contains game data for every game in MLB
for the 2002-2025 seasons, with the exception of the 2020 season.

The ultimate goal is to use this data for analytically decision making on the Kalshi platform.
"""

import pandas as pd
from pathlib import Path
import glob

base_path = Path(__file__).parent
data_path = Path(base_path/'data')

#print(data_path)

master_data = pd.DataFrame()
column_names = [
    'Date',
    'Game Number',
    'Day of Week',
    'Visiting Team',
    'Visiting Team League',
    'Visiting Team Game Number',
    'Home Team',
    'Home Team League',
    'Home Team Game Number',
    'Visiting Score',
    'Home Score',
    'Length in Outs',
    'Day/Night',
    'Completion',
    'Forfeit',
    'Protest',
    'Park ID',
    'Attendance',
    'Time in Minutes',
    'Visiting Line Score',
    'Home Line Score',
]

#master_data.columns = column_names
    
print(master_data.shape)
master_data = pd.concat([master_data, pd.read_csv(data_path/'gl2002.txt', header=None)])
print(master_data.head())
#master_data = pd.concat([master_data, pd.read_csv(data_path/'gl2003.txt')], ignore_index=True)
#print(master_data.shape)
master_data.to_csv(data_path/'master.csv')


""" for file in data_path.iterdir():
    if file.is_file():
        #print(file.name[2:6])
        #print(pd.read_csv(file).shape)
        new_season = pd.read_csv(file)
        master_data = pd.concat([master_data, new_season], axis = 0, ignore_index = True) """


#game_results = pd.read_csv(base_path/'data'/"gl2002.txt")

#print(game_results.shape)

#teams_and_score = game_results.iloc[:, [3, 6, 9, 10]]
#teams_and_score.columns = ["Visiting Team", "Home Team", "Visitor Score", "Home Score"]

#print(teams_and_score.shape)
""" master_data.dropna()
print(master_data.shape)
master_data.to_csv(data_path/'master.csv', index=False)
print("Finished!") """