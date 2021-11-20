def get_three_elements_subsets(array):
    subset_list = []
    for i in range(len(array) - 2):
        for j in range(i + 1, len(array) - 1):
            for k in range(j + 1, len(array)):
                subset_list.append([array[i], array[j], array[k]])
    return subset_list


array = [1,2,3,4,5]

print(get_three_elements_subsets(array))

print('len', len(get_three_elements_subsets(array)))