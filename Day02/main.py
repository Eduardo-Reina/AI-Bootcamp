"""x = int(input("What is X = "))
y = int(input("What is Y = "))

if x < y:
    print("Y is greater than X")

elif y < x:
    print("X is grater than Y")

else:
    print("X and Y have the same value")
"""

"""new_age = int(input("How old are you? "))


if new_age >= 18:
 print("You are an adult. ")

else:
 print("You are a minor")
"""
"""print("=" * 15)
print("C++")
print("Python")
print("Java")
print("JavaScript")
print("C#")
print("=" * 15)
# the last par of the code is for the code to not get too many spaces and that the user can use lower case!
#REMEMBER THIS!!!!!!
new_language =input("What is your favorite language? ").strip().lower()

if new_language == "Python":
    print("Great choice! ")

else:
    print("That's a cool language too! ")"""


"""new_number = int(input("Chose any number: "))

if new_number >=1:
    print ("You have a positive number. ")

elif new_number <= -1:
    print ("You have a negative number. ")

else:
    print("Your number is zero! ")"""


print("=" * 30)
print("AI Internship Interview! ")
print("=" * 30)


new_name = input("Name: ").strip().title()
new_age = int(input("Age: "))
new_experience = int(input("Years of Python Experience: "))

if new_age < 18:
    print("Sorry, you must be at least 18. ")

elif new_experience == 0:
    print("Everione starts somewhere! ")
    print("Keep learning! ")

elif new_experience <= 2:
    print("You're building a great Foundation")

else:
    print("You're ready to apply for internships!")


print(f"Good luck, {new_name}! ")
