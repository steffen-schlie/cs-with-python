# Lecture 6

# Finger Exercises

# Assume you are given an integer 0 <= N <= 1000. Write code that uses
# bisection search to guess N. The code prints how many guesses it took 
# to find N and its value.

N = 2
lower, upper = 0, 1001
guess = (lower+upper)//2
count = 0

# Use bisection search algorithm to make correct guess (eventually)
while (guess != N):
    count += 1
    if guess > N:
        upper = guess
    else: 
        lower = guess
    guess = (upper+lower)//2
print(f"{count}, {guess}")