def odd_even(rnge):
    a = []
    b = []
    c = []
    counter = -1
    countera = 0
    for i in range(1, rnge + 1):
        if i % 2 == 1:
            a.append(i)
        if i % 2 == 0:
            b.append(i)
    for j in a:
        c.append(j)
    for k in b:
        c.append(k)
    print(c)
    c.insert(4, 42)
    print("After inseting value in the list at 4 index : ",c)
    for z in 7, 8, 9:
        c.append(z)
    print("After Adding three values at last : ",c)
    for k in 0, 1:
        print("Vales : ",c[k])
    for u in b:
        counter += 1
    print("Last Element of list b : ",b[counter])
    for y in a:
        countera += 1
    print("Length of list a : ",countera)
odd_even(6)

