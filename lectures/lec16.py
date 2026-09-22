# Lecture 16

# Finger Exercises

# See question at
# https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/pages/lecture-16-recursion-on-non-numerics/

def flatten(L):
    """ 
    L: a list 
    Returns a copy of L, which is a flattened version of L 
    """
    # Base case: List contains one element
    result = []
    for i in L:
        if type(i) == list:
            result.extend(flatten(i))
        else:
            result.append(i)
    return result
     

# Examples:
L = [[1,4,[6],2],[[[3]],2],4,5]
print(flatten(L)) # prints the list [1,4,6,2,3,2,4,5]