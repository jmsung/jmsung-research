# problem_004.py
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

palindromic = []

for i in range(999, 0, -1):
	for j in range(999, 0, -1):
		x = int(i*j)
		y = int(str(x)[::-1])
		# print('x={}, y={}'.format(x, y))
		if x==y:
			palindromic.append(x)
			# print(x)

palindromic.sort(reverse=True)
print(palindromic[0])

