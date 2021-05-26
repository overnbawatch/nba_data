import pandas as pd

from matplotlib import pyplot as plt

df = pd.read_csv("seasons_2020-2021.csv")

# 列を全部表示されるようにオプションの設定
pd.set_option('display.max_columns', 150)
#最大表示行数の指定（ここでは50行を指定）
pd.set_option('display.max_rows', 100)

# seasonStageに含まれるデータをカウント
print(df['seasonStage'].value_counts())

# seasonStageが2(レギュラーシーズン)の場合のみのデータを表示
jazz_win = df[(df['seasonStage'] == 2) & ((df['teamId'] == 40) | (df['teamId.1'] == 40))]

print(jazz_win.duplicated(subset='startTimeUTC').value_counts())
# 試合時間が重複している行の削除して表示
# print(jazz_win.drop_duplicates(subset='startTimeUTC'))
# jazz_win.to_csv('jazz_win.csv')
#
# # チーム別勝利数の集計
# gamelist = {}
# count = 0
# for index, games in df.iterrows():
#     if(games['seasonStage']==2):
#         count += 1
#         if games['halftime'] is None:
#             continue
#         elif games['score'] > games['score.1']:
#             if not games["nickName"] in gamelist:
#                 team = [games['nickName']]
#                 winpoint = [1]
#                 gamelist.update(zip(team, winpoint))
#             else:
#                 gamelist[games["nickName"]] += 1
#         elif games['score'] < games['score.1']:
#             if not games["nickName.1"] in gamelist:
#                 team = [games['nickName.1']]
#                 winpoint = [1]
#                 gamelist.update(zip(team, winpoint))
#             else:
#                 gamelist[games["nickName.1"]] += 1
#
# winteam_sorted = sorted(gamelist.items(), key=lambda x: x[1])
#
# x = []
# y = []
# for k in winteam_sorted:
#     x.append(k[0])
#     y.append(k[1])
# # グラフのレイアウトの変更
# plt.barh(x, y)
# plt.tight_layout()
# # グラフの表示
# plt.show()
#

