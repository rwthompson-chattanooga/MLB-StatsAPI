import pandas as pd
from pathlib import Path

base_path = Path(__file__).parent
file_path = base_path / "data" / "gl2002.txt"

maindata = pd.read_csv(file_path)
print(maindata.head())
print(len(maindata))