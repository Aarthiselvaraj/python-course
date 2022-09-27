import sys
s = int(input("n = "))
def numSquares(s) :
    visited = [0]*(s + 1)
    a= []
    ans = sys.maxsize
    a.append([s, 0])    
    visited[s] = 1
    while(len(a) > 0) :
        l = a[0]
        a.pop(0)

        if(l[0] == 0) :
            ans = min(ans, l[1])
     
        i = 1
        while i * i <= l[0] :
            Path = l[0] - i * i
            if Path >= 0 and (visited[Path] == 0 or Path == 0) :

                visited[Path] = 1 

                a.append([Path,l[1] + 1])
             
            i += 1
    return ans
 
print(numSquares(s))
