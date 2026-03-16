with open('numbers.txt', 'r', encoding='utf-8') as numTxt, open('sum.txt', 'w', encoding='utf-8') as fTo:
    fileFrom = numTxt.read()
    numLst = fileFrom.split()
    tSum = 0
    for numStr in numLst:
        number = float(numStr)
        tSum = tSum + number
    fTo.write(str(tSum))