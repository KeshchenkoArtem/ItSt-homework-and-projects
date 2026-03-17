nums = [56, 34, 23, 12, 75]
print(f"from: {nums}")
try:
    user_input = input("Індекс елемента: ")
    idx = int(user_input)
    el = nums[idx]
    print(el)

except ValueError as ValueError:
    print(f"Error: {ValueError}.")
except IndexError:
    print(f"Error: Індекс {idx} не існує.")
finally:
    print("Finally")