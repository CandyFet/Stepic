from collections import Counter
c = Counter(input().lower().split())
for k in c:
    print(k, c[k])