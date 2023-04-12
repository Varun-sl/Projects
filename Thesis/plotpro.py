import matplotlib.pyplot as plt
import numpy as np
import time

x = []
y = []
timing=[]
carstrength=[]
pitime=[]
datasize=[]
difflist=[]


with open('DataLog.txt','r') as f:
	data=f.readlines()
	#x=data.split(':')
	#print(x)
	i=0
	for line in data:
		y=line.split(':')
		if (y[0] not in x)and(y[0]!=""):
			x.append(y[0])
		z=y[8]
		b=y[11]
		m=z.split(" ")
		n=b.split(" ")
		timing.append(m[1])
		carstrength.append(len(x))
		pitime.append(n[0])
		diff=int(n[0])-int(m[1])
		difflist.append(diff)
		datasize.append(i)
		i=i+1
		print(y)
	#while(i<=len(data)):
	#	k=y[i]
	#	if (k[0] not in x)and(k[0]!=""):
	#		x.append(k[0])
	#	z=k[8]
		#print(x)
	#	m=z.split(" ");
	#	timing.append(k[1])
	#	carstrength.append(len(x))
	#	i=i+1
		
print(carstrength)
print(timing)
print(pitime)
plt.plot(timing,carstrength)
plt.ylabel('number of cars')
plt.xlabel('time in seconds')
plt.show()
plt.close()
plt.plot(datasize,difflist)
plt.xlabel('number of data points')
plt.ylabel(' difference in time(seconds)')
plt.show()
		#time.sleep(1)
