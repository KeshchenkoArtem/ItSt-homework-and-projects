my_list = []

while True:
    word = input("Введіть число (або пустий рядок для завершення): ")
    if word == "":
        break
    elif not word.isnumeric():
        print("Вводіть тільки цілі числа")
    else:
        my_list.append(int(word))

if len(my_list) > 0:
    min_value = min(my_list)
    max_value = max(my_list)

    for i in range(len(my_list)):
        if my_list[i] < min_value:
            min_value = my_list[i]
        if my_list[i] > max_value:
            max_value = my_list[i]

    print(f"Мінімальне значення у списку: {min_value}. Максимальне значення у списку: {max_value}.")
else:
    print("Список порожній.")