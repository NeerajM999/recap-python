def maximumToys(prices, k):
    #prices.sort()
    np = [ n for n in prices if n <= k ]
    np.sort()

    i = len(np)
    while( i > 0 ):
        if sum(np[:i]) <= k:
            return i
        i -= 1



if __name__ == "__main__":
    """
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()
    
    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
    
    """
    #prices = [1, 12, 5, 111, 200, 1000, 10]
    #k = 50

    nk = input().split()
    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    print(maximumToys(prices, k))