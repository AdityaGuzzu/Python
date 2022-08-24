'''Build a car game that first prompts the following
    Enter 'start' to start the car
    Enter 'stop' to stop the car
    Enter 'quit' to exit the car program.

    It should take inputs from the user until they want to quit.
    If the user enters a wrong word, it should prompt  'Sorry, I don't understand that......'
'''
message = '''
Welcome to car simulation.
--------------------------
Enter 'start' to start the car
Enter 'stop' to stop the car
Enter 'quit' to quit the program'''

#lets print the initial instructions
print(message)
in_the_car = True

while(in_the_car):
    inp = input()
    if inp == "start":
        print("Started the car")
    elif inp == "stop":
        print("Stopped the car")
    elif inp == "exit":
        print("Quit the program")
        in_the_car = False
    else:
        print("I don't understand that......")


