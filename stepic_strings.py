def substring_counting(substring):
    length = len(substring)
    sub_builder = substring[0] + str(length)  # type: string
    return sub_builder


string = 'asdasd'
i = 0
k = len(string) - 1
substring = ''
res_string = ''
while i < k:
    if string[i] == string[i - 1]:
        substring = substring + string[i]
        i += 1
    if string[i] != string[i - 1] and i != 0:
        substring = substring + string[i]
        res_string = res_string + substring_counting(substring)
        substring = ''
        i += 1
    if i == 0:
        substring = substring + string[i]
        i += 1
    if string[i] != string[i - 1] and i-1 == 0:
        res_string = res_string + substring_counting(substring)
        substring = ''
print(res_string)
