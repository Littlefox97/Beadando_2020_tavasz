import numpy as np


def vizsgal(fmatrix, m):
    for i in fmatrix:
        sor = np.sort(i)
        sor_forditott = np.sort(i)[::-1]
        if not np.array_equal(i, sor) and not np.array_equal(i, sor_forditott):
            return False

    for i in range(m):
        oszlop = fmatrix[:, i]
        oszlop_rendezett = np.sort(fmatrix[:, i])
        oszlop_forditott = np.sort(fmatrix[:, i])[::-1]
        if not np.array_equal(oszlop, oszlop_rendezett) and not np.array_equal(oszlop, oszlop_forditott):
            return False

        return True

bemenet = input("Adja meg a sort és oszlopot: ").split(" ")
N = int(bemenet[0])
M = int(bemenet[1])

matrix = np.random.randint(0, 25, (N, M))
print(vizsgal(matrix, M))
#matrix = np.array([[5, 3, 1, 1], [8, 2, 1, 0], [12, 2, 0, 0]])
#print(vizsgal(matrix, M))
