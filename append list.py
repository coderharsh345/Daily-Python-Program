lis=[]
print("Enter the 10 numbers: ")
for i in range(10):
    i=int(input())
    lis.append(i)
print(lis)
length=len(lis)
index=1
for index in range(length-1):
    if lis[index]<lis[index+1]:
        if lis[index]>lis[index-1]:
            print('Element: ',lis[index])

