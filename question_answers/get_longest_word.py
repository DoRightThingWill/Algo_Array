# [a, t, r, t, e, b, u], we have these letters
# and a given dictionary to store all available words in English
# you need to find which is the longest word that could be formed by the letters from the given collection

# we could use the trie structure.
# and how we could use it?
# 1. we use the trie structure in an abstract way.
# 2. that means, logically, we are SEARCHING each node
# in the trie structure, but we are not going to explicitly 
# build a trie structure.
# 3. why do we not need to build this trie structure??
# 4, when do we need to build this trie?
def get_all_words(array, dict=0):
    all_permutations = set()
    get_permutations(array, 0, all_permutations)
    return all_permutations
def get_permutations(array, idx, all_permutations):
    if idx == len(array):
        # new_array = array[:]
        # all_permutations.append(new_array)
        return
    
    for i in range(idx, len(array)):
        swap(array, idx, i)
        new_arr = tuple(array[:idx + 1])
        all_permutations.add(new_arr)
        get_permutations(array, idx + 1, all_permutations)
        swap(array, idx, i)

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

array= [1,2,3,4,5,6,7]
all_permu = get_all_words(array)
print(all_permu)
print('permu qty',len(all_permu))



