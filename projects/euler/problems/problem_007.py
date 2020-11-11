"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from scripts.myfunc import is_prime

nth_prime = 10001

ith_prime = 0
x = 1

while ith_prime < nth_prime:
	x += 1
	if is_prime(x):
		ith_prime += 1

print(x)