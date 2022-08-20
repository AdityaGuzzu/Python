from copystringpalindrome import rev
word = input("The word you want to check ")
if rev(word) == word:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
