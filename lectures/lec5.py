# Lecture 5

# Finger Exercises

# Assume you are given a string variable named my_str.
# Write a piece of Python code that prints out a new string
# containing the even indexed characters of my_str.

my_str = "Mathematics"
new_str = ""
for i in range(0,len(my_str),2):
    new_str += my_str[i]
print(new_str)