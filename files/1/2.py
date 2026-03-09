import os

if os.path.exists('data.txt'):
    print(f"Файл 'data.txt' знайдено.")
    with open('data.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines[1::2]:
            print(line.strip())
else:
    print(f"Файл 'data.txt' не знайдено.")