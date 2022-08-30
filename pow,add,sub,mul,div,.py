def powe (a,s):
    return a**s
def add(a,s):
    return a+s
def sub(a,s):
    return a-s
def multiply(a,s):
    return a*s
def divide(a,s):
    return a/s
a=int(input('enter the 1st number:'))
s=int(input('enter the 2nd number:'))
powe=a**s
add=a+s
sub=a-s
multiply=a*s
divide=a/s
operator=input("enter any of this foe operation+,-,*,/,**:")
if operator=='**':
    result=a**s
elif operator=='+':
    result=a+s
elif operator=='-':
    result=a-s
elif operator=='*':
    result=a*s
elif operator=='/':
    result=a/s
else:
    print('invalid input')
print(a,operator,s,":",result)
   
