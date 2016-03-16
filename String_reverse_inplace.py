#Author = Vignesh Goutham

def string_reverse(charlist):
    if charlist == None:                        #strings are immutable in python, we cant do a strict in-place string reverse
        print("No character array sent")        #In-place algo = where the input is changed to output and a new memory/variable for o/p is not created
        return False                            #in-place is distructive as it destroys the input
    current = 0
    far_current = len(charlist)-1
    while(current != far_current):
        temp = charlist[current]
        charlist[current] = charlist[far_current]
        charlist[far_current] = temp
        current += 1
        far_current -= 1
    print(charlist)


if __name__ == "__main__":
    charlist = ['v','i','g','n','e','s','h']
    print(charlist)
    string_reverse(charlist)