M = int(input("A= "))
N = int(input("B= "))

for num in range(M,N+1):
    count = 0
    for divider in range(2,num//2+1):
        if num%divider == 0:
            count+=1
    if count >= 1:
        print(num)
