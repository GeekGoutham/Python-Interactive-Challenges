#Author = Vignesh Goutham

def delCharString(String1, *charac):        #Complexity is O(n) append is O(n) but have 2 for loops-- must try to improve algorithm
    char_list = []
    for ch in range(0, len(String1)-1):
        char_list.append(String1[ch])
    for cha in charac:
        if cha in char_list:
            char_list.remove(cha)
    print(char_list)






if __name__ == "__main__":
    delCharString("Vignesh","i","n","s")