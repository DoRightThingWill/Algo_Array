## Couple of high frequency coding interview questions
* Depth First Search
* Recursion
* Back Track
* Sliding Window
* Double/Triple Pointers
* Dynamic Programming
* Greedy
## Typical Array Problem

* Get all subsets that contains two elements. The order of elements in the subset does not matter. Elments in the input array are distinct.
```python
def produce_all_sets(array):
    rtn_list = []
    for i in range(len(array) - 1):
        for j in range(1, len(array)):
            


```


* Get a group of arrays. Each array contains two elements (different indecies) from the input array. 
* Get all the permutation of the input array. 
* Give a set of characters, return all strings that it could produce. For exmaple, input set is ['a', 'b']. Then the output set could be '', 'a', 'b', 'ab', and 'ba'
* Two number sum: give an array of integers and an integer, called target. Return all possible sets of two elements from the input array, where the two elements sum up to the target. If no pair of elements meet the requirements, return an empty array.
* Three number sum: 
* Four number sum: 


