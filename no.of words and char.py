word_count=1
char_count=0
string=input('enter a string:')
split_string=string.split()
word_count=len(split_string)
for word in split_string:
    char_count+=len(word)
print("number of words:",word_count)
print("number of characters",char_count)
