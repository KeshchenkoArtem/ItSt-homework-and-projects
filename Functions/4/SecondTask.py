def range_sum(min, max):
    if min > max:
        return range_sum(max, min)
    if min == max:
        return min
    return min + range_sum(min + 1, max)

min = 1
max = 10
range = range_sum(min, max)
print(f"Діапазон від {min} до {max}, сума: {range}")