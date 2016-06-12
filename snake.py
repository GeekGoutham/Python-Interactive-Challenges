#Author = Vignesh Goutham

def snake_matrix(body):
    output = list()
    temp = []
    output_L = max(body)
    output_H = len(body)
    if body[0] == output_L:
        temp.append("H")
        for i in range(output_L - 1):
            temp.append("x")
    else:
