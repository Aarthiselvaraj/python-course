a=input("enter the number")
reverse = ''
for i in range(len(a), 0, -1):
   reverse += a[i-1]
print('The reversed number is', reverse)
