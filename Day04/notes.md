Day 4 — While Loops, Break, and Continue

Today I learned about while loops and how they actually work.

while condition:
    # repeat this

# when the condition becomes False,
# continue here

A while loop keeps running as long as its condition is True. Once the condition becomes False, Python exits the loop and continues with the next line outside of it.

I also learned about break.

break immediately exits the loop that it is currently inside.

Example:

while True:
    if something:
        break

I also learned about continue.

continue does not end the loop. It skips the rest of the current iteration and goes back to the beginning of the loop for the next iteration.

One thing that confused me was thinking that continue would end the loop like break. I learned that they are very different:

break = leave the loop completely.
continue = skip the rest of this iteration and start the next one.

I also learned how easy it is to accidentally create an infinite loop.

For example, if I use continue before changing the value that controls the loop, the variable may never change and the program can get stuck forever.

I had this problem when I was working with numbers and trying to skip the number 5. My program kept getting stuck because the number stayed at 5 every time the loop restarted.

I learned that the order of the code inside a loop matters a lot.

I also struggled with where to put input() inside a loop. At first, I asked for the input before the loop. When I used continue, the program went back to the top of the loop but never asked for a new value.

I learned that if I want the user to enter a new value every time the loop repeats, the input() usually needs to be inside the loop.

I practiced this by making a program that:

keeps asking for numbers,
skips the number 5,
ends when the user enters 0,
and prints every other number.

I also built username and password validation.

For usernames, I used:

.isalpha()

to check that the username contains only letters.

For passwords, I used:

len(password)

to make sure the password had at least 8 characters.

The hardest part of Day 4 was the Final Boss.

I had trouble with nested loops and understanding which loop a break was actually leaving.

I learned that:

break

only exits the closest loop that contains it.

If I have one loop inside another loop, break does not automatically exit both of them.

I also had trouble with indentation and placing the experience section inside the correct part of the program.

At first, my age loop was also controlling the experience section. This made the program repeat questions when I did not want it to.

I learned that it is better to give each part of the program one job:

Username loop → validate username.
Password loop → validate password.
Age loop → validate age.
if/else → decide whether the person is old enough.
Experience loop → validate and classify experience.

This made the program much easier to understand.

I also learned that sometimes adding more loops does not make the program better. Sometimes the best solution is to simplify the structure and use if, elif, and else instead.

Today's Biggest Lesson

The placement and indentation of code inside loops are extremely important.

A loop may technically run, but if the code is in the wrong place, the program can repeat forever, skip important lines, or ask the wrong questions.

Today's Biggest Mistake

I created multiple infinite loops because I used continue without changing the value that controlled the loop.

I also confused myself with nested loops and expected one break to exit more than one loop.

Today's Biggest Win

Even though the Final Boss took me a long time and I got frustrated with the structure, I kept testing the code and fixing one problem at a time.

I now understand while, break, and continue much better than I did at the beginning of the day.

Day 4 was difficult, but I learned a lot from the mistakes.