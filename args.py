# *args = parameter that will pack all arguments into a tuple

def add(*args):
    sum = 0
    args = list(args) # cast type tuple to list
    args[0] = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6,7,8,9))
