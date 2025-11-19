import random

print("Привіть! Вітаємо тебе в нашій матиматичній грі!"
      "\nВ цій грі ми перевіримо наскільки гарно ти знаєш математику!"
      "\nУспіхів тобі в цих голодних іграх!")

#Запит до користувача, чи розпочинаємо гру ?
user_answer_to_start = ""
while True:
    user_answer_to_start = input("Ти готовий розпочати? (Введи Так або Ні): ")
    if user_answer_to_start == "Так":
        break
    elif user_answer_to_start == "Ні":
        print("Слабачок!")
        exit()
    else:
        print("Команду не розпізнано")

#Вибір користувачем рівню складності
print("\nРаді вашому рішенню, тепер виберіть уровень складності:\n"
      "1) Легкий(5 запитань)\n"
      "2) Середній(10 запитань)\n"
      "3) Важкий(15 запитань)\n")
user_choice = 0
difficulty = 0
while True:
    user_choice = input("Який рівень оберете(Введіть 1, 2 або 3): ")
    if user_choice == "1" or user_choice == "2" or user_choice == "3":
        difficulty = int(user_choice)*5
        break
    else:
        print("Команду не розпізнано\n")

# Обчислення балів
score = 0
wrong_streak = 0
feedback = []
#Початок гри
for num_question in range(1,difficulty + 1):
    type_question = random.randint(1, 4)
    if type_question == 1:
        num_1 = random.randint(1, 10)
        num_2 = random.randint(1, 10)
        num_3 = random.randint(1, 10)
        min_or_max = random.choice(["мінімальне", "максимальне"])
        question_text = f"Знайдіть {min_or_max} число серд наступних {num_1}, {num_2}, {num_3}: "
        print(question_text)

        #Знаходження правильної відповіді
        if min_or_max == "мінімальне":
            correct_answer = num_1
            if correct_answer > num_2:
                correct_answer = num_2
            if correct_answer > num_3:
                correct_answer = num_3
        else:
            correct_answer = num_1
            if correct_answer < num_2:
                correct_answer = num_2
            if correct_answer < num_3:
                correct_answer = num_3

        user_answer = int(input("Введіть вашу відповідь: "))
        if user_answer == correct_answer:
            print(f"Відповідь правильна, число {user_answer} є {min_or_max}!\n")
            feedback.append(f"{question_text} Ваша відповідь {user_answer}, правильна відповідь {correct_answer}")
            score += 1
            wrong_streak = 0
        else:
            print(f"Відповідь не правильна, насправді правильне число {correct_answer}!\n")
            wrong_streak += 1
            feedback.append(f"{question_text} Ваша відповідь {user_answer}, правильна відповідь {correct_answer}")
            if wrong_streak == 2:
                score = 0
                print("Дві неправильні відповіді поспіль! Ваші бали обнулено.\n")
    elif type_question == 2:
        num_1 = random.randint(1, 10)
        num_2 = random.randint(1, 10)
        num_3 = random.randint(1, 10)
        question_text = f"Знайдіть середнє арифметичне з наступних чисел: {num_1}, {num_2}, {num_3}: "
        print(question_text)

        # Знаходження правильної відповіді
        correct_answer = int((num_1 + num_2 + num_3) / 3)

        user_answer = int(input("Введіть вашу відповідь: "))
        if user_answer == correct_answer:
            print(f"Відповідь правильна, число {user_answer} є правильним!\n")
            feedback.append(f"{question_text} Ваша відповідь {user_answer}, правильна відповідь {correct_answer}")
            score += 1
            wrong_streak = 0
        else:
            print(f"Відповідь не правильна, правильна відповідь {correct_answer}!\n")
            wrong_streak += 1
            feedback.append(f"{question_text} Ваша відповідь {user_answer}, правильна відповідь {correct_answer}")
            if wrong_streak == 2:
                score = 0
                print("Дві неправильні відповіді поспіль! Ваші бали обнулено.\n")
    elif type_question == 3:
        num = random.randint(100, 1000)
        percent = random.randint(1, 50)
        question_text = f"Знайдіть {percent}% з числа {num}"
        print(question_text)

        # Знаходження правильної відповіді
        correct_answer = int((num * percent) / 100)

        user_answer = int(input("Введіть вашу відповідь: "))
        if user_answer == correct_answer:
            print(f"Відповідь правильна, число {user_answer} є правильним!\n")
            feedback.append(f"{question_text} Ваша відповідь {user_answer}, правильна відповідь {correct_answer}")
            score += 1
            wrong_streak = 0
        else:
            print(f"Відповідь не правильна, правильна відповідь {correct_answer}!\n")
            wrong_streak += 1
            feedback.append(f"{question_text} Ваша відповідь {user_answer}, правильна відповідь {correct_answer}")
            if wrong_streak == 2:
                score = 0
                print("Дві неправильні відповіді поспіль! Ваші бали обнулено.\n")
    elif type_question == 4:
        num = random.randint(1, 10)
        degree = random.randint(0, 3)
        question_text = f"Піднесіть {num} до {degree} степіня: "
        print(question_text)

        # Знаходження правильної відповіді
        correct_answer = num ** degree

        user_answer = int(input("Введіть вашу відповідь: "))
        if user_answer == correct_answer:
            print(f"Відповідь правильна, число {user_answer} є правильним!\n")
            feedback.append(f"{question_text} Ваша відповідь {user_answer}, правильна відповідь {correct_answer}")
            score += 1
            wrong_streak = 0
        else:
            print(f"Відповідь не правильна, правильна відповідь {correct_answer}!\n")
            wrong_streak += 1
            feedback.append(f"{question_text} Ваша відповідь {user_answer}, правильна відповідь {correct_answer}")
            if wrong_streak == 2:
                score = 0
                print("Дві неправильні відповіді поспіль! Ваші бали обнулено.\n")
print(f"Ваші бали становлять {score}\n")
print("Результати:")
for l in feedback:
    print(l)