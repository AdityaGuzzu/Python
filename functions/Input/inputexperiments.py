def PANeligibility():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    nationality = input("Enter your nationality: ")
    if age >= 18 and nationality == "Indian":
        print("You can apply for PAN.")
    else:
        print("You are not eligible to apply for PAN.")

