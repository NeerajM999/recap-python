from random import randint

def selection_sort(a):
    sorted_len = 0

    while sorted_len < len(a):
        min_loc = None

        for i,item in enumerate(a[sorted_len:]):
            if min_loc is None or item < a[min_loc]:
                #print ("Before: min_loc is: {} and item is {}, i={}".format(min_loc,item,i))

                # update with current smallest element
                min_loc = i + sorted_len
                #print ("After: min_loc is: {} and item is {}, i={}".format(min_loc,item,i))


        # swap
        a[min_loc], a[sorted_len] = a[sorted_len], a[min_loc]
        sorted_len += 1
        #print("In progress: ", a)
    return a

def bubble_sort(input):
    """
    space: O(1)
    time: O(n^2)
    """

    issorted = False
    count = 0
    array_size = len(input) - 1

    while not issorted:
        issorted = True
        for i in range(0, array_size):
            count += 1
            if input[i] > input[i+1]:
                input[i], input[i+1] = input[i+1], input[i]
                issorted = False
        array_size -= 1 # last element is sorted in first pass, 2nd last in 2nd pass and so on.. so we dont need to sort them again

    #print("counter = ", count)
    return input

def create_array(size=10, max_val=100):
    return [randint(0, max_val) for _ in range(size)]

if __name__ == "__main__":

    a = create_array()
    print("unsorted: ", a)
    a = selection_sort(a)
    print("sorted: ", a)

    ## benchmarking

    from time import time
    n = [10,100,1000,10000]
    times={'built-in':[], 'bubble-sort':[], 'selection-sort':[]}

    for size in n:
        a = create_array(size, size)
        t0 = time()
        a = sorted(a)
        t1 = time()
        times['built-in'].append(t1-t0)

        a = create_array(size, size)
        t0 = time()
        a = bubble_sort(a)
        t1 = time()
        times['bubble-sort'].append(t1-t0)

        a = create_array(size, size)
        t0 = time()
        a = selection_sort(a)
        t1 = time()
        times['selection-sort'].append(t1-t0)

    print("\nn \tBuilt-in \tBubble-sort \tSelection-sort")
    print("_"*40)

    for i, batch in enumerate(n):
        print("%d\t%0.5f\t%0.5f\t%0.5f" %
              (batch, times['built-in'][i], times['bubble-sort'][i], times['selection-sort'][i]))



