import pandas as pd
_path = "/Users/hamidelmi/Desktop/Apply/025-UKP TUD/task2/code/data/output/models/dataset2/3/result1.csv"


df = pd.read_csv(_path)

print(df.describe())

print(df[df["l1"] != df["l2"]]["cnt"].describe())

