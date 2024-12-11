def n(number):
    result = ''
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                result += str(i) + str(j)
    return result

print('Введите число: ')
print(n(int(input())))