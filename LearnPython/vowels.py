import re

def count_vowels(value):
    pattern = re.compile(r'[aeiouAEIOU]')

    results = pattern.findall(value, 0 , len(value))
    print("Vowels: ", results)
    return len(results)


def count_consonents(value):
    pattern1 = re.compile(r'[^aeiouAEIOU]')
    results = pattern1.findall(value, 0, len(value))

    #print(results)

    pattern2 = re.compile(r'[a-zA-Z]')
    value2 = ''.join(results)
    results2 = pattern2.findall(value2, 0, len(value2))
    print("Consonents: ", results2)

    return len(results2)


def count_vowels_consonents(value):
    return count_vowels(value) + count_consonents(value)


#count_vowels("abecdEi")
#count_consonents("abce13,45ay")

print("total count: ", count_vowels_consonents("abcioQEZI $yx,;"))
