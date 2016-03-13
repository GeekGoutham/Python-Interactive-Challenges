#Author = Vignesh Goutham

def string_permutations(String1, String2):          # Algorithm has 3 for loops -- Will reduce time drastically
    char_string1 = []
    char_string2 = []
    for char in String1:
        char_string1.append(char)
    for char in String2:
        char_string2.append(char)
    print(char_string1)
    print(char_string2)
    for check_char in char_string1:
        if check_char not in char_string2:
            return False
    return True


def string_permutations_v2(String1, String2):
    if len(String1) != len(String2):
        return False                                            #Single for loop -- better O(n)
    for char in String1:
        if char not in String2:
            return False
    return True

def string_permutations_v3(String1, String2):       # sort uses merge sort with O(n log n) -- Bad compared to O(n)
    sort_string1 = sorted(String1)
    sort_string2 = sorted(String2)
    if sort_string1 == sort_string2:
        return True
    else:
        return False



if __name__ == "__main__":
    print(string_permutations_v2("act","cAt"))