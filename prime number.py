l=int(input("Enter the lower value: "))
g=int(input("Enter the greater value: "))
for n in range(l,g+1):
    if n>2:
        for i in range(2,int(n/2)+1):
            if (n%i)==0:
                print("Not Prime number: ",n)
                break
            else:
                print("Prime number: ",n)
    else:
        print("not prime number: ",n)
