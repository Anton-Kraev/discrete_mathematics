from math import factorial

sum1 = 0
sum2 = 0
res = 0

for i in range(5, 15):
    a = factorial(36) / (factorial(i) * factorial(36 - i))
    sum1 += a
for j in range(5, 11):
    b = factorial(20) / (factorial(j) * factorial(20 - j))
    sum2 += b
res = sum1 * sum2

print(int(res))
