def produce_all_sets(array):
    rtn_list = []
    for i in range(len(array) - 1):
        for j in range(i+1, len(array)):
            rtn_list.append([array[i], array[j]])
    
    return rtn_list


array = [1,2,3,4,5]

print(produce_all_sets(array))
# the length of rtn_list should be nC2 = n * (n - 1) / 2
print('len', len(produce_all_sets(array)))