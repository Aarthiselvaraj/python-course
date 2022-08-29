def add(x,y):
    return x+y
def subract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def devide(x,y):
    return x/y
print("select operation")
print('a.add')
print('b.subract')
print('c.multiply')
print('d.divide')
choice =input("enter the choice(a/b/c/d):")
num1=int(input("enter the first number:"))
num2=int(input("enter the scond number:"))
if choice=='a':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=='b':
    print(num1,"-",num2,"=",subract(num1,num2))
elif choice=='c':
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=='d':
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("this is an invalid input" )
