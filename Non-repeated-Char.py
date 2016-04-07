#Author = Vignesh Goutham

def getNonRepeatChar(string1):              #The bottom algorithm is more good
    chardict = {}                           #Reading and witing to dict is O(1), but dict.keys() is O(n) -- so algorithm might be O(n^2)
    for ch in string1:
        if ch in chardict.keys():
            chardict[ch] += 1
        else:
            chardict[ch] = 1

    for ch in string1:
        count = chardict[ch]
        if count == 1:
            print(ch+ " is the first non-repeated character in the string")
            return
    print("No characters are non-repeated in the given string")


def getNonRepeatChar_v2(string1):
    for ch in string1:                              #Count in python is also O(n) --
        count = string1.count(ch)
        if count == 1:
            print(ch + " is the non-repeating first char")
            return

def getNonRepeatChar_v3(string1):           #not working properly with the xor -- but worked for numbers (integers)
    result = 0
    asc = [ord(ch) for ch in string1]
    print(asc)
    for ch in asc:
        result ^= ch
        print(result)
    res = chr(result)
    print(res)


if __name__ == "__main__":
    getNonRepeatChar_v3("vingvighnesh")
