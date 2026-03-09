name = input("Введіть ім'я файлу: ")
with open(name, 'r', encoding='utf-8') as file_from, open('cleaned.txt', 'w', encoding='utf-8') as cleaned:
    txt = file_from.read()
    clean_txt = ""
    for char in txt:
        if not char.isdigit():
            clean_txt = clean_txt + char
    cleaned.write(clean_txt)