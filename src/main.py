import requests, json
import re
from datetime import datetime as dt
from datetime import timedelta

def get_color(x):
	if x == 0:
		return 0
	x = min(2800,x)
	x = x + 1
	return (x+399) // 400

username = input()
#対象のurl
target_url = "https://atcoder.jp/users/"
target_url += username
target_url += "/history/json"

#サイト管理者に分かるように自身の連絡先などをUser-Agentに記載する
headers = {
	'User-Agent':username 
}

#対象ページのhtml
html = requests.get(target_url, headers=headers).text

url = requests.get(target_url)
text = url.text

data = json.loads(text)
color = list("黒灰茶緑水青黄橙赤")

color_mae = 0;
zero = timedelta(0)
color_day = [zero] * 9 
date = dt.strptime(data[0]["EndTime"][0:13], '%Y-%m-%dT%H')

date_sum = timedelta(0)
print(username)
for row in data:
	now_date = dt.strptime(row["EndTime"][0:13], '%Y-%m-%dT%H')
	#前回のコンテスト終了からの日数を算出する
	date_delta = now_date - date
	date = now_date
	ind = get_color(row["NewRating"])
	color_day[color_mae] = color_day[color_mae] + date_delta
	#色変したら、〜色で過ごした期間を出力する
	date_sum += date_delta
	if ind != color_mae:
		if color_mae == 0:
			color_mae = ind
			continue
		print(color[color_mae]+"で過ごした期間: ")
		print(date_sum)
		date_sum = timedelta(0)
	color_mae = ind
# 今の日付も考える
now_date = dt.now()
#前回のコンテスト終了からの日数を算出する
date_delta = now_date - date
color_day[color_mae] = color_day[color_mae] + date_delta
date_sum += date_delta
print(color[color_mae]+"で過ごした期間: ")
print(date_sum)
date_sum = timedelta(0)
color_mae = ind
for i, _ in enumerate(color_day): 
	if i == 0: continue
	print(color[i] +":")
	print(_)
