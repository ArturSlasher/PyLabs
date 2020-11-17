def writeback(n1, n2=0): #n2 по умолчанию = 0
    n2 *= 10
    n2 += n1 % 10
    if (n1//10 < 1):
        # если дошли до первой цифры
        return n2
    else:
        # рекурсия
        return writeback(n1//10, n2)

a = 1234
print(writeback(a))