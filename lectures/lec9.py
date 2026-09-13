# Lecture 9

# Finger Exercises

# See Questions at
# https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/pages/lecture-9-lambda-functions-tuples-and-lists/

def dot_product(tA, tB):
    """
    tA: a tuple of numbers
    tB: a tuple of numbers of the same length as tA
    Assumes tA and tB are the same length.
    Returns a tuple where the:
    * first element is the length of one of the tuples
    * second element is the sum of the pairwise products of tA and tB
    """
    # My code here
    pair_prod = 0
    for i in range(len(tA)):
        pair_prod += tA[i]*tB[i]
    return (len(tA), pair_prod)

# Examples:
tA = (1, 2, 3)
tB = (4, 5, 6)   
# print(dot_product(tA, tB)) # prints (3,32)


# YOU TRY IT
# Write a function that meets these specs
def char_counts(s):
    """
    s: string of lowercase chars
    Return a tuple where the first element is the number of vowels in s and 
    the second element is the number of consonants in s
    """
    (vowel_count,cons_count) = (0,0)
    for char in s:
        if char in 'aeiuo':
            vowel_count += 1
        else:
            cons_count +=1
    return (vowel_count, cons_count)

# print(char_counts("mathematics"))
# print(char_counts("aaaai"))


# YOU TRY IT
# Write a function that meets these specs
def sum_and_prod(L):
    """
    L: list os numbers
    Return a tuple where the first value is the sum of all elements in L and
    the second value is the product of all elements in L
    """
    (sum, prod) = (0,1)
    for e in L:
        sum += e
        prod *= e
    return (sum, prod)

print(sum_and_prod([-2, 4.5, 12]))