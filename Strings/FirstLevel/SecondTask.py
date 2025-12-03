print("Паліндром — слово або текст, що читається однаково зліва направо і справа наліво.")

certain_text = input("Введіть паліндром: ")

if certain_text.lower() == certain_text.lower()[::-1]:
    print(f"Так, \"{certain_text}\" є паліндромом!")
else:
    print(f"Ні, \"{certain_text}\" не є паліндромом!")
