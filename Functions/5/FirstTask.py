def power(a, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(a, -n)
    return a * power(a, n - 1)

a = 15
n = 2
result = power(a, n)
print(f"{a}^{n} = {result}")