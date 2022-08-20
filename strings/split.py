string1 = "This is a sample"
print(string1.split())
print(string1.split(' '))
str2 = "IAMADITYA"
print(str2.split('A'))
print(string1.split('s'))
print(str2.split('I'))
#This removes the character/s we want to, from the string and returns a list with each word as an element. However if
#                       the given character/s is at the beginning or end of a line, it appends a blank element into
#                       the list.And if no argument is given, it  takes ' ' as the argumrnt