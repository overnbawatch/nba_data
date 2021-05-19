import json
import pandas as pd
import csv

from matplotlib import pyplot as plt

df = pd.read_csv("seasons_2020-2021.csv")

# 列を全部表示されるようにオプションの設定
pd.set_option('display.max_columns', 150)

# チーム別勝利数の集計
gamelist = {}
count = 0
for index, games in df.iterrows():
    count += 1
    if games['halftime'] is None:
        continue
    elif games['score'] > games['score.1']:
        if not games["nickName"] in gamelist:
            team = [games['nickName']]
            winpoint = [1]
            gamelist.update(zip(team, winpoint))
        else:
            gamelist[games["nickName"]] += 1
    elif games['score'] < games['score.1']:
        if not games["nickName.1"] in gamelist:
            team = [games['nickName.1']]
            winpoint = [1]
            gamelist.update(zip(team, winpoint))
        else:
            gamelist[games["nickName.1"]] += 1

winteam_sorted = sorted(gamelist.items(), key=lambda x: x[1])

x = []
y = []
for k in winteam_sorted:
    x.append(k[0])
    y.append(k[1])
# グラフのレイアウトの変更
plt.barh(x, y)
plt.tight_layout()
# グラフの表示
plt.show()


# 行の表示
print(df.head)

# halftimeがNaNのデータを抽出して表示
csvdata = df[df["halftime"].isnull()]
nonend = csvdata.loc[:, ['startTimeUTC', 'nickName', 'nickName.1']]
print(nonend)


