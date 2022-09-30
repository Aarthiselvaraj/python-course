age=int(input("enter your age:"))
if(age>=18):
    print("the person is  elligible for vote")
elif(age<18):
    print("the person is not elligible for vote")
    print("the person can vote after",18-age,"years")
else:
    print("INVALID INPUT")
