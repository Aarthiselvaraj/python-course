def FactorialnFactor(n):
    if(n==1):
        return 1
    else:
        return n*FactorialnFactor(n-1)
try:
    a=int(input("Enter the number:"))
    if(a<=0):
        print("Invalid Input")
    else:
        print("Factorial:",FactorialnFactor(a))
        b=0
        for i in range(1,a+1):
            if(a%i==0):
                b+=1
        print("Number of factors:",b)
except ValueError:
    print("Invalid Input")
