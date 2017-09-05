#!/usr/bin/python
import random
grid = [[0 for x in range(9)] for y in range(9)]
coords = [[[0 for x in range(2)] for y in range(9)] for z in range(9)]
for i in range(81):
	coords[int(i/9)][i%9] = [i%9,int(i/9)]
print(str(coords))
#[x or y][rows or cols][row or col pos for 1, 2, and 3]
def threeRandomNumbers():
	ans = [[[0,1,2],[0,1,2],[0,1,2]],[[0,1,2],[0,1,2],[0,1,2]]]
	random.shuffle(ans[0][0])
	random.shuffle(ans[0][1])
	random.shuffle(ans[0][2])
	random.shuffle(ans[1][0])
	random.shuffle(ans[1][1])
	random.shuffle(ans[1][2])
	return ans

def getGrid():
	ans = ""
	for i in range(9):
		if i%3 == 0:
			ans += "+-------+-------+-------+\n"
		for j in range(3):
			ans += "| "
			for k in range(3):	
				ans += str(grid[i][j*3+k]) + " "
		ans+="|\n"
	ans += "+-------+-------+-------+\n"	
	return ans

def fillGrid():
	nums = threeRandomNumbers()
	print("coords for 1:")
	for i in range(9):
		print("\t(" + str(nums[0][i][0])+","+str(nums[1][i][0])+")")

def checkSpot(y, x):
	for i in range(9):
		if x!=i and grid[y][x] == grid[y][i]:
			return False
	for i in range(9):
		if y!=i and grid[y][x] == grid[i][x]:
			return False
	for i in range(3):
		for j in range(3):
			if x!=i+int(x/3) and y!=j+int(y/3) and grid[y][x] == grid[j+int(y/3)][i+int(x/3)]:
				return False
	return True

def main():
	fillGrid()
	print(getGrid())

main()
