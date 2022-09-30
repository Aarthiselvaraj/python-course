a=input("enter the word:")
reverse = ''
for i in range(len(a), 0, -1):
   reverse += a[i-1]
print('The reverse string is', reverse)
