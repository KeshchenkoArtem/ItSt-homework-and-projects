my_list = []

while True:
    word = input("Введіть число (або пустий рядок для завершення): ")
    if word == "":
        break
    elif not word.isnumeric():
        print("Вводіть тільки числа")
    else:
        my_list.append(int(word))

even_count = 0
odd_count = 0

for i in range(len(my_list)):
    if my_list[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Кількість парних: {even_count}. Кількість непарних: {odd_count}.")