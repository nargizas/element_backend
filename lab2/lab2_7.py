def election(x, y, z):
    count = 0
    if x:
        count += 1
    if y:
        count += 1
    if z:
        count += 1

    if count >= 2:
        return True

    return False


x, y, z = input().split()
res = election(int(x), int(y), int(z))
print(int(res))
