with open('data.txt', 'w', encoding='utf-8') as file:
    l1 = input("Введіть перший рядок: ")
    l2 = input("Введіть другий рядок: ")
    l3 = input("Введіть третій рядок: ")
    file.write(l1 + '\n')
    file.write(l2 + '\n')
    file.write(l3 + '\n')