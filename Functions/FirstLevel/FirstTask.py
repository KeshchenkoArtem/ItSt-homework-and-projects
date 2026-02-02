def sum_in_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end + 1))

print(sum_in_range(1, 13))