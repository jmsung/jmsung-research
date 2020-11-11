import numpy as np

def fib(a,b):
    return a+b


def prime_factor(x):
	""" Return the prime factor of input x """
	pf = set()
	while x > 1:
		for i in range(2,x+1):
			if x%i == 0:
				x = int(x/i)
				pf.add(i)
				break
	sorted_pf = sorted(pf)				

	return sorted_pf

def is_prime(n):
	""" Return whether the input n is primer number or not"""
	for i in range(2,n):
		if n%i == 0:
			return False
	return True


def prime_below1(n):
	""" Return prime numbers below n

	Parameters
	----------
	n: int
		Input value

	Return
	------
	primes: list
		List of prime values below n
	"""
	n = int(n)

	primes = [2]

	for i in range(3, n, 2):
		if sum([i%prime==0 for prime in primes]) > 0:
			continue
		if is_prime(i):
			primes.append(i)

	return primes

def prime_below2(n):
	""" Return prime numbers below n

	Parameters
	----------
	n: int
		Input value

	Return
	------
	primes: list
		List of prime values below n
	"""
	n = int(n)

	primes_true = []
	primes_test = [2]
	primes_test.extend([i for i in range(3, n, 2)])

	while len(primes_test)>0:
		value = primes_test[0]
		if is_prime(value):
			primes_true.append(value)
			prime_test.remove()




	return primes	