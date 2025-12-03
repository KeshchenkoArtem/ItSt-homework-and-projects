certain_text = input("Введіть довільну кількість довільних речень: ")

def count_sentences(text):
    sentence = ".!?"
    count = 0
    for char in text:
        if char in sentence:
            count += 1
    return count

print(f"Кількість речень: {count_sentences(certain_text)}")