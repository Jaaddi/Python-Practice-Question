def picture(num):
    for i in range(-num, 0): # loop will go up to -5 to 1 and all times negative value changes to positive and in this way we get value from -5 to 0
        print(-i * "*")
        if i == -1: # When i == -1 then it will pick inner loop and do all work with that and 
            for j in range(1, num + 1):
                print(j * "*")
            break # IT will break after 1st hydration of first loop
num = int(input("Enter the Picture value"))
picture(num)            
