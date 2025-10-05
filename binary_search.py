def binary_search():
    arrayn = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    searched = 12
    founded = False
    arrayb = arrayn

    while not founded:
        mid = len(arrayb) // 2
        try_guess = arrayb[mid] # i cannot do this, because it is a search instead
        # mid = (low + high) / 2

        if try_guess == searched:
            print("Founded")
            founded = True

        if try_guess < searched:
            arrayb = arrayb[mid:]
        else:
            arrayb = arrayb[:-mid]

binary_search();

# in tghe books version the professor choses the mid by suming the low more the highest
# element