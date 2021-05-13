import json
import pandas as pd
import csv

from matplotlib import pyplot as plt

df = pd.read_csv("seasons_2020-2021.csv")


print(df.info())

# 欠損値の確認
print(df.isnull().sum())

# 重複の確認
print(df.duplicated().value_counts())