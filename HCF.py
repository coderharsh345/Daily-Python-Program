def HCF_nikal(a,b):
    """
     tera bhai HCf nikal kr dega
     """
    smaller=b if a>b else a
    hcf=1
    for i in range(1,smaller+1):
        if(a%i==0)and (b%i==0):
            hcf=i
    return hcf
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
print("HCF of",n1,"&",n2,"is",HCF_nikal(n1,n2))
