"""
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

# n = 20

# for i in range(1, 1000000000):
# 	for j in range(2, n+1):
# 		if i%j == 0:
# 			if j == n:
# 				print(i)
# 			continue
# 		else:
# 			break


def findsprimes(n):
    primes = [2]
    for i in range(3,n+1):
        for j in primes:
            if(j == primes[len(primes)-1]):
                primes = primes + [i]
            if(i%j == 0):
                break
            else:
                continue
    return primes

def findfactors(n):
    primes = findsprimes(n)
    factors = []
    for i in range(n):
        for j in range(i,n):
            if(i * j == n):
                if(i not in primes):
                    if(j not in primes):
                        factors = findfactors(i) + findfactors(j)
                    else:
                        
                        factors = [j] + findfactors(i)
                    
                else:
                    if( j not in primes):
                        if(i not in primes):
                            factors = findfactors(i) + findfactors(j)
                        else:
                            
                            factors = [i] + findfactors(j)
                    else:
                        factors = [i,j]
                    
                break
    if(n in primes):
        factors = [n]
    return factors
    
def findsmallest(n):
    primes = findsprimes(n)
    primesnum = [0] * len(primes) 
    allzefac = []
    for i in range(n+1):
        allzefac = allzefac + [findfactors(i)]
    for i in primes:
        for j in allzefac:
            if(j.count(i) > primesnum[primes.index(i)]):
                primesnum[primes.index(i)] = j.count(i)
    
    summy = 1
    for i in  range(len(primes)):
        if primesnum[i] != 0:
            summy = summy * primes[i] ** primesnum[i]
    return summy


n = 20
print(findsmallest(n))