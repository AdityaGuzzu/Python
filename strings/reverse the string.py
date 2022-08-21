str1 = "Hello"
str2 = ""
tmp = len(str1) - 1
while tmp >= 0:
 #string is just a char array so we can use str2[tmp]
 str2 += str1[tmp]
 tmp -=1
print(str2)
#for i in str1:
 #   print (i)