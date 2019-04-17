def array_addition(arr):

    # get largest number and remove it from array
    goal = max(arr)
    arr.remove(goal)

    # powser set
    sets = [[]]

    for num in arr:
        for idx in range(0, len(sets)):
            temp = sets[idx] + [num]
            sets.append(temp)
            if sum(temp) == goal:
                return True

    return False


array = [1, 3, 3, 5, 6]

print(array_addition(array))

