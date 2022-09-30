def Match_Position(str1,str2):
	a=str1.replace('  ',' ')
	s=str2.replace('  ',' ')
	if(len(a)<len(s)):
		length=len(a)
	else:
		length=len(s)
	count=0
	for i in range(length):
		if(a[i]!=s[i]):
			count=count+1
	print(length-count)
str1=str(input("s1 = "))
str2=str(input("s2 = "))
Match_Position(str1,str2)
