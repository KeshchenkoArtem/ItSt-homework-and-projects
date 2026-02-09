def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

lst = [5, 1, 2, 4]
print(multiply(lst))