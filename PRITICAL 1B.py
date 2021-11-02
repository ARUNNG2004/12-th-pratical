n=int(input("Enter the number "))
s=0.0
for i in range(1,n+1):
    a=float(i**i)/i
    s=s+a
print("the sumof the series",s)
