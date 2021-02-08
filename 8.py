def check_list(l_1, l_2):
    c_1 = 0
    c_2 = 0
    for i in l_1:
        c_1 += 1
    for j in l_2:
        c_2 += 1
    for k in range(0, c_1):
        for z in range(0, c_2):
            if l_1[k] == l_2[z]:
                return True
                break
l_1 = [2, 2, 3, 4, 5]
l_2 = [6, 6, 7, 8, 2]
check_list(l_1, l_2)
