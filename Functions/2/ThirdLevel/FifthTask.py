def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

numbers = [1, 12, 233, 25, 11, 17, 1233]

for n in numbers:
    result = is_prime(n)
    print(f"{n} просте число? {result}")