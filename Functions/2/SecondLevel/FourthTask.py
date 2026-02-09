def get_max(a, b, c, d):
    max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    if d > max_val:
        max_val = d
    return max_val

num1 = 22
num2 = 93
num3 = 23
num4 = 11

print(get_max(num1, num2, num3, num4))