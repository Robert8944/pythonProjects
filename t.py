#!/usr/sbin/python
import random,sys,tty
letters = ["a","s","d","f","j","k","l",";","g","h"]

def getCh(prompt=""):
	print(prompt)
	tty.setraw(sys.stdin.fileno())
	ch = sys.stdin.read(1)
	return ch

def main():
	while True:
		i = int(random.random()*len(letters))
		x = input(letters[i])
		while(x != letters[i]):
			x = getCh(letters[i])
			if(x == "q"):
				return

main()
