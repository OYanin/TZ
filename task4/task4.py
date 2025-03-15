from sys import argv

try:
    path = argv[1]
except:
    print('Проблемы с доступом к файлу')

with open(path, "r") as f_digits:
    d_digits = [int(digit.replace('\n', '')) for digit in f_digits.readlines()]

cnt = 0

while not(all([sum(d_digits)/len(d_digits) == digit for digit in d_digits])):
    cnt += 1
    d_digits.sort()
    average = sum(d_digits)/len(d_digits)

    if average - d_digits[0] > d_digits[-1] - average:
        d_digits[0] += 1
    else:
        d_digits[-1] -= 1

print(cnt)