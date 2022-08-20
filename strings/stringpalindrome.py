str1 = "lyryl"
str2 = ""
tmp = len(str1) - 1
while tmp >= 0:
    str2 += str1[tmp]
    tmp -= 1
#print(str2)
if str2 == str1:
    print(str1 + " is a palindrome")
else:
    print(str1 + " is not a palindrome")