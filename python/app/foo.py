def isinstnace(x, val):
    # print( type(x) )
    # print( type(x) == int )
    if type(x) == val:
        return True
    else:
        return False

def add_int(x, y):
    if isinstnace(x, int) and isinstance(y, int):
        return x + y
    else:
        raise ValueError("{} or {} is not Integer.".format(x, y))

def add(a, b):
    return a+b

def minus(a, b):
    return a-b

def multi(a, b):
    return a*b

def divide(a, b):
    return a/b