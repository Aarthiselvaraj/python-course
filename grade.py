print("enter the marks got in each subject")
print("maths:")
maths=int(input())
print("bio:")
bio=int(input())
print("eng:")
eng=int(input())
total=maths+bio+eng
avg=total/3
if avg>90 and avg<100:
    print("grade A")
elif avg>80 and avg<90:
    print("grade B")
elif avg>70 and avg<80:
    print("grade C")
else:
    print("grade D")
    
