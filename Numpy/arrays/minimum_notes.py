'''
We will use NumPy to convert an amount of money into the minimum number of notes.

We will assume this is the business game with the lowest denomination being $50 and the highest being $10,000
'''

import numpy as np
note_values = np.array([10000,5000,1000,500,100,50], dtype=int)
num_of_notes = np.zeros(6, dtype=int)

#stop is a loop controlling boolean
stop = False

while not stop:
    num_of_notes = np.zeros(6, dtype=int)
    amount = int(input("Enter the amount: "))

    #to control illegal amounts
    if amount%50 != 0:
        print("Wrong amount entered.")

    else:
        amount_copy = amount
        for value in note_values:
            if amount_copy/value > 0:
                num_of_notes[np.where(note_values==value)] = amount_copy / value
                amount_copy %= value

        for elem in np.arange(len(num_of_notes)):
            print(note_values[elem], '*', num_of_notes[elem])


    continue_ = int(input("Do you want to continue?. Press 0 for yes and 1 for no "))
    stop = continue_
