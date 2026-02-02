def find_min(numbers):
    min = numbers[0]
    for num in numbers:
        if num < min:
            min = num
    return min

lst = [9, 3, 31, 0, -13]
print(find_min(lst))