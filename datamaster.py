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

game_results = pd.read_csv(base_path/'data'/"gl2002.txt")

#print(game_results.shape)

teams_and_score = game_results.iloc[:, [3, 6, 9, 10]]
teams_and_score.columns = ["Visiting Team", "Home Team", "Visitor Score", "Home Score"]

print(teams_and_score.head())