'''
reading from a text file
'''

with open('text.txt') as file:
    #this copies the entire contents of the file into word
    word = file.read()
    print(word)

    #closing the file
    file.close()

with open('text.txt') as file:

    #the readline function reads the text line by line. i.e the delimiter is '\n'
    word = file.readline()
    print(word)

    #closing the file
    file.close()


with open('text.txt') as file:
    #readlines fucntion converts the file into an array with each line being one element. But incluses the '/n'
    #character

    word = file.readlines()
    print(word)

    #closing the file
    file.close()

