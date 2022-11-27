a = int(input())
res = []
for num in range(1, a+1):
    if a % num == 0:
        res.append(str(num))

print(" ".join(res))
