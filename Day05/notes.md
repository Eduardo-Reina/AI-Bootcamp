Day 5 — For Loops
For Loops

Today I learned how for loops work.

A for loop goes through a sequence one item at a time. Unlike a while loop, I usually do not have to manually update the loop variable because Python automatically moves to the next item.

If the loop variable is not needed, an underscore (_) can be used as a placeholder.

range()

I learned that range() can be used to create a sequence of numbers for a for loop.

range() can have:

A stop value
A start and stop value
A start, stop, and step value

Important rules:

The start number is included.
The stop number is NOT included.
The step controls how much the number changes each iteration.
A positive step counts upward.
A negative step can count backward.

Looping Through Strings

A for loop can also go through a string one character at a time.

This means I can examine every letter or character individually and use conditions to decide what to do with it.

I also learned that the in operator can check whether a character exists inside another string. For example, this can be useful for checking whether a letter is a vowel.

Counters and Running Totals

I learned how to use variables as counters inside loops.

A counter can start at 0 and increase whenever a certain condition is true.

I also learned that += can increase a counter or add the current value to a running total.

This allows a for loop to do things such as count vowels or calculate the total of several numbers.

Final Boss — Important Lessons

The Final Boss helped me understand several problems with control flow that I also struggled with during Day 4.

One Value Can Satisfy Multiple Conditions

I had a problem when counting letters and vowels because a vowel is also a letter.

Using an if/elif structure meant that once Python recognized the character as a letter, it skipped the vowel check.

I learned that separate if statements should be used when more than one condition can be true at the same time.

Boolean Flags

To solve the Final Boss, I learned about using a Boolean variable as a flag.

A flag can start as False and change to True when something important happens.

The rest of the program can then check the flag to decide whether certain code should run.

This allows the program to remember something that happened earlier, even after a loop has ended.

Day 5 Key Takeaways
For loops go through sequences one item at a time.
range() controls a sequence of numbers using start, stop, and step.
The stop value in range() is not included.
For loops can go through strings character by character.
Counters keep track of how many times something happens.
Running totals add values together over multiple iterations.
The remainder operator can help identify even and odd numbers.
break exits the current loop, not the entire program.
continue skips the current iteration.
Indentation determines whether code runs during or after a loop.
Separate if statements are useful when multiple conditions can be true.
Boolean flags can remember that something happened earlier in the program.