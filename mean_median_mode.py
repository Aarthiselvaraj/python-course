a=[]
g=int(input("enter the number of elements : "))
for i in range(g):
    s=float(input("enter the elements:"))
a.append(s)
def getMean(a):
    a.sort()
    sum=0
    for i in a:
        sum=sum+i
        r=sum/len(a)
        return round(r)
print("MEAN = ",getMean(a))
def getMedian(a):
    a.sort()
    if len(a)%2!=0:
        return a[len(a)//2]
    else:
        median1=a[len(a)//2]
        median2=a[len(a)//2-1]
        return((median1+median2)/2)
print("MEDIAN = ",getMedian(a))
def getMode(a):
    mode= sorted(set(a),key= a.count,reverse = True)
    Max_Mode = a.count(mode[0])
    Result_Mode =[]
    for i in mode:
        if a.count(i)<Max_Mode:
            break
        Result_Mode.append(i)
    return sorted(Result_Mode)
print("MODE= ",getMode(a))
