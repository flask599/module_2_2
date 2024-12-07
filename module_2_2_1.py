print('Нули ничто, отрицание недопустимо!')
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(my_list):
    a = my_list[i]
    i = i + 1
    if a == 0:
        continue
    elif a < 0:
        break
    elif i == len(my_list):
        print(a)
    else:
        print(a)