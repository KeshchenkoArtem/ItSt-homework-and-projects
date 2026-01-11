input_data = "Молоко:2:45, Хліб:1:20, реклама:0:0, Яблука:3:30, Сир:1:-10, Кола:2:25"

items_raw = input_data.split(",")
items = []

for item in items_raw:
    parts = item.strip().split(":")
    if len(parts) == 3:
        name = parts[0].strip().lower()
        qty = int(parts[1])
        price = int(parts[2])
        items.append([name, qty, price])

clean_items = []
for name, qty, price in items:
    if price <= 0:
        continue
    if "реклама" in name or "акція" in name:
        continue
    clean_items.append([name, qty, price])

menu = (
    "\n--- Smart Shopping Assistant ---\n"
    "1) Показати список\n"
    "2) Додати товар\n"
    "3) Видалити товар\n"
    "4) Загальна вартість\n"
    "5) Очистити все\n"
    "6) Вихід\n"
    "Введіть потрібний варіант (1-6): "
)

while True:
    choice = input(menu)

    if choice == "6":
        print("Вихід з програми...")
        break

    elif choice == "1":
        print("\n--- Список товарів ---")
        if not clean_items:
            print("\tСписок порожній!")
        else:
            for i, (name, qty, price) in enumerate(clean_items, start=1):
                print(f"\t{i}) {name} - {qty} шт. по {price} грн")

    elif choice == "2":
        new_item = input("Введіть товар у форматі назва:кількість:ціна: ")
        parts = new_item.strip().split(":")
        if len(parts) == 3:
            name = parts[0].strip().lower()
            qty = int(parts[1])
            price = int(parts[2])
            if price > 0 and "реклама" not in name and "акція" not in name:
                clean_items.append([name, qty, price])
                print("\tТовар додано!")
            else:
                print("\tНекоректний товар!")
        else:
            print("\tФормат неправильний!")

    elif choice == "3":
        idx = int(input("Введіть номер товару для видалення: "))
        if 1 <= idx <= len(clean_items):
            removed = clean_items.pop(idx - 1)
            print(f"\tВидалено: {removed[0]}")
        else:
            print("\tНевірний номер!")

    elif choice == "4":
        total = sum(qty * price for _, qty, price in clean_items)
        print(f"\n--- Загальна вартість ---\n\t{total} грн")

    elif choice == "5":
        clean_items.clear()
        print("\tСписок очищено!")

    else:
        print("\tНевірний вибір!")