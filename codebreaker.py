#!/usr/bin/python
import sys,time
x=input("Welcome to my trap! Do you know how to read code?\n")
if(x!="Of course I do!"):
	print("You've failed to disarm my trap! Your servers are now compromised.")
	sys.exit(0)
print("Congratulations! That's SOOOOOOOO impressive, you read an if statement. Try this on or size")
x=input("What is the area of a circle with radius 1?\n")
if(not(x=="pi" or x=="3.14")):
	print("You can't even do simple math! Now your servers are surely doomed!\n")
	sys.exit(0)
print("Clever one.",flush=True)
time.sleep(.5)
print("Hmmmmmm.",end="",flush=True)
time.sleep(.5)
print(".",end="",flush=True)
time.sleep(.5)
print(".",end="",flush=True)
time.sleep(.5)
print(".",end="",flush=True)
x=input(" I bet you can't read the math in my code!\nX=")
if(x!=str(13+20-7-7+2*5)):
	print("Was that math too hard? Better luck next time!\n")
	sys.exit(0)
print("Wow! You are hard to trick!")
x=input("Ok, now it's time to really test your limits:\n")
counting = 10
while(int(x)==counting):
	x=input("")
	counting=counting-1
	if(counting==0):
		print("You did it! The world is safe from harm.")
		break
if(int(x)!=counting):
	print("Bwa-Haha! You'll never beat me!")
