def get_permutations(array):
    if len(array) == 1:
        return [[array[0]]]
    val = array.pop()

    arrangements =  get_permutations(array)

    new_arrangements =[]
    for arrangement in arrangements:
        # length of new arrangement is larger than length of old arrangement by one
        for i in range(len(arrangement) + 1): 
            # i is controlling the qty of the new arrangements (1 + len(arrangement))
            # i here is also the index of val (new element) in the new arrangement
            new_arrangement = []
            for j in range(i):
                new_arrangement.append(arrangement[j])
            new_arrangement.append(val)
            for k in range(i + 1, len(arrangement) + 1):
                new_arrangement.append(arrangement[k - 1])
            new_arrangements.append(new_arrangement)
    
    return new_arrangements

array = [1,2,3,4]
permutations = get_permutations(array)
print('len', len(permutations))
print(permutations)





