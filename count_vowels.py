Aarthi = input("Please Enter Your Own String : ")
vowels = 0
for i in Aarthi:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A'
       or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
print("Total Number of Vowels in this String = ", vowels)