# Lecture 4

# Finger Exercises

# Assume you are given a positive integer variable named N. 
# Write a piece of Python code that finds the cube root of N.
# The code prints the cube root if N is a perfect square or 
# it prints error if N is not a perfect cube. 

N = 8
i = 1
while (i**3 < N):
    i += 1
if i**3 == N:
    print(i)
else:
    print('error')

