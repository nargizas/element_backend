def double_power(a, b):
    return a ** b


a, b = input().split()
res = double_power(int(a), int(b))

print(res)
