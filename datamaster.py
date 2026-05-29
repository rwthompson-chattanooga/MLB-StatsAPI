import pandas as pd
from pathlib import Path
import glob

base_path = Path(__file__).parent
print(base_path)
file_list = list(base_path.glob('data/*.txt'))
#print(file_list)

maindata = pd.concat((pd.read_csv(f) for f in file_list), ignore_index=True)
#print(maindata.head())
print(len(maindata))