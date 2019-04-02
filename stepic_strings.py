s = input()
cnt = 1
for i in range(len(s)-1):
	if s[i] == s[i+1]:
		cnt += 1
	else:
		print(s[i], end="")
		print(cnt, end="")
		cnt=1
print(s[-1], end="")
print(cnt, end="")