a = int(input())
b = int(input())

nums = []
for num in range(a, b+1):
    if num % 2 == 0:
        nums.append(str(num))

print(" ".join(nums))
