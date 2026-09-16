# Lecture 12

# Finger Exercise

# See Question at
# https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/pages/lecture-12-list-comprehension-functions-as-objects-testing-debugging/

def count_sqrts(nums_list):
    """
    nums_list: a list
    Assumes that nums_list only contains positive numbers and that there are no duplicates.
    Returns how many elements in nums_list are exact squares of elements in the same list, 
    including itself.
    """
    tot = 0
    for i in nums_list:
        if i*i in nums_list:
            tot += 1
    return tot


# Examples:
# print(count_sqrts([3,4,6,-5,9,25]))  # prints 2


# YOU TRY IT