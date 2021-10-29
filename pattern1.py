def triangle(n):
    k=n-1
    for i in range(0,n):
        k=k-1
        for i in range(0,i+1):
            print("*",end=" ")
        print("\r")
n=10
triangle(n)
