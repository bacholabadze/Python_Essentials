ans = input("Enter your date of birth (format YYYYDDMM):  ")


def digitOfLife(num):
    digit_sum = 0
    for n in num:
        digit_sum += int(n)

    if len(str(digit_sum)) == 1:
        return digit_sum
    else:
        return digitOfLife(str(digit_sum))


print(digitOfLife(ans))
