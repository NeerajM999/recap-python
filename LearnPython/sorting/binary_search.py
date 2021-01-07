def binary_search(a, value):
    if len(a) == 0 or (len(a) == 1 and a[0] != value):
        return False

    # find mid of the array
    mid = a[len(a)//2]

    if value == mid:
        return True
    elif value < mid:
        return binary_search(a[:len(a)//2], value)
    elif value > mid:
        return binary_search(a[len(a)//2+1:], value)

if __name__ == "__main__":

    a = [1,2,3,4,5,6,7,8,9,10]
    print("array is ", a)
    print(binary_search(a, 23))