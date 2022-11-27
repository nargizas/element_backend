num = input()

l = len(num)
num = num[::-1]
res = 0
for i in range(l):
    if num[i] == '1':
        res += 2 ** i

print(res)
