import os
import random

dir = input('dir: ')
verse1 = int(input('verse 1: '))
verse2 = int(input('verse 2: '))
verse3 = int(input('verse 3: '))
refrain = int(input('refrain: '))
refrain_str = 'REFRAIN \n'
files = os.listdir(dir)
lines = []

for file in files:
    temp = open(dir + '/' + file,'r')
    for line in temp:
        lines.append(line)
    temp.close

for i in range(refrain):
    refrain_str += lines[random.randint(0, len(lines) - 1)]
song = open(dir + '/song', 'w')

for i in range(verse1):
    song.write(lines[random.randint(0, len(lines) - 1)])
song.write(refrain_str)

for i in range(verse2):
    song.write(lines[random.randint(0, len(lines) - 1)])
song.write(refrain_str)

for i in range(verse3):
    song.write(lines[random.randint(0, len(lines) - 1)])
song.write(refrain_str)
song.close