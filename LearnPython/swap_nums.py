def swap(a, b):
    """
    swaps 2 nos without using 3rd variable
    :param a:
    :param b:
    :return:
    """
    a = a ^ b
    b = a ^ b
    a = a ^ b

    return (a,b)

def swap2(a,b):
    a, b = b, a
    return (a,b)

def swap3(a,b):
    a = a + b
    b = a - b
    a = a - b

    return (a,b)

print(swap(10,5))

print(swap2(2,3))

print(swap3(4,5))