import math as m

def isPrime(x):
	for i in range(2,int(m.sqrt(x)),1):
		if x%i==0:
			return False
	return True