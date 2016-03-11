#Author = Vignesh Goutham

def check_unique_dict(string_input):             #Implmented using dict -- Poor performance as you need to check if there is more than one entry
    char_dict = {}                                  #Still O(n) but dict takes more space then list
    for character in string_input:
        if character in char_dict.keys():
            flag = False
            return False
        else:
            char_dict[character] = 1
 #    print(char_dict)
    return True

def check_unique_list(string_input):   #Better than dict implementation : Still O(n) complexity
    string_check_list=[]
    for character in string_input:
        if character in string_check_list:
            return False
        else:
            string_check_list.append(character)
    return True

def check_unique_set(string_input):  #O(n) as well -- better algorithm using set() -- set does not allow duplicates.
    return len(set(string_input)) == len(string_input)


if __name__ == '__main__':
    string_input = input("Enter the string needed to be checked :  ")
    result = check_unique_list(string_input)
    print(str(result))