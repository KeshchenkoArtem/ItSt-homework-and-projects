def remover(numbers, value):
    count = 0
    while value in numbers:
        numbers.remove(value)
        count = count + 1
    return count

lst = [10, 72, 3, 2, 72, 2, 15]
remove = int(input(f"Введіть число для видалення зі списку {lst}: "))
deleted = remover(lst, remove)

print(f"Видалено {deleted} елементів.")