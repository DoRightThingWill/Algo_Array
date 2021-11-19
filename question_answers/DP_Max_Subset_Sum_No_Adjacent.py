# write a function
# input is an array of integers
# and find the max value of:
# subset consisting of non-adjacent elements
# in the original array


# here I provide three solutions for this question
# you can figure out which one is best considering the time complexity

def max_sub_set_sum_one(array):
    # Write your code here.
    #				xx
    #			/			\
    #		yes				no
    #		/  \		/		\
    #	no		no		yes		no
    #	/	\
    # yes	no
    #
    #
	max_list = []
	cur_max  = 0
	get_max_from_array(array, 0, cur_max, max_list)
	print(max_list)
	
	max_list.sort()
	return max_list[-1]
	
def get_max_from_array(array, start, cur_max, max_list):
	if start >= len(array):
		max_list.append(cur_max)
		return 0
	# cur_max here is kind of like a path list to record the contribution made by this run
	# max_list is just for comparison
	cur_max_1 = cur_max
	cur_max_2 = cur_max
	# option 1: add the first element
	cur_max_1 += array[start]
	cur_max_1 += get_max_from_array(array, start+2, cur_max_1, max_list)
	
	# opetion 2: skip the first element
	cur_max_2 += get_max_from_array(array, start+1, cur_max_2, max_list)
	
	# set the cur_max to the larger one from the two options
	cur_max =  max(cur_max_1, cur_max_2)
	
	return cur_max
	
	
def max_sub_set_sum_two(array):
    # Write your code here.
	# Time O(n),  Space O(n)
	if len(array) == 0:
		return 0
	
	# numbers = [0 for _ in range(len(array))]
	numbers = array[:]
	# you can just copy this array and then override it
	
	print(numbers)
	for idx in range(len(array)):
		if idx == 0:
			numbers[idx] = array[idx]
		elif idx == 1:
			numbers[idx] = max(array[1], array[0])
		else:
			numbers[idx] = max(numbers[idx - 1], array[idx] + numbers[idx - 2])
	
	return numbers[-1]

def max_sub_set_sum_three(array):
    # Write your code here.
    # memorized dynamic programming
	
	return max_sub_sum_helper(array, 0, {})

def max_sub_sum_helper(array, idx, memorized):
	if idx in memorized:
		return memorized[idx]
	
	if idx >= len(array):
		return 0
	elif idx == len(array) - 1:
		memorized[idx] = array[idx]
		return array[idx]
	elif idx == len(array) - 2:
		memorized[idx] = max(array[idx], array[idx + 1])
		return memorized[idx]
	# if idx not in memorized:
	cur_max_sum = 0

	skip_cur_number = max_sub_sum_helper(array, idx + 1, memorized)
	with_cur_number = array[idx] + max_sub_sum_helper(array, idx + 2, memorized)

	cur_max_sum = max(skip_cur_number, with_cur_number)

	memorized[idx] = cur_max_sum

	return cur_max_sum

# this is most optimal solution
# time complexity: O(n)
# space complexity: O(1)
def slution_four(array):
	if not len(array):
		return 0
	elif len(array) == 1:
		return array[0]
	
	prev = array[0]
	current = max(array[0], array[1])
	for i in range(2, len(array)):
		prev = current
		current = max(current, array[i] + prev)
	
	return current