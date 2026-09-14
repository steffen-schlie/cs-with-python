# Lecture 10

# Finger Exercises

# See question at
# https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/pages/lecture-10-lists-mutability/

def all_true(n, Lf):
    """ 
    n: int
    Lf: list of functions that take in an int and return a Boolean
    Returns True if each and every function in Lf returns True when called 
    with n as a parameter. Otherwise returns False. 
    """
    # My code here
    flag = True
    for f in Lf:
        if not f(n):
            flag = False
            break
    return flag
        
# Examples:    
print(all_true(6,[lambda x: x%2 == 0, lambda x: x**2 == 36]))


# YOU TRY IT

# Write a function that meets these specs:
def make_ordered_list(n):
    """
    n: positive int
    Returns list containing all ints in order from 0 to n (inclusive)
    """
    mylist = []
    for i in range(n+1):
        mylist.append(i)
    return mylist

# print(make_ordered_list(12))

# Write a function that meets these specs:
def remove_element(L,e):
    """
    L: list
    e: object
    Returns a new list with elements in the same order as L
    but without any elements equal to e.
    """
    for elem in L:
        if elem == e:
            L.remove(elem)
    return L

# print(remove_element(make_ordered_list(10),2))

# Write a function that meets these specs:
def count_words(sen):
    """
    sen: string representing a sentence
    Returns how many words are in s.
    """
    return len(sen.split(' '))

# print(count_words("Maths<3"))

# Write a function that meets these specs:
def sort_words(sen):
    """
    sen: string representing a sentence
    Returns a list containing all words in sen
    but sorted in alphabetical order.
    """
    new_list = sen.split(' ')
    # alt.: return sorted(new_list)
    new_list.sort()
    return new_list

# print(sort_words("liverpool is a great club"))