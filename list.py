number=[]
num=int(input('Enter How many numbers you entered: '))
for n in range(num):
    n=int(input())
    number.append(n)
print("Unsortes List:",number)
length=len(number)
number.sort()
print("Largset value: ",number[length-1])
print("Second Largest value: ",number[length-2])
print("Smallest value: ",number[0])
print("Second Smallest value: ",number[1])
