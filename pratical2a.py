def odev(a):
    if (a%2==0):
        return 1
    else:
        return 0

n=int(input("Enter the number "))    
if (odev(n)==1):
        print("The  given numver is even")
else:
        print("The  given numver is odd")