#Author = Vignesh Goutham

def string_reverse(charlist):
    if charlist == None:                        #strings are immutable in python, we cant do a strict in-place string reverse
        print("No character array sent")        #In-place algo = where the input is changed to output and a new memory/variable for o/p is not created
        return False                            #in-place is distructive as it destroys the input
    current = 0
    far_current = len(charlist)-1
    while(current != far_current):
        charlist[current],charlist[far_current] = charlist[far_current], charlist[current]
        current += 1
        far_current -= 1
    print(charlist)

def string_reverse_v2(string1):  #Pythonic way to do with strings  (Not in-place)
    if string1 == None:
        print("No string to reverse")
        return False
    else:
        print(string1[::-1])

def string_reverse_v3(string1):         #Using reversed method -- (Not in-place)
    if string1 == None:
        print("No string to return")
    else:
        rev = reversed(string1)
        print("".join(rev))


if __name__ == "__main__":
    charlist = ['v','i','g','n','e','s','h']
    print(charlist)
    string_reverse(charlist)
    print("=====================")
    string_reverse_v2("Vignesh")
    string_reverse_v3("vignesh")