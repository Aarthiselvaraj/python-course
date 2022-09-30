a=input("enter the character to be printed:")
rows = int(input("enter the no.of rows:"))
if(rows<=0):
     print("INVALID INPUT")
     
for i in range(0, rows):
    for j in range(0, i + 1):
        print(a, end=' ')
    print("\n")
   
