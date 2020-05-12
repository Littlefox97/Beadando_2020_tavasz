import numpy as np


def torol(vek):
    db = 0
    i = 0
    while i < len(vek):
        if i > 0 and vek[i] != vek[i - 1]:
            vek = vek[i:]
            i = 0
            db += 1
        i += 1

    vek = np.delete(vek, [i for i in range(len(vek))])
    db += 1
    return db


A = np.array([0, 1, 1, 1, 0])
print(torol(A))
#B = np.array([0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0])
#print(torol(B))