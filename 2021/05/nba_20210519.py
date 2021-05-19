import pandas as pd
import csv
import requests

# NBA-APIからJSONデータの取得
url = "https://api-nba-v1.p.rapidapi.com/games/seasonYear/2020"

headers = {
    'x-rapidapi-key': "***********************************",
    'x-rapidapi-host': "api-nba-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

# NBA-APIから取得したJSONデータを使用
df = pd.read_json(response)

dic = df['api']['games']

winteam = {}
gamelist = []

# 書き込み用のCSVファイルのオープン
# newlineを設定しないと1行飛ばしで書き込まれてしまうので注意
with open('seasons_2020-2021.csv', 'w', newline='') as f:
    w = csv.writer(f)

    # ヘッダの作成
    headerlist = []
    for mylist in dic:
        print(mylist)
        for k,v in mylist.items():
            if k=='vTeam' or k=='hTeam':
                for key in v.keys():
                    headerlist.append(key)
            else:
                headerlist.append(k)

        break
    w.writerow(headerlist)

    # 全データの作成
    for gamedic in dic:
        gamelist = []
        for k,v in gamedic.items():
            if k == 'vTeam' or k == 'hTeam':
                for kscore, vscore in v.items():
                    if kscore == 'score':
                        for point in vscore.values():
                            gamelist.append(point)
                    else:
                        gamelist.append(vscore)
            else:
                gamelist.append(v)
        w.writerow(gamelist)
