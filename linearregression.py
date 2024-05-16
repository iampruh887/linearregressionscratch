import numpy as np
def findindex(List, val) -> int:
	ctr = 0
	val = val.replace(" ", "")
	for i in List:
		if i.lower() == val.lower():
			return ctr
		ctr+=1
def readfile(filename) -> tuple:

	"""
		function to read the file and 
		return it as a list
	"""
	file = open(filename, "r")
	List = []
	for i in file:
		List.append([i])
	ctr = 0
	for i in List:
		tempstr = ""
		temp = "" 
		for j in i:
			temp += j
		for j in temp:
			if j == '\n':
				break
			tempstr += j
		List[ctr] = tempstr
		ctr += 1

	OrigList = []
	strn = ""

	for j in List:
		tempList = []
		temp = ""
		for k in j:
			strn += k
		ctr = 0
		strn = strn.replace(" ", "")
		for i in strn:
			if i != ',':
				temp += i
			if i == ',':
				tempList.append(temp)
				temp = "" 
			if i == strn[len(strn) - 1] and ctr == len(strn) - 1:
				tempList.append(temp)
				OrigList.append(tempList)
			ctr += 1
		strn = ""

	titles = OrigList[0]	
	print(titles)
	ct = 0
	del OrigList[0]
	tempOrigList = []

	for i in OrigList:
		temp = []
		for j in i:
			temp.append(np.int64(j))
		tempOrigList.append(temp)
	OrigList = np.array(tempOrigList)
	# obtained all values in a vector format		
	return (OrigList, titles)
output = readfile("tested.csv")
values= output[0]
titles = output[1]

