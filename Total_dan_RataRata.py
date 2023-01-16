n = []
t = 0

N = int(input())

for i in range(N):
    nilai = float(input("{}. ".format(i+1)))
    n.append(nilai)

print("\nHasil nilai total adalah : {}".format(sum(n)))

print("Hasil Rata - Rata Adalah : {}".format(sum(n)/N))
