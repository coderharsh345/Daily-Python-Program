l=[eval(x) for x in input("Enter the array: " ).split(',')]
print(l)
e=eval(input("Enter the number to check which was repeated: "))
i=0
while i<len(l):
    if[i]==e:
        print(i,end=' ')
        i+=1
