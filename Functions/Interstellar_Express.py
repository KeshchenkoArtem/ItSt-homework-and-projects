def calculate_delivery(user_input):
    parts = user_input.split(":")
    name = parts[0].strip()
    base_cost = float(parts[1].replace("грн", ""))
    distance = float(parts[2])

    tax_bonus = 0
    for char in name:
        if char.isdigit():
            tax_bonus += int(char)
        if char == "$":
            tax_bonus += 100
    delivery_cost = base_cost
    if distance > 1000:
        delivery_cost *= 1.5
    penalty = 0
    if "небезпечний" in name.lower():
        penalty = 500
    discount = 0
    if name.upper().startswith("A"):
        discount = delivery_cost * 0.1
    total_price = delivery_cost + tax_bonus + penalty - discount

    return f"ВАНТАЖ: {name.upper()} | ЦІНА: {total_price} | БОНУС: {tax_bonus}"

print(calculate_delivery("Arduino $2.5:700грн:600"))