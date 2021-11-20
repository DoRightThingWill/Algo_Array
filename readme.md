## Couple of high frequency coding interview questions
* Depth First Search
* Recursion
* Back Track
* Sliding Window
* Double/Triple Pointers
* Dynamic Programming
* Greedy
## Typical Array Problem

* Get all subsets that contains two elements. The order of elements in the subset does not matter. Elements in the input array are distinct.
```python
def produce_all_sets(array):
    rtn_list = []
    for i in range(len(array) - 1):
        for j in range(1, len(array)):
            rtn_list.append([array[i], array[j]])
    
    return rtn_list

# [1, 2, 3, 4]
# [1, 2], [1, 3], [1, 4]
# [2, 3], [2, 4]
# [3, 4]
# since the j is always larger than index i, through this way, there will never be duplicate set appear, e.g., [1, 2], [2, 1]
```
* Get all subsets that contains Three elements. The order of elements in the subset does not matter. Elements in the input array are distinct.
```python
def get_three_elements_subsets(array):
    subset_list = []
    for i in range(len(array) - 2):
        for j in range(i + 1, len(array) - 1):
            for k in range(j + 1, len(array)):
                subset_list.append([array[i], array[j], array[k]])
    return subset_list

# [1,2,3,4,5]
# mathematically, the list should have nC3 elements
# similar with 2-elements-subsets, this approach will not generate duplicated 3-elements-sub-sets
# And, we could also use the same method to generate 4-elements subsets. 
# To avoid duplicates, the key is make inner loop index always larger than parent loop index by ONE. This way, the iteration will never look back.
# actually, 
```

* Get a group of arrays. Each array contains two elements (different index) from the input array. 
```python
# since this is array, the order matters
# [1,2,3]
# [1,2] [2,1] [1,3] [3,1] [2,3] [3,2]
def get_arrangements(array):
    arrangement_list = []
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j:
                arrangement_list.append([array[i], array[j]])
    
    return arrangement_list

#time complexity is O(n^2). And space complexity is O(n^2)

# similarly, we could get arrangements of 3 elements:

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
# it is easy to see the time complexity is O(n^3). And space complexity is O(n^3) too. Here, one important finding is: to generate a set, which means no duplicated index appear, like [array[1], array[2]], and [array[2], array[1]], we need to make sure: inner loop index is over outside loop index by ONE. This makes the loop never look back.

# While for arrangements or permutation, all loop iterates from head to end, skipping the same index.

```



* Get all the permutation of the input array. 
What if, we do not know the length of the input array and we need to make the full permutation? If the length is N, we need N level loops???? Of course. NO.

```python
# N level loops sounds crazy. Recursion will save our life. 
# Talk about recursion. We better look at it as a Tree (even a single line tree).
# For example, the input array is [1,2,3]. Use a tree to simulate the process of making
# permutations

#                                     []
#                                   /  |  \
#                                 /    |    \
#                                1     2     3
#                              / | \
#                             /  |   \
#                            2   3
#                           /    |
#                          3    2

# Oh, my god, ugly tree. Hope you could understand what I am doing.
# The height of the tree is len(array). How many leaves we have? len(array) ! . Factorial
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

    # we could use an extra list as the arrangement
    # or we could simply switch values in place in the original array
    if cur_idx == len(array):
        new_arr = array[:]
        rtn_list.append(new_arr)
        return

    for idx in range(cur_idx, len(array)):
        # take this value
        swap(array, idx, cur_idx)
        permutation_helper(array, cur_idx + 1, rtn_list)

        # take next value
        # kick out the value you just added, and enter next iteration
        swap(array, idx, cur_idx)

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

```

* Give a set of characters, return all strings that it could produce. For example, input set is ['a', 'b']. Then the output set could be '', 'a', 'b', 'ab', and 'ba'

```python
# [a, t, r, t, e, b, u], we have these letters
# and a given dictionary to store all available words in English
# you need to find which is the longest word that could be formed by the letters from the given collection

# I modified this question.
# Overall strategy is :
# find all words that we could make from the letter collection
# from long to short, for each word, check if it is in the dictionary
# assume checking existence in the dict is O(1)

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

# by nature, this approach is same with making full permutations, except that, for this method, we need to make words by combining the letters from each node to the root node, rather than in the second method, where we only need to combine letters between root node and leaf nodes.
```

* generate **power set**

```python
# consider a simple scenario:
# power set of [1,2] is [[], [1], [2], [1,2]] (2^n elements)
# if we have one extra element 3, how could we generate power set of [1,2,3] by using power set of [1,2] and [3]
# right, we iterate the power set of [1,2], and for each list, we add 3, thus we make
#[[], [3], [1], [1,3], [2], [2,3], [1,2], [1,2,3]]
# we could implement this strategy in both recursive and iterative ways.

def get_power_set_one(array, idx = len(array) -1):
    power_sets =[[]]
    if idx < 0:
        # is the array is empty, the return the default power set
        return [[]]
    
    val = array[idx]
    power_sets = get_power_set_one(array, idx - 1)
    for i in range(len(power_sets)):
        power_set = power_sets[i]
        power_sets.append(power_set + [val])
    
    return power_sets


def get_power_set_two(array):
    power_sets= [[]]

    for i in range(len(array)):
        for j in range(len(power_sets):
            power_set =  power_sets[j]
            power_sets.append(power_set + [array[i]])
    
    return power_set

```

* Now it is the right time to make some comparison:

    * find all ONE, TWO, THREE, FOUR , ... elements sub-sets
        * loop. inner index over outside index by one
    * find all sub-sets (power set)
        * merger - conquer


    * find all ONE, TWO, THREE, FOUR, ... elements sub-array
        * loop, inner index not equal to outside index
    * find the full permutations
        * search a tree
    * find all sub-arrays
        * search a tree (N branch tree)

* Two number sum: give an array of integers and an integer, called target. Return all possible sets of two elements from the input array, where the two elements sum up to the target. If no pair of elements meet the requirements, return an empty array.
* Three number sum: 
* Four number sum: 
