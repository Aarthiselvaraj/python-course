def sqrSumEvenNSumOdd(s):
    odd = 0
    even = 0
    for i in s:
        if (i%2 ==0):
            even = even+i**2
        else:
            odd = odd+i**2
    s=[odd,even]
    return s
s=[]
a= int(input("Enter the number of element: "))
if a <= 0:
      print("Invalid Input")
    
for i in range(a):
    if a <0:
      print("Invalid Input")
    aarthi = int(input("Enter the element: "))
    s.append(aarthi)
print(sqrSumEvenNSumOdd(s))
