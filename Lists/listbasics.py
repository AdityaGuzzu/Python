#List is an ordered collection of data
#Let's print values of a list
Colleges = ["Sri Chaitanya", "Bhavan's", "Narayana", "Toppers"]
y = len(Colleges)
z = 0
while z <= y-1:
    print(Colleges[z])
    z += 1
z = 0
print("printing reverse of the list")
while z > -y:
    print(Colleges[z])
    z -= 1
print("printing with for loop")
for college in Colleges:
    print(college)
print("Printing alternate items of a list")
y = len(Colleges)
z = 1
while z <= y-1:
    print(Colleges[z])
    z += 2
