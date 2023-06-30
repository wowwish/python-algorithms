# A Recursive function is a function that calls itself ... until a termination condition is satisfied.

times = 0
ball = 3
def open_gift_box():
    # this if condition is the base case or the termination condition
    global times
    if times == ball:
        return ball
    times += 1
    open_gift_box() # recursive call. Each recursive call makes the problem smaller.


# If the base case or termination condition is never reached, it will lead to a stack overflow error (
# infinite recursion)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(4))