import math
# Complete the repeatedString function below.
def repeatedString(s, n):
    if len(s) > 1:
        #s = (s * math.ceil(n/len(s)))[0:n]
        #return sum([ 1 for i in s if i == 'a' ])

        l = len(s)
        c = sum([ 1 for i in s if i == 'a' ])

        r = c*(n//l) + sum([ 1 for i in s[0:n%l] if i == 'a' ])
        return r

    elif len(s) == 1 and s == 'a':
        return n

    else:
        return 0


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
