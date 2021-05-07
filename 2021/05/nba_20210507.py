import json
import pandas as pd

from matplotlib import pyplot as plt

df = pd.read_json("games_2020.json")

with open('games_2020.json','r') as f:
   df = json.load(f)

dic = df['api']['games']

winteam = {}

for gamelist in dic:
    if not len(gamelist['vTeam']['score']['points']) == 0:
       if gamelist['vTeam']['nickName'] in winteam:
           winteam[gamelist['vTeam']['nickName']] += 1
       else:
           team = [gamelist['vTeam']['nickName']]
           winpoint = [1]
           winteam.update(zip(team, winpoint))

winteam_sorted = sorted(winteam.items(), key=lambda x:x[1], reverse=True)

x = []
y = []

for k in winteam_sorted:
    x.append(k[0])
    y.append(k[1])

plt.bar(x, y)
plt.show()
