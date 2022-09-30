rows=int(input("Enter the number of row:"))
if (rows<=0 ):
     print("invalid input")
else:
    for i in range(rows+1):
        for j in range(1,i+1):
            print(j/10,end=" ")
        print("\n")
