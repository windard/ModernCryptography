# coding=utf-8

text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("names.txt") as n:
	names = eval("["+n.read()+"]")

score = 0

names.sort()

for i,x in enumerate(names):
	score += (i+1)*(sum([text.index(y)+1 for y in x]))	

print score