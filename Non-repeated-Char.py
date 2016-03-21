#Author = Vignesh Goutham

def getNonRepeatChar(string1):
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


if __name__ == "__main__":
    getNonRepeatChar("vignesh")
