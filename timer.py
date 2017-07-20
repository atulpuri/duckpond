#! python3

q = input('are you a duck? y or n \n')
if q.lower()=='n':
	print('sucks to be you')
	import os
	os.system('shutdown /s /t 900')
else:
	print('well then, welcome to the club')
input()