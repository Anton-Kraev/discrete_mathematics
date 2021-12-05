from itertools import *

data = []

for x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13 in product('AUGC', repeat=13):
    s = x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10 + x11 + x12 + x13
    if not ('UAA' in s or 'UAG' in s or 'UGA' in s):
        data.append(x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10 + x11 + x12 + x13)

print(len(data) * 3)
