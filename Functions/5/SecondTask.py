def rec_sum(a, b):
    if a > b:
        return 0
    return a + rec_sum(a + 1, b)

a = 1
b = 5
result = rec_sum(a, b)
print(f"Діапазоні від {a} до {b} становить {result}")