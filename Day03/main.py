# This code shows how to USE and in a statement very usefull...
"""new_score = int(input("What was your score? "))

if  90 <= new_score <= 100:
    print("Grade: A ")
    print("Congratulations ")
    print("Keep up the good work! ")

elif 80 <= new_score <= 89:
    print("Grade: B ")

elif 70 <= new_score <= 79:
    print("Grade: C")

elif 60 <= new_score <= 69:
    print("Grade: D")

else:
    print("Grade: F ")
    print("Make sure to study for your next exam! ")

#print(type(new_score))"""

# This code is to learn if a number is even or odd !!!
# It also teaches how to create your own code!!!

"""def main():
    x = int(input("What is X? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return n % 2 == 0
    
main()"""


# How to use match

"""new_name = input("What's your name? ")

# This is how or is suposed to be used !!!
if new_name == "Harry" or new_name == "Hermione" or new_name == "Ron":
    print("Gryffindor")

elif new_name == "Draco":
    print("Slytherin")

else:
    print("Who?")

match new_name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")

    case "Draco":
        print("Slytherin")

    case _:
        print("Who?")"""


# Final Boss Battle of day # 3


print("=" * 30)
print("AI University Login")
print("=" * 30)

new_name = input("Name: ").strip().title()
new_username = input("Username: ").strip().lower()
new_password = input("Password: ").strip()
#Remember If you want to ask a guestion before another and only
#have one those guestiones answered if the one before is 
if new_username == "admin" and new_password == "python123":
    new_age = int(input("Age: "))
    if new_age < 18:
        print("You are too young for the internship program.")

    elif new_age >= 18:
        new_experience = int(input("Years of Python experience: "))
        if new_experience == 0:
            print("Everyone starts somewhere!")

        elif new_experience == 1 or new_experience == 2:
            print("You're building a great foundation!")

        else:
            print("You're ready to apply for internships!")


else:
    print("Incorrect username or password.")
    print("Access Is Denied!!!")


print(f"Good luck {new_name}")
