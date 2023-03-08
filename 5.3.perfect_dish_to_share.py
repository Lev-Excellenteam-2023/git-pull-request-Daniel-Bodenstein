def perfect_dish_to_share_5_3():
    n = 6
    while (True):
        sum = 0
        for i in range(1, int(n / 2) + 1):
            if n % i == 0:
                sum += i
        if sum == n:
            yield n
        n = n + 1

#our_generator = perfect_dish_to_share_5_3()
#for item in our_generator:
#    print(item)