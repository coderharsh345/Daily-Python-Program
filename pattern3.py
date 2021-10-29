for i in range(1,8):
    for j in range(1,8):
        if ((i+j)==5 or (j-i)==3 or (i-j)==3 or (i+j)==11 or i==4 or j==4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("\n")
