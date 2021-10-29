def triangle(n):
    k=n-1
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")#giving a space to the star
        k=k-1
        for i in range(0,i+1):
            print("*",end=" ")
        print("\r")#giving the space between two lines 
n=10
triangle(n)
