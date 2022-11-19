a = int(input())
b = int(input())
c = int(input())

count = 0

if a == b:
    count += 1

if b == c:
    count += 1

if a == c:
    count += 1

print(count)
