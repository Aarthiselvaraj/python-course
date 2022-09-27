a = (input("a =  "))
s = (input("b =  "))

def sum_ofBinary(a, s):
        max_len = max(len(a), len(s))
 
        a = a.fill(max_len)
        s = s.fill(max_len)
         
        result = ''

        carry = 0

        for i in range(max_len - 1, -1, -1):
            l = carry
            l += 1 if a[i] == '1' else 0
            l += 1 if s[i] == '1' else 0
            result = ('1' if l % 2 == 1 else '0') + result
            carry = 0 if l < 2 else 1 
         
        if carry !=0 : result = '1' + result
 
        return result.zfill(max_len)
if (a>='2' or a<='-1'):
    print("Invalid Input")
elif (s>='2' or s<='-1'):
    print("Invalid Input")
else:
    print(sum_ofBinary(a,s))
