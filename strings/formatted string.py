#Lets print something like 'Barcelona and [Manchester United] are finished ' with Barcelona and Manchester
#   United being stored in two different variables.

#This method is valid but very much un-readable
eng_club = "Manchester United"
esp_club = "Barcelona"
msg = esp_club + ' and ' + '[' + eng_club + '] are finished '
#lets print it on the console
print(msg)

#more readable way can be achieved though formatted strings like we have in C and C++
#quotes prefixed with an 'f' make a formatted string. Variables can be written in between {}
msg = f"{esp_club} and [{eng_club}] are finished"

#lets print it. We get the exact same result
print(msg)