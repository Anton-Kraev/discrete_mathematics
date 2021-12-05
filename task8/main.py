from math import *
from itertools import *

districts = [str(x) for x in range(57)]
districts.append('a')
districts.append('b')
districts.append('c')

all_options = 0
good_options = 0

options = list(combinations(districts, 6))
for option in options:
    for i in range(6):
        if option[i] in 'abc':
            good_options += 1
            break
    all_options += 1

print(good_options / all_options)
