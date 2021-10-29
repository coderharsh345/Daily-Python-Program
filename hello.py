import cmath
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
d=((b**2)-(4*a*c))
e=(cmath.sqrt(d))
x1=((-b+e)/(2*a))
x2=((-b-e)/(2*a))
print("First value is",x1,"\tSecond Value is",x2)
