# Lecture 7

# Finger Exercises

# See Questions at 
# https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/pages/lecture-7-decomposition-abstraction-functions/

def eval_quadratic(a, b, c, x):
    """
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    Returns the value of the quadratic a×x² + b×x + c.
    """
    # My code here:
    return a*x*x + b*x + c

print(eval_quadratic(2,-3,0,2))


def two_quadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    """
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    Evaluates one quadratic with coefficients a1, b1, c1, at x1.
    Evaluates another quadratic with coefficients a2, b2, c2, at x2.
    Prints the sum of the two evaluations. Does not return anything.
    """
    # My code here
    print(eval_quadratic(a1, b1, c1, x1)+eval_quadratic(a2, b2, c2, x2))

two_quadratics(1,1,1,1,1,1,1,1)
print(two_quadratics(1,1,1,1,1,1,1,1)) 

