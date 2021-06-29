import random
import timeit
import matplotlib.pyplot as plt
import math
def mergeSort(A):
	if len(A)>1:
		mid=int(len(A)/2)
		L=A[:mid]
		R=A[mid:]
		mergeSort(L)
		mergeSort(R)
		merge(A,L,R)
def merge(A,L,R):
	i = j = k = 0
	while i < len(L) and j < len(R):
		global comp
		if L[i] < R[j]:
			comp=comp+1
			A[k] = L[i]
			i += 1
		else:
			comp=comp+1
			A[k] = R[j]
			j += 1
		k += 1
	while i < len(L):
		A[k] = L[i]
		i += 1
		k += 1
	while j < len(R):
		A[k] = R[j]
		j += 1
		k += 1
timeList=[]
compList=[]

for p in range(200):
	comp=1
	A = []
	for i in range(0,p):
		n = random.randint(1,100)
		A.append(n)
	mergeSort(A)
	compList.append(comp)
n = [*range(1, 201, 1)]
nn=[]
for x in n:
		nn.append(x*math.log(x,2))
plt.plot(compList,n,color='green', linewidth=3,label='Mergesort time')
plt.plot(nn,n,color='red', linewidth=3,label='nlogn')
plt.title('Merge Sort Running ime')
plt.xlabel('value of time')
plt.ylabel('value of n')
plt.legend()
plt.show()