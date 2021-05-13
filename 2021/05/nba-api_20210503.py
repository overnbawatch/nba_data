import pandas as pd

df = pd.read_json("steph_game_all.json")

csv_data = df.to_csv("hoge.csv")