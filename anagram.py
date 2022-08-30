a=input("enter the word or letters")
b=input("enter the word or letters")
if(sorted(a)==sorted(b)):
    print(a,'and',b,'are anagram')
else:
    print("not a anagram")
