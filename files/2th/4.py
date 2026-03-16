with open('file1.txt', 'r', encoding='utf-8') as f1, open('file2.txt', 'r', encoding='utf-8') as f2, open('merged_alternate.txt', 'w', encoding='utf-8') as fTo:
    while True:
        l1 = f1.readline()
        l2 = f2.readline()
        if l1 != "":
            fTo.write(l1)
        if l2 != "":
            fTo.write(l2)
        if l1 == "" and l2 == "":
            break