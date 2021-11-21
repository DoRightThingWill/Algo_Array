def get_arrangements(array):
    arrangement_list = []
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j:
                arrangement_list.append([array[i], array[j]])
    
    return arrangement_list

array = [1,2,3,4,5]

print(get_arrangements(array))
print('len', len(get_arrangements(array)))


