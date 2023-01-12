x = "AAAAAHHGNNNNNIIIKKKKKFQQQWEROOOR"


def rle(x):
    char = x[0]
    count = 0
    result = ''
    for i in x:
        if i == char:
            count += 1
            continue
        result += char + str(count)
        char = i
        count = 1
    result += char + str(count)
    return result


print(rle(x))
