filename = input("Ім'я файлу: ")
target = input("Слово для пошуку: ")
with open(filename, 'r', encoding='utf-8') as file:
    txt = file.read()
    wLst = txt.split()
    wCount = 0
    for word in wLst:
        if word == target:
            wCount = wCount + 1
print(f"'{target}' зустрічається {wCount} разів.")