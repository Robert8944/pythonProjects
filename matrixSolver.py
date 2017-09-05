#!/usr/sbin/python
am = []
def main():
	global am
	correct = "n";
	while(correct.lower() != "y"):
		rowNum = int(input("Number of rows? "))
		colNum = int(input("Number of cols?(include augment) "))
		for i in range(0,rowNum):
			row = []
			for j in range(0,colNum):
				newNum = int(input())
				row.append(newNum)
			am.append(row)
		dispMatrix()
		correct = input("Correct?(Y/n) ")
		if(correct == ""):
			correct = "y"
	ans = 0
	while(ans != "q"):
		ans = input("What do you want to do?\n 1)display the matrix\n 2)row interchange\n 3)row scale\n 4)row replace\n 5)find RREF step by step\n q)quit\n")
		if(ans == "1"):
			dispMatrix()
		if(ans == "2"):
			r1 = int(input("first row? "))
			r2 = int(input("second row? "))
			rowInterchange(r1,r2)
		if(ans == "3"):
			r = int(input("row to scale? "))
			s = float(input("scale factor? "))
			rowScale(r,s)
		if(ans == "4"):
			r1 = int(input("row to be replaced? "))
			r2 = int(input("row to be scaled and added? "))
			s = float(input("scale factor? "))
			rowReplace(r1,r2,s)
		if(ans == "5"):
			rref()

def rref():
	submatrix = am
	rrefHelper(submatrix)

def rrefHelper(matrix):
	#check if submatrix is done
	if(len(matrix)==1):
		#do second half of steps
		return
	#find leftmost non-zero entry
	pivotCol = 0
	pivotRow = 0
	for colNum in range(0,len(matrix[0])):
		for rowNum in range(0,len(matrix)):
			if(matrix[rowNum][0] != 0):
				pivotRow = rowNum
				pivotCol = colNum
	#if necessary interchange rows to make the pivot position in the top row
	if (pivotRow != 0):
		rowInterchange(1,pivotRow+1)
	#use elementary row operations to create zeros in the coloum entries below pivot
	for rowNum in range(1,len(matrix)):
		if(matrix[rowNum][0] != 0):
			rowReplace(rowNum+1,1,-1*matrix[rowNum][0]/matrix[0][0])
	#repeat steps above for submatrix
	submatrix = [[]]
	for rowNum in range(1,len(matrix)):
		row = []
		for colNum in range(1,len(matrix[0])):
			row.append(matrix[rowNum][colNum])
		submatrix.append(row)
	rreftHelper(submatrix)

	
####
# 
# display the matrix
# 
####
def dispMatrix():
	longest = 0
	for row in am:
		for num in row:
			if(len(str(num))>longest):
				longest = len(str(num))	
	for row in am:
		print("|",end="")
		for num in row:
			for spaces in range(0,longest-len(str(num))):
				print(" ",end="")
			print(str(num)+" ",end="")
		print("|")
####
# 
# interchange two of the rows. row inputs expect numbering starting at 1
# 
####
def rowInterchange(r1,r2):
	am[r1-1],am[r2-1] = am[r2-1],am[r1-1]
####
# 
# scale the row by the scale factor. row inputs expect numbering starting at 1
# 
####
def rowScale(r,s):
	am[r-1] = [num*s for num in am[r-1]]
####
# 
# scale the second row by the scale factor and add it the the first row.
# the first row will be replaced with the result
# row inputs expect numbering starting at 1
# 
####
def rowReplace(r1,r2,s):
	am[r1-1] = [am[r1-1][i] + am[r2-1][i]*s for i in range(0,len(am[r1-1]))]

main()
