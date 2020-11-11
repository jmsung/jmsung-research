"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from scripts import myfunc

n = 2e6

primes = myfunc.prime_below(n)

print(primes)
print(sum(primes))




