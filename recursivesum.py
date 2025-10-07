def recuyrsive_sum(array):
    if not array:
        return 0
    return array[0] + recuyrsive_sum(array[1:])


array = [2, 4, 6]
print(f"some: {recuyrsive_sum(array)}")