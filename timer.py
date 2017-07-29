#! python3
# are you really a duck?
# the ira just sent me a time bomb in the mail!

q = input('are you a duck? y or n \n')
if q.lower()=='n':
	print('sucks to be you')
	import os
	os.system('shutdown /s /t 30')
else:
	print('well then, welcome to the club')
input()