import time
import math
#Efficient way to print the prime numbers.

def prime_v1(n):
	if n==1:
		return False
	max_div=math.floor(math.sqrt(n))
	for i in range(2,1+max_div):
		if n%i==0:
			return False
	return True

def prime_v2(n):
	max_div=math.floor(math.sqrt(n))
	if n==1:
		return False
	elif n==2:
		return True
	elif n>2 and n%2==0:
		return False
	else:
		for d in range(3,1+max_div,2):
			if n%d==0:
				return False
		return True


t0=time.time()
num=[]
for d in range(2,100000):
	#prime_v1(d)
	if(prime_v2(d)):
		num.append(d)
print(num)
t1=time.time()
print("Time Required : ",t1-t0)
