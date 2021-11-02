NUM1=[]
for i in range(1,11):
    NUM1.append(i)
print("number from 1 to 10...\n",NUM1)
for j,i in enumerate(NUM1):
    if (i%2==1):
        del NUM1[j]
    print("Thr value after removed odd number...",NUM1)