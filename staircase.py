def ways(a):
    if (a<=1):
        return a
    return ways(a-1)+ways(a-2)
n = int(input("n = "))
def countways(n):
    return ways(n+1)
print ( "Number of ways: ",countways(n))

    
 
