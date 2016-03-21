#Author = Vignesh Goutham

def getNonRepeatChar(string1):              #Both algorithms have the same time complexity of O(n), but the lower v2 looks clean and might be having lesser space complexity
    chardict = {}
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
    for ch in string1:
        count = string1.count(ch)
        if count == 1:
            print(ch + " is the non-repeating first char")
            return




if __name__ == "__main__":
    getNonRepeatChar_v2("vsngivignesh")