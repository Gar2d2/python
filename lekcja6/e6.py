import numpy as np  
def funkcja(s1, s2, s3):
    mat = np.empty((4,4), dtype="str")
    for i in range(len(s2)):
        mat[i][i] = s2[i]
    for i in range(3):
        mat[i+1][0] = s1[i]
    for i in range(3):
        mat[0][i+1] = s3[len(s3)-1 -i]

    return mat

s1 = "kot"
s2 = "pies"
 
print(funkcja("kot", "pies", "koń"))