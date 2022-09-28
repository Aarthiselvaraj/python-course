P=float(input("enter the principle amount:"))
R=10
T=float(input("enter the time given:"))
S=(input("enter wheather the customer is senior citizen(yes/no):"))
def Simple_interest(P,R,T,S):
  Si=(P*R*T)/100
  if(S=="yes"):
     R=12
     print("the simple interest is:",Si)
  elif(P<0):
     print("invalid input")
  elif(T<0):
     print("invalid input")
  else:
     R=10
     print("the simple interest is:",Si)
Simple_interest(P,R,T,S)


