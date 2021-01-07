#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    ex = [ expenditure[x: x+d] for x in range(len(expenditure) - d + 1)]

    threshold = 0
    notifications = 0

    for idx, l in enumerate(ex):
        print("l = ", l)
        if d % 2 != 0:
            threshold = l[math.floor(d / 2)] * 2
        else:
            threshold = (l[d/2] + l[(d+1)/2])/2 * 2

        print("threshold: ", threshold)

        if idx + 1 < len(ex):
            print("idx + 1: ", idx + 1)
            if ex[idx+1][0] >= threshold:
                print("item = ", ex[idx + 1][0])
                notifications += 1

    return notifications


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)
    print("notifications: ", result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
