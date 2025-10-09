def quicksort(arr):
    if (len(arr) < 2):
        return arr
    pivot = arr.pop(0)
    left_arr = []
    rigth_arr = []
    for item in arr:
        if item < pivot or item == pivot:
            left_arr.append(item)
        else :
            rigth_arr.append(item)

    return quicksort(left_arr) + [pivot] + quicksort(rigth_arr)


arr = [12, 43, 34, 67, 67, 86, 34, 3]
print(quicksort(arr))