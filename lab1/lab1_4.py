start_time = 9 * 60
n = int(input())
time = start_time + n * 45
if n % 2 == 0:
    time += (n // 2 - 1) * (20) + 5
else:
    time += n // 2 * (20)

h = time // 60
m = time % 60
print(f"{h} {m}")
