#Author = Vignesh Goutham
import math

def sqrt_vg(n):
    root = n/2
    for _x in range(10):
        root = (1/2) * (root + (n/root))                #Newton's algorithm
    print("Sqrt using newton's method: " + str(root))


if __name__ == "__main__":
    inp = int(input("Enter the number you want to find the sqrt of  "))
    sqrt_vg(inp)
    print("The sqrt using the sqrt function: " + str(math.sqrt(inp)))