'''
The following should be on the terminal:
phone: 1234
one two three four
'''

numbers = { 0: "zero",
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine"}
str_num = input("Phone: ")
str = ""
for i in str_num:
    str += numbers[int(i)]
    str += " "
print(str)