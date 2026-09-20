# Lecture 15

# Finger Exercises

# See question at:
# https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/pages/lecture-15-recursion/

def recur_power(base, exp):
    """
    base: int or float.
    exp: int >= 0

    Returns base to the power of exp using recursion.
    Hint: Base case is when exp = 0. Otherwise, in the recursive
    case you return base * base^(exp-1).
    """
    # My code here  
    if exp <= 0:
        return 1
    else:
        return base*recur_power(base, exp-1)

# Examples:
print(recur_power(2,5))  # prints 32


# YOU TRY IT
def factorial(n):
    """
    n: nonnegative int

    Returns n*(n-1)*(n-2)*...*2*1
    """
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(32))