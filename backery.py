a=int(input("Enter the number of loaves purchased: "))
s=int(input("enter the number of days old loaves purchased: "))
t=185
print("REgular price: Rupees 185")
amt_new=a*t
amt_old=s*t
amt_old_discount=amt_old*(6/10)
if(a<0):
    print("Amount of new loaves: ",amt_new)
else:
    print("Amount of new loaves:",amt_new)
    print("Amount of day old loaves:\n",amt_old_discount)
    print("Total amount:",amt_new+(amt_old-amt_old_discount))
