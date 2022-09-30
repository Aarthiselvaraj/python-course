a=int(input("enter the no.total users:"))
r=int(input("enter the no.staff users:"))
s=r//3
r+=s
student_user=a-r
if a<=0:
 print("invalid input")

else:
    print("student user: ",student_user)
