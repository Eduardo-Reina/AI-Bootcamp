# simple for loop
# uses range() to loop through a sequence of numbers that you can specify.
# if a variable is not used in the loop, it is common to use an underscore (_) as a placeholder.
# if range() includes two numbers, the first number is the starting point and the second number is the stopping point (not inclusive).
# if range inclides three numbers, the first number is the starting point, the second number is the stopping point (not inclusive), and the third number is the step size.
# step size is the amount by which the loop variable increases each time through the loop.
"""for _ in range(5):
    print("Meow")"""

# simple for loop that counts down from 10 to 1 and then prints "Liftoff!".
"""for number in range(10, 0, -1):
    print(number)
print("Liftoff!")"""


# Simple for loop that iterates through each letter in the string "Programming" and prints each letter on a new line.
"""word = "Programming"
for letter in word:
    print(letter)"""

# a simple for loop that iterates through each letter in the string "Programming" and checks if the letter is a vowel. If it is, it prints a message indicating that a vowel was found along with the letter.
"""word = "Programming"
for letter in word:
    # You can put all the letters you want to check for in a string inside the quotation marks.
    if letter in "aeiou":
        print(f"Vowel found: {letter}")"""

# a simple for loop that iterates through the numbers 1 to 15 and prints each number, except for the numbers that are divisible by 3. If a number is divisible by 3, the loop will skip that number.
"""for number in range(1, 16):
    if(number % 3 == 0):
        continue
    print(number)
print("Finished!")"""

# a simple for loop that iterates through each letter in the string "Programming" and counts the number of vowels in the string. The final count is printed after the loop has finished.
"""word = "Programming"
vowel_count = 0

for letter in word:

    if letter in "aeiou":
        vowel_count += 1
print(vowel_count)"""


# a simple for loop that iterates through the numbers 1 to 5 and calculates the total sum of those numbers. The final total is printed after the loop has finished.
"""total = 0

for number in range(1, 6):
    total += number
    print(total)"""


"""even_numbers = 0

for number in range(1, 11):
    # if i need to use odd numbers 'if number % 2 == 1:'
    if number % 2 == 0:
        even_numbers += number
print(f"Total of even numbers: {even_numbers}")"""


letters = 0
numbers = 0
vowels = 0
forbidden_found = False

username = input("Enter Username: ").lower()

for char in username:
    if char == "!":
        print("Forbidden character found: !")
        forbidden_found = True
        break

    if char.isalpha():
        letters += 1

    if char in "aeiou":
        vowels += 1

    if char.isdigit():
        numbers += 1
if not forbidden_found:
    print(f"Total letters: {letters}")
    print(f"Total vowels: {vowels}")
    print(f"Total numbers: {numbers}")
