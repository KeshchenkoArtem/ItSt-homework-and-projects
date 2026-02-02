def degree_list(lst, degree):
    result = []
    for num in lst:
        num = num ** degree
        result.append(num)
    return result

lst = [9, 7, 6, 4]
degree = int(input(f"Введіть степінь до котрого будуть підведені всі числа з списку {lst}: "))

new_lst = degree_list(lst, degree)
print(f"Список у {degree} степені: {new_lst}")