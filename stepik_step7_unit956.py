n = int(input())
d = {}
for i in range(n):
    key = int(input())
    if key in d:
        print(d[key])
    else:
        value = f(key)
        print(value)
    d.setdefault(key, value)