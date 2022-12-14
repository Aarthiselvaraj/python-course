def maxProfit(amount,a):
 
    
    profit = [0]*a
    max_amount = amount[a-1]
 
    for i in range(a-2, 0, -1):
 
        if amount[i] > max_amount:
            max_amount= amount[i]
 

        profit[i] = max(profit[i+1], max_amount - amount[i])
 
    min_amount = amount[0]
 
    for i in range(1, a):
 
        if amount[i] < min_amount:
            min_amount = amount[i]
 
        profit[i] = max(profit[i-1], profit[i]+(amount[i]-min_amount))
 
    result = profit[a-1]
 
    return result
 
 

amount = []
b=int(input("Enter the numbers:"))
for i in range(0,b):
    aa=int(input())
    amount.append(aa)
print(amount)
print ("Maximum profit is", maxProfit(amount, len(amount)))
