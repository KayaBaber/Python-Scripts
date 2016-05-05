def diag(matrix,offset):
    diagonal=[]
    for i in range(len(matrix)-abs(offset)):
        print i
        if offset > 0:
            diagonal.append(matrix[i][i+offset])
        else:
            diagonal.append(matrix[i-offset][i])
    return diagonal

N=10
matrix = [range(0,N)]*N
print matrix

d = diag(matrix, -1)
print d