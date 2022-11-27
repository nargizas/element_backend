a = int(input())
res = a
for num in range(2, a):
    if a % num == 0:
        res = num
        break

print(res)
