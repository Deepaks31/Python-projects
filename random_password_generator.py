import random
import string

characters= list(string.ascii_letters + string.digits + "!@#$%^&*(){}[]/><':;|")

def generate_password():
    length=int(input("Enter a length of a password: "))

    random.shuffle(characters)

    password = []

    for x in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password="".join(password)

    print(password)


option = input("Do you want to generate password (Yes or No) : ")
if option == "Yes":
        generate_password()
elif option == "No":
        print("Program Ended")
        quit()
else:
        print("Invalid Input Enter Yes or No")
        quit()

