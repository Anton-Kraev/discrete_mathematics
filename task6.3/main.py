all_ = 0
good = 0
for x1 in range(2, 23, 2):
    for x2 in range(2, 23, 2):
        for x3 in range(2, 23, 2):
            all_ += 1
            if x1 + x2 + x3 > 56:
                good += 1
print(good, all_)
