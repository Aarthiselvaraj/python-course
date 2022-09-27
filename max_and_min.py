aa = []
s= int(input("Enter the number of elements : "))
for i in range (1,s+1):
    sa = int(input("Enter the element : "))
    aa.append(sa)
aa.sort()
print(aa)
g= int(input("M = "))
if( g>=s+1):
    print("Invalid input")
l = int(input("N = "))
if(l >=s+1):
    print("Invalid input")
if(g == 1):
    print("The ", g ,"Maximum Value: ",aa[-(g)])
else:
    print("The ", l,"Maximum number: ",aa[g-l])
print("The",l, "Minimum number : ",aa[l-1])
Sum = aa[g-1] +aa[l-1]
Diff = aa[g-1] -aa[l-1]
print("The sum of minimum and maximum number is ",Sum)
print("The difference between minimum and maximum number is ",Diff)
