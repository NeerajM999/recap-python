def string_permutations(value):
    _string_permutations("",value)

def _string_permutations(perm, value):
    if value == "":
        print(str(perm) + str(value))

    else:
        for i in range(0, len(value)):
            _string_permutations(perm + value[i], value[0:i] + value[i+1:len(value)])

string_permutations("abc")

