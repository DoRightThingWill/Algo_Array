def get_full_permutation(array):
    rtn_list = []
    # permutation = []
    # permutation_helper(array, 0, rtn_list, permutation)
    permutation_helper(array, 0, rtn_list)

    return rtn_list

# def permutation_helper(array, cur_idx, rtn_list, permutation):
def permutation_helper(array, cur_idx, rtn_list):
    # base case: reach the bottom of the recursion tree
    # so here, cur_idx is the level of the recursion tree, and also the moving pointer
    # of the input array
    if cur_idx == len(array):
        # permu_copy =  permutation[:]
        new_arr = array[:]

        # rtn_list.append(permu_copy)
        rtn_list.append(new_arr)
        return

    for idx in range(cur_idx, len(array)):
        # take this value
        swap(array, idx, cur_idx)
        # permutation_helper(array, cur_idx + 1, rtn_list, permutation)
        permutation_helper(array, cur_idx + 1, rtn_list)

        # take next value
        # kick out the value you just added, and enter next iteration
        # permutation.pop()
        swap(array, idx, cur_idx)

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

# kick out the already-taken value
# use idx to control the array range of values to be taken


arr0 = [1,2]
arr1 = [1,2,3]
arr2 = [1,2,3,4]
arr3 = [1,2,3,4,5]

print("********************************")
print('len arr-->', len(arr0))
print(get_full_permutation(arr0))
rtn = get_full_permutation(arr0)
print("qty permutation-->", len(rtn))
print("********************************")
print('len arr-->', len(arr1))
print(get_full_permutation(arr1))
rtn = get_full_permutation(arr1)
print("qty permutation-->", len(rtn))
print("********************************")
print('len arr-->', len(arr2))
print(get_full_permutation(arr2))
rtn = get_full_permutation(arr2)
print("qty permutation-->", len(rtn))
print("********************************")
print('len arr-->', len(arr3))
print(get_full_permutation(arr3))
rtn = get_full_permutation(arr3)
print("qty permutation-->", len(rtn))
