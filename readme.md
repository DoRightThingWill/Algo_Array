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
* Get all the permutation of the input array. 
* Give a set of characters, return all strings that it could produce. For example, input set is ['a', 'b']. Then the output set could be '', 'a', 'b', 'ab', and 'ba'
* Two number sum: give an array of integers and an integer, called target. Return all possible sets of two elements from the input array, where the two elements sum up to the target. If no pair of elements meet the requirements, return an empty array.
* Three number sum: 
* Four number sum: 
<<<<<<< HEAD


=======
>>>>>>> 944add495e9181a3576bdf0b2a110579401e19c2
