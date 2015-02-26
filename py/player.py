#!/usr/bin/python
import sys
import subprocess
import random
import weather

while (1):
	print 'runnning dice program...'

	rand = weather.throwDice('maebashi')
	print 'weather', rand

	fileName = './normal.mp4'
	if rand == 'rainy':
		fileName = './hit.mp4'

	a = subprocess.call([ "OMXplayer", fileName])
	#a = subprocess.call([ "node", './async.js', '--rand=3'])

