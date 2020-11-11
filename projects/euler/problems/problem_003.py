"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""


from scripts import myfunc
import time
start_time = time.time()

x = 600851475143

y = myfunc.prime_factor(x)

print(y)

print(time.time() - start_time)
