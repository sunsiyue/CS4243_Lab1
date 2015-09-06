import numpy as np
import numpy.linalg as la

file = open("data.txt")
data = np.genfromtxt(file, delimiter=",")
file.close()

print "data=\n", data

dataRows = len(data[:,0])
print dataRows
m = np.matrix(np.zeros([dataRows*2,6]))
b = np.matrix(np.zeros([dataRows*2,1]))

for i in range(dataRows):
	for j in range(4):
		if j<2:
			b[2*i+j, 0]=data[i, j]
		else:
			m[2*i, j-2]=data[i,j]
			m[2*i+1, j+1]=data[i,j]
			m[2*i, 2]=m[2*i+1, 5]=1


print "M=\n", m
print "b=\n", b

a,e,r,s=la.lstsq(m,b)
print "a=\n", a
print "sum squared error = \n", pow(la.norm(m*a-b), 2)
print "residue=\n", e



