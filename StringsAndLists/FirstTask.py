my_list = []

while True:
    word = input("Введіть число (або пустий рядок для завершення): ")
    if word == "":
        break
    elif not word.isnumeric():
        print("Вводіть тільки числа")
    else:
        my_list.append(int(word))

count = 0
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i - 1]:
        count += 1

print(f"Кількість елементів: {count}")