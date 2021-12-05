from math import factorial

k = 4
n = 16
res = 0  # res = S(n, k) - stirling number 2nd kind

for j in range(k + 1):
    res += ((-1) ** (k + j)) * (j ** n) * (factorial(k) / (factorial(j) * factorial(k - j)))
res /= factorial(k)

print(int(res))
