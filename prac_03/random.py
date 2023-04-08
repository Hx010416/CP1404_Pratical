"""
In your console, type in the following (run each line multiple times), and write the answers to the questions below in comments in randoms.py.
import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

What did you see on line 1?
Answer: A random integer between 5 and 20 inclusive.
What was the smallest number you could have seen, what was the largest?
Answer: The smallest number is 5 and the largest number is 20.

What did you see on line 2?
Answer: A random odd integer between 3 (inclusive) and 10 (exclusive).
What was the smallest number you could have seen, what was the largest?
Answer: The smallest number is 3 and the largest number is 9.
Could line 2 have produced a 4?
Answer: No, it could not have produced a 4 since the step is 2 and it starts at 3, so the only possible values are 3, 5, 7, and 9.

What did you see on line 3?
Answer: A random floating point number between 2.5 (inclusive) and 5.5 (inclusive).
What was the smallest number you could have seen, what was the largest?
Answer: The smallest number is 2.5 and the largest number is 5.5.

Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""
import random

random_number = random.randint(1, 100)
print(random_number)