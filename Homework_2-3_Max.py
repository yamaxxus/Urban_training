my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
base = 0
while base < len(my_list):
    if my_list[base] < 0:
        break
    if my_list[base] > 0:
        print(my_list[base])
    base += 1