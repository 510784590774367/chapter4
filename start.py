import os
import time
import qrcode
from tqdm import tqdm
while True:
	def red(msg):
		input(f"\033[5;49;91m{msg}\033[m")
	def green(mkg):
		input(f"\033[5;49;92m{mkg}\033[m")
	def yellw(msgg):
		input(f"\033[5;49;93m{msgg}\033[m")
	def darkblue(msggu):
		input(f"\033[5;49;94m{msggu}\033[m")
	def no(msgu):
		print(f"\033[7;49;34m{msgu}\033[m")
	def clear():
		os.system("clear")
	def s():
		time.sleep(0.5)
	def void():
		print("")
	clear()
	for i in tqdm(range(5)):
		s()
	void()
	print("\033[5;49;96m Digite seu login: 8111.233.422\033[m")
	void()
	sec = "chapter4"
	resp = input("Digite sua senha: ")
	if(resp == sec):
		void()
		green("LOGADO COM SUCESSO!!")
		os.system("python login.py")
		break
	else:
		void()
		red("esqueceu a senha?aperte enter: ")
		void()
		yellw("resolva esse enigma e digite sua senha logo após: ")
		void()
		yellw(
		"1 2 3 4 6 7 8 9 11 12 13 14 15"
		"16 17 18 19 20 21 22 23 24 25"
		"27 28 29 30 31 32 33 34 36 37 38"
		"39 40 41 42 44 46 47 48 49 50"
		"51 52 53 54 55 56 57 58 59 60 61"
		"62 63 64 65 67 68 69 70 71 72 73"
		"74 75 76 78 79 80 81 82 83 84 85"
		"86 87 88 89 91 92 93 94 95 96 97"
		"98 99 100 101 102 103 104 105 106"
		)
		input()
		sim = "s"
		nao = "n"
		numbers = "510354543667790"
		respk = input("quais são os números que faltam?(tudo junto): ")
		if(respk == numbers):
			input("CERTISSÍMO!")
			void()
			os.system("python login.py")
			break
		else:
			clear()
			void()
			yellw("resolva esse enigma e digite sua senha logo após: ")
			void()
			yellw(
	                "1 2 3 4 6 7 8 9 11 12 13 14 15"
	                "16 17 18 19 20 21 22 23 24 25"
        	        "27 28 29 30 31 32 33 34 36 37 38"
	                "39 40 41 42 43 44 45 46 47 48 50"
	                "51 52 53 54 55 56 57 58 59 60 61"
	                "62 63 64 65 67 68 69 70 71 72 73"
	                "74 75 76 78 79 80 81 82 83 84 85"
	                "86 87 89 90 91 92 93 94 95 96 97"
	                "98 99 100 101 102 103 104 105 106"
	                )
			input()
			os.system("python start.py")
			break
