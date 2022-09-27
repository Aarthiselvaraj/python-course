def MaxArea(a, Len) :
    Area = 0
    for i in range(Len) :
        for j in range(i + 1, Len) :
           

            Area = max(Area, min(a[j], a[i]) * (j - i))
    return Area
 
a = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    s = int(input())
    a.append(s)
print(a)
len1 = len(a)
print(MaxArea(a, len1))
