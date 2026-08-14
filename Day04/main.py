# This is a simple while loop that prints "Miow" three times
"""new_sentence = 0

while new_sentence < 3:
    print("Miow")
    new_sentence += 1"""


# Username loop
"""new_user = input("Username:").strip()
while not new_user.isalpha():
    print("Invalid Username")
    print("Only Use Letters!")
    print("Try again! ")
    new_user = input("Username: ").strip()

# Password basic loop
new_pasword = input("Password: ").strip()
while len(new_pasword) < 8:
    print("Password must have 8 characters or more!")
    new_pasword = input("Password: ").strip()


print(f"Welcome {new_user}")"""


"""new_user = input("Username:").strip()
#.isalpha() is only to check if the username contains only letters!!
while not new_user.isalpha():
    print("Invalid username!")
    print("Username can only contain letters.")
    new_user = input("Username: ").strip()

print(f"Welcome {new_user}!")"""

# This is a simple while loop that teaches the person how to use break.
"""new_password = input("Password: ").strip()

while True:

    if new_password == "python123":
    
            break

    print("Incorrect password. Try again!")

    new_password = input("Password: ").strip()

print("Access granted!")"""

# This is a simple while loop that teaches the person how to use continue.
"""new_number = 0

while new_number < 10:
    
    new_number = new_number + 1

    if new_number == 5:
        continue
    print(new_number)

print("Finished!")"""

# This is a simple while loop that teaches the person how to use break and continue.
"""while True:
    new_number = int(input("Enter a number from 1 to 10: "))
    if new_number == 0:
        break

    elif new_number == 5:
        print("Skipping number 5")
        continue
    else:
        print(f"Your number is: {new_number}")"""


"""while True:

    new_age = int(input("Enter your age: "))

    if new_age == 0 or new_age > 120:
        print("Invalid age. Please enter a valid age between 1 and 120.")
        continue

    elif new_age < 18:
        print(f"You are {new_age} years old. You are a minor.")
        break

    else:
        print(f"You are {new_age} years old. You are an adult.")
        break"""

new_username = input("Enter your username: ").strip().title()

while not new_username.isalpha():
    print("Invalid username. Please enter a valid username containing only letters.")
    new_username = input("Enter your username: ").strip().title()


new_password = input("Enter your password: ").strip()

while True:
    if len(new_password) < 8:
        print("Password must have at least 8 characters.")
        new_password = input("Enter your password: ").strip()
    else:
        break


new_age = int(input("Enter your age: "))

while True:
    if new_age <= 0 or new_age > 120:
        print("Invalid age. Please enter a valid age between 1 and 120.")
        new_age = int(input("Enter your age: "))
    else:
        break


if new_age < 18:
    print("You are too young to apply.")

else:
    while True:
        new_experience = int(input("Enter your years of experience: "))

        if new_experience == 99:
            print("Application cancelled.")
            break

        elif new_experience < 0:
            print("Invalid experience.")
            continue

        elif new_experience == 0:
            print("Novice")
            break

        elif new_experience <= 2:
            print("Intermediate")
            break

        else:
            print("Advanced")
            break
