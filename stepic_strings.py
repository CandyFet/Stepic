string = 'abct'
i = 1
k = int(len(string) - 1)
substring = ''
result_string = ''
for symbol in string:
    if string.index(symbol) == 0 and string.index(symbol) != k:
        substring = substring + symbol
        len = string.index(symbol)
    if symbol == string[string.index(symbol) - 1] and string.index(symbol) != 0 and string.index(symbol) != k:
        substring = substring + symbol
        len = string.index(symbol)
    if symbol != string[string.index(symbol) - 2] and string.index(symbol) != k:
        result_string = result_string + string[string.index(symbol) - 1] + str(len(substring))
        substring = ''
        len = string.index(symbol)
    if string.index(symbol) == k:
        result_string = result_string + symbol + str(len(substring))
        len = string.index(symbol)
print(result_string)