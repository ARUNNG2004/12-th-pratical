odd=set([x for x in range(1,10,2)])
primes=odd
for num in range(10):
	if (num>1==0):
		for i in range(2,num):
			if(num%i==0):
				break
			else:


				primes.add(i)
print("odd Numbers: ", odd)
print("Prime Numbers: ", primes)
print("Union: ", odd.union(primes))
print("Intersection: ", odd.intersection(primes))
print("Difference: ", odd.difference(primes))
print("Symmetric Difference: ", odd.symmetric_difference(primes))