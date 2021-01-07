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


if __name__ == "__main__":
    l = [3,2,5,1,9,6,8]
    print(bubble_sort(l))
