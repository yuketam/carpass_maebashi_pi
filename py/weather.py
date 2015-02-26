#!/usr/bin/python
#coding:utf-8
import sys
import sqlite3
import random

#db = sqlite3.connect("weather_data.db", isolation_level=None)

# 天気sqlからcity_code都市のデータを取ってくる
#def __getWeather(city_code):
#	data = db.cursor()
#	data.execute(u'SELECT city, weather, COUNT(weather) AS count FROM weather WHERE city=47401 GROUP BY weather')
#	for row in data:
#		print row

# あらかじめnodeで計算した都市の天気データdictionaryを返す
# TODO nodeでつくったアルゴリズムをpythonで書き直し	
def __getDice(city_code):
	print 'initializing Maebashi weather dice...'
	return {
		'sunny': 0.5319956191817258,
		'cloudy': 0.37205663772197454,
		'rainy': 0.09184072596417117,
		'snowy': 0.004107017132128465
	}

# 乱数作成
def __makeRand():
	tryCount = 100
	randList = []

	for i in range(tryCount):
		randList.append(random.random())
	print randList

	rand_r = randList[random.randint(0, tryCount-1)]
	print '>', str(rand_r)

	return rand_r


#乱数と天気データからサイコロの目を計算する
def __evaluate(data, rand):
	min = 0
	max = 0
	result = ''

	for key, val in data.items():
		max = min + val
		print 'evaluate...', key, val, min, rand, max
		if min <= rand and rand < max:
			result = key
			break

		min += val

	return result


#サイコロを振る
def throwDice(city_code):
	dice_data = __getDice(city_code)
	rand = __makeRand()

	return __evaluate(dice_data, rand)