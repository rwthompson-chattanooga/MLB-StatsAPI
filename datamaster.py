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

print(base_path)

#file_list = list(base_path.glob('data/*.txt'))
#print(file_list)

#maindata = pd.concat((pd.read_csv(f) for f in file_list), ignore_index=True)
#print(maindata.head())
#print(len(maindata))
#print(maindata.iloc[0:5,0:12])

game_results = pd.DataFrame()
#concat(pd.read_csv(base_path/'data'/'gl2002.txt'))
#print(game_result_score_only.info())

#for file in file_list:
#    game_result_score_only = pd.concat(pd.read_csv(file)[:])