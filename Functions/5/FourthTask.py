def leap_y(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def get_d_in_m(m, y):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if m in [4, 6, 9, 11]:
        return 30
    return 29 if leap_y(y) else 28

def days_between(d1, m1, y1, d2, m2, y2):
    if (d1, m1, y1) == (d2, m2, y2):
        return 0
    if (y1, m1, d1) > (y2, m2, d2):
        return days_between(d2, m2, y2, d1, m1, y1)
    if m1 != m2 or y1 != y2:
        d_in_m = get_d_in_m(m1, y1)
        days_remaining = d_in_m - d1 + 1
        next_m, next_y = m1 + 1, y1
        if next_m > 12:
            next_m, next_y = 1, y1 + 1
        return days_remaining + days_between(1, next_m, next_y, d2, m2, y2)
    return d2 - d1

print(days_between(31, 5, 2008, 2, 3, 2026))