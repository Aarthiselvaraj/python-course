print("Enter the number -1 to stop____")
s=[]
a=[]
while True:
    r=int(input("Enter the number "))
    if(r==-1):
        break
    if(r>0):
        s.append(r)
    else:
        a.append(r)

aarthi=(sum(s)/len(s))
aarthi=(sum(a)/len(a))
print("The average of negative number is: ",aarthi)
print("The average of positive number is: ",aarthi)
