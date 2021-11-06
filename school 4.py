odd=set([x for x in range(1,10+1,2)])
primes=odd
for i in range(2,10):
	j=2
	f=0
while j<i:
	if i% j==0:
		f=1
	j+=1
if f==0:

	print("odd Numbers: ", odd)
print("Prime Numbers: ", primes)
print("Union: ", odd.union(primes))
print("Intersection: ", odd.intersection(primes))
print("Difference: ", odd.difference(primes))
print("Symmetric Difference: ", odd.symmetric_difference(primes))