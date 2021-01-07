def rotLeft(a, d):
    if len(a) > 0:
        d = d % len(a)
        return a[d:] + a[:d]

    else:
        return 0

def rotLeftInPlace(a,d):
    if len(a) > 0:
        d = d % len(a)
        a.extend(a[:d])
        del(a[:d])
        return a
    else:
        return 0

if __name__ == "__main__":
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    print(result)

    print(rotLeftInPlace(a,d))