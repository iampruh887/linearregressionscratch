import numpy as np
import math
#function to find out index
def findindex(List, val) -> int:
	ctr = 0
	for i in List:
		if i == val:
			return ctr
		ctr+=1
#data engineering stuff [ignore pls.. it will destroy you]
#at the time of writing this code, only god and I knew what it meant, 
#not only god knows what i did here.
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
	ct = 0
	invalid = []
	del OrigList[0]
	tempOrigList = []
	for i in OrigList:
		for j in i:
			if j == "":
				invalid.append(ct)
		ct+=1
	t = []
	i = 0
	while i<len(OrigList):
		if i not in invalid:
			t.append(OrigList[i])
		i+=1
	OrigList = t
	del t
	
	for i in OrigList:
		temp = []
		for j in i:
			temp.append(np.float64(j))
		tempOrigList.append(temp)
	OrigList = np.array(tempOrigList)
	# obtained all values in a vector format		
	return (OrigList, titles)
output = readfile("tested.csv")
values= output[0]
titles = output[1]
print(titles)
k = len(values)
#dividing into training and testing data
num = math.ceil(k*0.7)
i = 0
training = []
testing = []
while i<num:
	training.append(values[i])
	i+=1
i = num 
while i<k:
	testing.append(values[i])
	i+=1

X = np.array([])
Klist = training
ct = 0
X = np.array([])
for i in Klist:
		temp = np.array([np.float64(i[2]), np.float64(i[3]), np.float64(i[6])])
		if X.size == 0:
			X = temp
		else:
			X = np.vstack((X, temp))
y_hat = []
y = []
for i in training:
	y.append(np.float64(i[1]))
m = len(X)
W = np.array([])
ds = np.float64(0)
for i in range(3): 
	W = np.append(W, np.array([ds]))
alpha = 0.0001
epochs = 100000
#gradient descent
prev_cost = float('inf') 
tolerance = 0.000001
for i in range(epochs):
    f = np.dot(X, W)
    error = f - y 
    gradients = (1/float(m)) * np.dot(X.T, error)
    W = W - alpha * gradients
    J = (1/float(2*m)) * np.sum(error**2)
    #print(f"Iteration {i+1}, cost: {J}")

    # Check convergence by comparing current cost with previous cost
    if abs(J - prev_cost) < tolerance:
     #   print("Converged!")
        break

    prev_cost = J
    

#again some feature engineering and stuff, dont try to understand this plz
X = np.array([])
Klist = testing
for i in Klist:
		temp = np.array([np.float64(i[2]), np.float64(i[3]), np.float64(i[6])])
		if X.size == 0:
			X = temp
		else:
			X = np.vstack((X, temp))

y = []
for i in Klist:
	y.append(np.float64(i[1]))

n = len(X)
acc = []
for i in range(n):
	f = np.dot(X, W)
	#print(f)
	fin = float(f[i])*100
	
	g = None
	lmn = float(50)
	print(fin, lmn)
	if fin>lmn:
		g = 1
	else:
		g = 0
	if g == y[i]:
		acc.append(1)
	else:
		acc.append(0)
correct = 0
for i in acc:
	if i == 1:
		correct += 1
accuracy = (correct/float(len(acc)))*100
print(f"accuracy = {accuracy}")
#print(X, y)
