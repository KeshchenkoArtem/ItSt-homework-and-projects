try:
    user_input = input("Введіть дані: ")
    prts = user_input.split()
    sList = []
    total = 0
    for i in prts:
        num = float(i)
        sList.append(num)
        total += num
    print(f"Отримано значень: {len(sList)}")
    print(f"Загальна сума: {total}")

except ValueError as ValueError:
    print(f"Error: {ValueError}.")
finally:
    print("Finally")