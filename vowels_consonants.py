string = input('Enter the String: ')
print('Vowels: ')
for i in string:
   if( i in "AEIOUaeiou"):
      print(i,end=' , ')
print('\nConsonants:')
for i in string:
   if (i not in "AEIOUaeiou "):
      print(i,end=' , ')

