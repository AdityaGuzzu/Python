'''
Building a guess game where the user should guess the right number in three attempts
'''
counter = 0
did_win = False
while counter < 3 and not did_win:
    inp = int(input("Guess the number: "))
    if(inp == 5):
        print("Hurray! You won")
        did_win = True
    else:
        print("OOPS you lost!")
        counter += 1