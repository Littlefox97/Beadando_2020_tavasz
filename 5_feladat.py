n = int(input("Adja meg a pontok darabszámát: "))
pontok = [(-1, -1) for i in range(n)]
tavolsagok = [[-1 for i in range(n)] for _ in range(n)]
for i in range(n):
    koord = input("").split(" ")
    pontok[i] = (int(koord[0]), int(koord[1]))
    tavolsagok[i][i] = 0
    for j in range(i):
        tav = min(abs(pontok[i][0] - pontok[j][0]), abs(pontok[i][1] - pontok[j][1]))
        tavolsagok[i][j] = tavolsagok[j][i] = tav

print(tavolsagok)