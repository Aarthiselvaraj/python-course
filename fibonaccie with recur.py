def fibonaccie_recur(n):
    if(n<=1):
        return 1
    else:
        return(fibonaccie_recur(n-1)+fibonaccie_recur(n-2))
num=int(input("enter the number:"))
print('fibonaccie series:')
for i in range(num):
    print(fibonaccie_recur(i))
    
