#Author = Vignesh Goutham

def compress_string(String1):
    print("Entered String = "+ String1)             #Maintain loop counter to find the number of occurance instead of using a dict
    counter = 0
    result = ""
    prev_char = String1[0]
    for char in String1:
        if char == prev_char:
            counter += 1
        else:
            result += prev_char + (str(counter) if counter > 1 else "")
            prev_char = char
            counter = 1
    result += prev_char + (str(counter) if counter > 1 else "")
    print(result)





if __name__ == "__main__":
    compress_string("AABBCCDDD")