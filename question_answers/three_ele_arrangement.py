def get_arrangements(array) :
    arrangements = []

    for i in range(len(array)):
        for j in range(len(array)):
            for k in range(len(array)):
                x = array[i]
                y = array[j]
                z = array[k]
                if i != j and j != k and i != k:
                    arrangements.append([x,y,z])

    return arrangements

array = [1,2,3,4,5]

print(get_arrangements(array))

print('len',len(get_arrangements(array)))