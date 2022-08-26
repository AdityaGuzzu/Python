def PANeligibility(name, age, nationality):
    if age >= 18 and nationality == "Indian":
        print(f"{name}, you can apply for PAN.")
    else:
        print(f"{name}, you are not eligible to apply for PAN.")


name = input("Enter your name: ")
age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ")
PANeligibility(name,age,nationality)


