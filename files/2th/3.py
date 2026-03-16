fNames = ['file1.txt', 'file2.txt', 'file3.txt']
with open('merged.txt', 'w', encoding='utf-8') as fTo:
    for fName in fNames:
        fTo.write(f"{fName}\n\n")
        with open(fName, 'r', encoding='utf-8') as fFrom:
            content = fFrom.read()
            fTo.write(f"{content}\n\n")