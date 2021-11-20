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
# it is easy to see the time complexity is O(n^3). And space complexity is O(n^3) too

```
Here, one important finding is: to generate a set, which means no duplicated index appear, like [array[1], array[2]], and [array[2], array[1]], we need to make sure: inner loop index is over outside loop index by ONE. This makes the loop never look back.

While for arrangements or permutation, all loop iterates from head to end, skipping the same index.


* Get all the permutation of the input array. 
What if, we do not know the length of the input array and we need to make the full permutation? If the length is N, we need N level loops????

```python

```


* Give a set of characters, return all strings that it could produce. For example, input set is ['a', 'b']. Then the output set could be '', 'a', 'b', 'ab', and 'ba'


* Two number sum: give an array of integers and an integer, called target. Return all possible sets of two elements from the input array, where the two elements sum up to the target. If no pair of elements meet the requirements, return an empty array.
* Three number sum: 
* Four number sum: 
