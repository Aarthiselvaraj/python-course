from math import factorial
s = int(input("Enter a number of rows:"))
a=int(input("Enter the row number"))
if(s>0):
    for i in range(s):
        for j in range(s-i+1):
            print(end=" ")
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
        print()
    if(a>0):
        m=0
        for i in range(s):
            for j in range(i+1):
                if(i==a-1):
                    m+=factorial(i)//(factorial(j)*factorial(i-j))
        print("Sum of numbers:",m)
    else:
        print("INVALID INPUT")
else:
    print("INVALID INPUT")
