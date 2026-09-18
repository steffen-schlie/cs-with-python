# Lecture 14

# Finger Exercises

# See question at:
# https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/pages/lecture-14-dictionaries/

def keys_with_value(aDict, target):
    """
    aDict: a dictionary
    target: an integer or string
    Assume that keys and values in aDict are integers or strings.
    Returns a sorted list of the keys in aDict with the value target.
    If aDict does not contain the value target, returns an empty list.
    """
    # My code here  
    new_list = []
    for key in list(aDict.keys()):
        if aDict[key] == target:
            new_list.append(key)
    sorted_list = sorted(new_list)
    return sorted_list

# Examples:
aDict = {5:2, 2:4, 1:2}
target = 2   
print(keys_with_value(aDict, target)) # prints the list [1,5]



def all_positive(d):
    """
    d is a dictionary that maps int:list
    Suppose an element in d is a key k mapping to value v (a non-empty list).
    Returns the sorted list of all k whose v elements sums up to a 
    positive value.
    """
    # My code here  
    new_list = []
    for key in d.keys():
        if sum(d[key]) > 0:
            new_list.append(key)
    sorted_list = sorted(new_list)
    return sorted_list

# Examples:
d = {5:[2,-4], 2:[1,2,3], 1:[2]}
print(all_positive(d))   # prints the list [1, 2]