with open('data.txt', 'r', encoding='utf-8') as data, open('filtered.txt', 'w', encoding='utf-8') as filtered:
    for line in data:
        if "Python" in line:
            filtered.write(line)