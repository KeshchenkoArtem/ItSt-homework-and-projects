width = int(input("Введіть ширину дошки: "))
height = int(input("Введіть висоту дошки: "))
s1 = input("Введіть перший символ: ")
s2 = input("Введіть другий символ: ")

for x in range(height):
    row = ""
    for y in range(width):
        if (x + y) % 2 == 0:
            row += s1
        else:
            row += s2
    print(row)