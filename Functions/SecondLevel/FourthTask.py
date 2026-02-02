def primes_count(numbers):
    total = 0
    for num in numbers:
        if num > 1:
            divisors = 0
            for i in range(1, num + 1):
                if num % i == 0:
                    divisors = divisors + 1
            if divisors == 2:
                total = total + 1
    return total

lst = [1, 2, 3, 4, 5, 6, 7]
print(primes_count(lst))