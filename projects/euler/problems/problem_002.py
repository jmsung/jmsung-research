"""
Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.
"""

from scripts import myfunc

fib_seq = [1, 2]
max_seq = 4*1e6

for i in range(1000):
	x = fib_seq[-1]+fib_seq[-2]
	if x <= max_seq:
		fib_seq.append(x)		
	else:
		print('Reached to %d' %(int(max_seq)))
		break


print(fib_seq[-1])

fib_even = [i for i in fib_seq if i%2 == 0]
print(sum(fib_even))


