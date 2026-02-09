def lucky_num(num):
    num_str = str(num)
    first_h = int(num_str[0]) + int(num_str[1]) + int(num_str[2])
    second_h = int(num_str[3]) + int(num_str[4]) + int(num_str[5])
    return first_h == second_h

n = 123420
print(f"{n} це щасливе число ? {lucky_num(n)}")