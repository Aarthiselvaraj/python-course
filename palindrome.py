def numberPalindrome(num):
    for i in range(0,len(num)):
        if (num[i] != num[len(num)-i-1]):
            return False
    return True
num = (input("Enter the number: "))
if(numberPalindrome(num)== True):
    print(True)
else:
    print(False)
numberPalindrome(num)
