def freq(str):
    str = str.split()         
    str2 = []
    for i in str:             
        if i not in str2:
            str2.append(i)               
    for i in range(0, len(str2)):
        print('Frequency of', str2[i], 'is :', str.count(str2[i]))
str =input("Enter the You String Word: ")
s1=""
i=0
for x in str:
    if(str.index(x)==i):
        s1+=x
    i+=1
print("Word are used in string : ",s1)

