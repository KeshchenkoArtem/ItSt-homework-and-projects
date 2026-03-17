try:
    num1 = float(input("Перше число: "))
    num2 = float(input("Друге число: "))
    result = num1 / num2
    print(result)

except ValueError as ValueError:
    print(f"Error: {ValueError}")
except ZeroDivisionError:
    print("Error: Division by zero is impossible.")
finally:
    print("Finally")