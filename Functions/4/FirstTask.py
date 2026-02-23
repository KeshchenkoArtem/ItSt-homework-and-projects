def digits_forward(n):
    if n < 0:
        n = -n
    if n < 10:
        print(n, end=" ")
    else:
        digits_forward(n // 10)
        print(n % 10, end=" ")

number = -2345435
print(number)
digits_forward(number)