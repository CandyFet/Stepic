start = int(input())
m = []
for i in range(start):
    j = 0
    while j < i+1:
        m.append(i+1)
        j += 1
    if len(m) > start:
        break
m = m[0:start]
for i in m:
    print(i, end=" ")