# Lecture 8

# Finger Exercises

# See Questions at
# https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/pages/lecture-8-functions-as-objects/

def same_chars(s1, s2):
    """
    s1 and s2: strings
    Returns boolean True if a character in s1 is also in s2, and vice versa.
    If a character only exists in one of s1 or s2, returns False.
    """
    for char in s1:
        if char not in s2:
            return False
    for char in s2:
        if char not in s1:
            return False
    return True
        
# print(same_chars('abc','cba'))
# print(same_chars('abccc','caaab'))
# print(same_chars("abcd", "cabaa"))
# print(same_chars("abcabc", "cabz"))


# YOU TRY IT
# Fix the code that tries to write this function (see original code snippet under url above)
def is_triangular(n):
    """
    n: positive integer
    Returns True if n is triangular, i.e. equals a continued summation of natural numbers 
    (1+2+3+...+k), False otherwise.
    """
    total = 0
    for i in range(n+1):
        total += i
        if total == n:
            return(True)
    return(False)

# print(is_triangular(21))


# YOU TRY IT
# How many integer have a square root within epsilon range of n?
def bisection_root(x):
    epsilon = 0.01
    low = 0
    high = x
    ans = (high+low)/2.0
    while(abs(ans**2 - x) >= epsilon):
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high+low)/2.0
    return ans

def count_nums_with_sqrt_close_to(n, epsilon):
    """
    n: positive integer > 2
    epsilon: positive number < 1
    Returns how many integers have a square root within epsilon of n.
    """
    total = 0
    for i in range(n**2+2*n+1):
        if abs(bisection_root(i)-n) <= epsilon:
            total += 1
            print(bisection_root(i))
    return total

# print(count_nums_with_sqrt_close_to(10, 0.1))

# YOU TRY IT
# Write a function that meets these specs
def apply(criteria, n):
    """
    criteria: is a func that takes in a number and returns a bool
    n: int
    Returns how many ints from 0 to n (inclusive) match the criteria 
    (i.e. return True when run with criteria)
    """
    count = 0
    for i in range(n+1):
        if criteria(i):
            count += 1
    return count

print(apply(is_triangular, 20))
