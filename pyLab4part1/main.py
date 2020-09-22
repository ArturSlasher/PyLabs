def calcNextDate(day, month, year, isBig):
    if isBig: yearLen = 365
    else: yearLen = 364

    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        monthLen = 31
    else:
        if month==2:
            if (yearLen == 365):
                monthLen = 29
            else: monthLen = 28
        else:
            monthLen = 30

    if day == monthLen:
        if month == 12:
            month = 1
            year += 1
            day = 1
        else:
            day = 1
            month += 1
    else:
        if month == 12:
            if day == monthLen:
                month = 1
                year += 1
            else: day += 1
        else:
            day += 1

    return day, month, year

print(calcNextDate(31, 12, 2000, True))
