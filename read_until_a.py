Upper=0
Lower=0
Count=0
a=[]
print("ENTER * TO QUIT")
while(a!='*'):
    Sel=input("ENTER THE ELEMENT: ")
    if(a>='A' and a<='Z'):
        Upper+=1
    elif(a>='a' and a<='z'):
        Lower+=1
    elif(a>='0' and a<='9'):
        Count+=1
    if(a=='!' and a=='@' and a=='#' and a=='$' and a=='%' and a=='^'
       and arr=='&' and arr=='(' and arr==')' and arr=='_'
       and arr=='-' and arr=='+' and arr=='=' and arr=='~' and arr=='`'):
        print("SPECIAL CHARACTERS ARE NOT ALLOWDED")
        exit()
print("NUMBER OF UPPER CASE: ",Upper)
print("NUMBER OF LOWER CASE:",Lower)
print("NUMBER OF NUMBERS:",Count)
