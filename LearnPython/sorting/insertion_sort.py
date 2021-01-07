from random import randint
from time import time

def insertion_sort(a):
    for sorted_len in range(1,len(a)):
        current_item = a[sorted_len]
        insert_indx = sorted_len

        while insert_indx > 0 and current_item < a[insert_indx-1]:
            a[insert_indx] = a[insert_indx - 1]
            insert_indx = insert_indx - 1

        a[insert_indx] = current_item

    return a

def create_array(size=10, max_val=100):
    return [ randint(0, max_val) for _ in range(size) ]

if __name__ == "__main__":

    a = create_array()
    print("Unsorted: ",a)
    a = insertion_sort(a)
    print("Sorted: ", a)