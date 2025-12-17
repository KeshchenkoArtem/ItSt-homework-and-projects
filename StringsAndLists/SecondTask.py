my_list = []

while True:
    word = input("Введіть число (або пустий рядок для завершення): ")
    if word == "":
        break
    elif not word.isnumeric():
        print("Вводіть тільки числа")
    else:
        my_list.append(int(word))

unique_once = []
for num in my_list:
    if my_list.count(num) == 1:
        unique_once.append(num)

print(f"Елементи, що зустрічаються рівно один раз: {unique_once}")