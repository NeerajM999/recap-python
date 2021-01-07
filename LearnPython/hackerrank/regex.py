

import re
import sys
import math

def dotPattern():
    #regex_pattern = r".{3}\..{3}\..{3}\..{3}"	# Do not delete 'r'.
    regex_pattern = r".{3}\..{3}\..{3}\..{3}$"

    #test_string = input("Enter expression: ")
    test_string = "123.456.abc.def"

    match = re.match(regex_pattern, test_string) is not None

    print(str(match).lower())


def stringPattern():
    Regex_Pattern = r'hackerrank'	# Do not delete 'r'.
    #Test_String = input("Enter test string: ")

    Test_String = "The hackerrank team is on a mission to flatten the world"
    match = re.findall(Regex_Pattern, Test_String)

    print("Number of matches :", len(match))
    print(match)


def searchDigitPattern():

    Regex_Pattern = r"^\d{2}\D\d{2}\D\d{4}$"	# Do not delete 'r'.

    test_string = "06-11-2015"

    print(str(bool(re.search(Regex_Pattern, test_string))).lower())


def whiteSpacePattern():
    Regex_Pattern = r"\S{2}\s\S{2}\s\S{2}"	# Do not delete 'r'.

    test_string = "12 11 15"
    print(str(bool(re.search(Regex_Pattern, test_string))).lower())


def webscrape():

    pattern = re.compile(r'href="/questions/(\d+)/.+?>(.+?)</a>.+?class="relativetime">(.+?)</span>', re.DOTALL)
    fragment = sys.stdin.read()

    result = pattern.findall(fragment)

    for line in result:
        print(*line, sep=';')

def power_conversion(raw_power):
    # Write your code here

    units = {
        "W": 1,
        "WATT": 1,
        "KW": 1000,
        "MW": 1000000,
        "GW": 1000000000
        }

    pattern = re.compile(r'^(\d+)([a-zA-Z]{2}$)|^(\d+)e(\d*)([a-zA-Z]+)')

    result = pattern.findall(raw_power)
    print(result)
    if result:
        line = [ a for a in result[0] if a != '' ]

        print(line)

        if len(line) == 2:
            return int(line[0]) * int(units.get(line[-1].upper()))

        elif len(line) == 3:
            num = line[0]+'e'+line[1]
            print(num)
            return int(float(num) * int(units.get(line[-1].upper())))
        else:
            return ""
    else:
        return ""

def countSwaps(a):
    """
    Bubble sort an array
    :param a:
    :return:
    """
    swaps = 0
    for i in range (0,len(a)):
        for j in range(0, len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1

    print("Array is sorted in %d swaps." % swaps)
    print("First Element:", a[0])
    print("Last Element:", a[-1])



if __name__ == "__main__":
    #stringPattern()
    #dotPattern()
    #searchDigitPattern()
    #whiteSpacePattern()fptr = open(os.environ['OUTPUT_PATH'], 'w')

    """
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()

    """
    
    """

    maximumToys([1, 12, 5, 111, 200, 1000, 10], 50)
    
    """

    print(power_conversion("1igu"))