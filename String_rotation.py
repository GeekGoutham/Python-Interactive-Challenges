#Author = Vignesh Goutham

def is_substring(s1, s2):           #Will check if s1 is in s2
    return (s1 in s2)


def is_rotation(s1, s2):
    if s1 is None or s2 is None:
        return False
    if len(s1) != len(s2):
        return False
    return is_substring(s2,s1+s1)       #If you add another s1 to s1, and just check if the other string is in that big string, then we say
                                        #it is a string rotation. We build a string so that rotation may not be needed.

def is_rotation_v2(s1, s2):                     #Wont work if there are the same characters in the same word!
    first_char_s2 = s2[0]
    index_fchar_s1 = s1.find(first_char_s2)
    if (index_fchar_s1 == -1):
        return False
    else:
        build_string = s1[index_fchar_s1:]
        build_string += s1[:index_fchar_s1]
        print(build_string)
        if (s2 == build_string):
            return True
        else:
            return False



if __name__ == "__main__":
#    result = is_rotation("foobaz","bazbarfoo")
    result_V2 = is_rotation_v2("ierint","intier")
    print(result_V2)