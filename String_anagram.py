#Author = Vignesh Goutham

def detect_anagram(s1,s2):      #Sorting requires O(nlogn) as it uses merge sort
    s1.sort()                   # Algorithm runs as O(n logn)
    s2.sort()

    if s1 == s2:
        print("Its an Anagram")
    else:
        print("Its not an anagram")


def detect_anagram_v2(s1,s2):       #uses O(n) linear time, as we use three different for loops not nested
    list_s1=[0]*26                  #ord("a") is 97 and minusing it will point to the location of the list
    list_s2=[0]*26                  # Better than using count, as count function is O(n) by itself
    for item in s1:
        position = ord(item)-ord('a')
        list_s1[position] += 1

    for item in s2:
        position = ord(item)-ord('a')
        list_s2[position] += 1

    for index in range(len(list_s1)):
        if list_s1[index] != list_s2[index]:
            return False
    return True

if __name__ == "__main__":
    Result = detect_anagram_v2("abcd","dacb")
    print(Result)