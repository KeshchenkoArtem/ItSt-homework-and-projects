def comb_lists(lst1, lst2):
    result = []
    for i in lst1:
        result.append(i)
    for i in lst2:
        result.append(i)
    return result

lst1 = [1, 2, 3]
lst2 = [10, 20]

combined = comb_lists(lst1, lst2)
print(combined)