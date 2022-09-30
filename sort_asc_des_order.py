Aarthi =[]
aa= int(input("Enter the number of names to be printed : "))
d= str(input("Enter the Order (A/D): "))
for i in range(aa):
    s= input(" ")
    Aarthi.append(s)
Aarthi.sort()
if (d == 'A'):
    for i in Aarthi:
        print(i)
else:
    Aarthi.sort(reverse=True)
    for i in Aarthi:
     print(i)
