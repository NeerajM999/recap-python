
def merge(a,b):
    c = []
    i, j = 0,0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    # if one of the array finishes first, push remaining items from other list
    if i == len(a):
        c.extend(b[j:])
    else:
        c.extend(a[i:])

    return c

def merge_sort(a):
    if len(a) <=1: return a

    first, second = merge_sort(a[:len(a)//2]), merge_sort(a[len(a)//2:])

    return merge(first, second)

def create_array(size=10, max_val=100):
    from random import randint
    return [ randint(0, max_val) for _ in range(size) ]


if __name__ == "__main__":

    a = create_array()
    print("unsorted: ", a)
    a = merge_sort(a)
    print("sorted: ", a)

    a = quick_sort(a)
    print("Quick sort: ", a)
    