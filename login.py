import os
import time
import qrcode
from tqdm import tqdm
while True:
	def ired(msg):
		input(f"\033[5;49;91m{msg}\033[m")
	def igreen(msg):
		input(f"\033[5;49;92m{msg}\033[m")
	def iyellw(msg):
		input(f"\033[5;49;93m{msg}\033[m")
	def idarkblue(msg):
		input(f"\033[5;49;94m{msg}\033[m")
	def iblue(msg):
		input(f"\033[5;49;96m{msg}\033[m")
	def irose(msg):
		input(f"\033[5;49;95m{msg}\033[m")
	def red(msg):
		print(f"\033[5;49;91m{msg}\033[m")
	def green(msg):
		print(f"\033[5;49;92m{msg}\033[m")
	def darkblue(msg):
		print(f"\033[5;49;94m{msg}\033[m")
	def yellw(msg):
		print(f"\033[5;49;93m{msg}\033[m")
	def rose(msg):
		print(f"\033[5;49;95m{msg}\033[m")
	def blue(msg):
		print(f"\033[5;49;96m{msg}\033[m")
	def no(msgu):
		print(f"\033[7;49;34m{msgu}\033[m")
	def clear():
		os.system("clear")
	def s():
		time.sleep(0.5)
	def void():
		print("")
	for i in tqdm(range(5)):
		time.sleep(0.3)
	clear()
	ser = "1"
	arq = open("/data/data/com.termux/files/home/chapter4/image.txt", "r")
	green(arq.read())
	resp = input(" >")
	if(resp == ser):
		clear()
		ark = open("/data/data/com.termux/files/home/chapter4/publi.txt", "r")
		green(ark.read())
		respk = input(" >")
		serk = "2"
		if(respk == serk):
			kuj = open("/data/data/com.termux/files/home/chapter4/comen.txt", "r")
			green(kuj.read())
			input()
			green(ark.read())
			correct = "rNFTGDxGE#xXaceu$=(["
			rrews = input(" >")
			if(rrews == correct):
				norvile = open("/data/data/com.termux/files/home/chapter4/curt.txt", "r")
				print(norvile.read())
				break
			else:
				s()
				print("invalid request!!")
				continue
		else:
			s()
			print("invalid request!!")
			continue
	else:
		s()
		print("invalid request!")
		continue
