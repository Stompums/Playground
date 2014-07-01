
#!/usr/bin/env python
"""
What's the sum of the last ten digits of the product of the set of primes less than ten thousand?
"""

import divisor

prime_king = divisor.primes(10000)
product = 1
for i in prime_king:
	product = product*i
	if product >1e10:
		product = product%int(1e10)

print sum([int(business) for business in str(product)])
