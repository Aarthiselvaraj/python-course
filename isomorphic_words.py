str1,str2=(str(input("Enter the first string s=")),(input("Enter the second string t=")))
def isisomorphic(str1, str2):
    if len(str1)!= len(str2):
        return False
    else:
        map1,map2 = {},{}
        for i in range(len(str1)):
            char1, char2 = str1[i], str2[i]
            if char1 not in map1:
                map1[char1] = char2
            if char2 not in map2:
                map2[char2] = char1
            if map1[char1] != char2 or map2[char2]!= char1:
                return False
    return True
print(isisomorphic(str1, str2))
