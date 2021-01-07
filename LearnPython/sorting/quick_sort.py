from random import randint

def quick_sort(input):
    """
    Time: average - O(nlogn), worst - O(n^2)
    :param input:
    :return:
    """
    if len(input) <=1:
        return input

    small, equal, large = [], [], []
    pivot = input[randint(0, len(input) - 1)]
    for item in input:
        if item < pivot:
            small.append(item)
        elif item == pivot:
            equal.append(item)
        elif item > pivot:
            large.append(item)

    return quick_sort(small) + equal + quick_sort(large)


## in-place quick sort

def quick_sort_inplace(a, low=0, high=None):
    if high is None:
        high = len(a) - 1

    if low < high:
        p = partition(a, low, high)
        quick_sort_inplace(a, low, p-1)
        quick_sort_inplace(a, p+1, high)

def partition(a, low, high):
    i = low-1
    pivot = a[high]

    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            # swap
            a[i], a[j] = a[j], a[i]

    a[i+1], a[high] = a[high], a[i+1]

    return i+1


def create_array(size=20, max_val=500):
    return [randint(0, max_val) for _ in range(size)]

if __name__ == "__main__":

    a = create_array()
    print(a)

    print(quick_sort(a))

    b = create_array()
    print("Unsorted: ", b)
    quick_sort_inplace(b)
    print("Sorted: ", b)


    # code for bench mark both functions
    from time import time
    times = {'new':[], 'inplace':[]}
    sizes = [10,100,1000,10000,100000]
    samples = 3

    for s in sizes:
        total = 0.0
        for _ in range(samples):
            a = create_array()
            t0 = time()
            a = quick_sort(a)
            t1 = time()
            total += (t1 - t0)
        times['new'].append(float(total/samples))

        for _ in range(samples):
            a = create_array()
            t0 = time()
            quick_sort_inplace(a)
            t1 = time()
            total += (t1 - t0)
        times['inplace'].append(float(total/samples))

    print ("\nn\tQuicksort\tQuicsort - inplace")
    print ("_"*40)
    for i, s in enumerate(sizes):
        print("%d\t%0.5f    \t%0.5f"%(s,times['new'][i], times['inplace'][i]))
    print("\n")



