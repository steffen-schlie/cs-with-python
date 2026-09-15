# Lecture 11

# Finger Exercise

# See Question at
# https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/pages/lecture-11-aliasing-cloning/

def remove_and_sort(Lin, k):
    """ 
    Lin: is a list of ints
    k: is an int >= 0
    Mutates Lin to remove the first k elements in Lin and 
    then sorts the remaining elements in ascending order.
    If you run out of items to remove, Lin is mutated to an empty list.
    Does not return anything.
    """
    # My code here  
    if len(Lin) <= k:
        Lin.clear()
        return
    for i in range(k):
        del(Lin[0])
    Lin.sort()

# Examples:
L = [1,6,3]
k = 1
remove_and_sort(L, k)
print(L)   # prints the list [3, 6]


# YOU TRY IT
# Write a function that meets the specs
def remove_all(L, e):
    """
    L: list
    Mutates L to remove all elements in L that are equal to e
    Returns None
    """
    copy_list = L[:]
    L.clear()
    for elem in copy_list:
        if elem != e:
            L.append(elem)
    # alternatively
    # while e in L:
    #   L.remove(e)

L = [1,2,2,2]
remove_all(L, 2)
print(L)
    