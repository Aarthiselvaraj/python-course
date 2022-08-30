n=input("enter any word:")
vowels=('a,i,e,o,u')
count=0
for i in n:
    if i in vowels:
        count+=1
print("the number of vowels",count)    
