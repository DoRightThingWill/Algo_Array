def get_power_set_one(array, idx = 0):
    power_sets =[[]]
    if idx == len(array):
        # is the array is empty, the return the default power set
        return [[]]
    
    val = array[idx]
    power_sets = get_power_set_one(array, idx + 1)
    for i in range(len(power_sets)):
        power_set = power_sets[i]
        power_sets.append(power_set + [val])
    
    return power_sets


def get_power_set_two(array):
    power_sets= [[]]

    for i in range(len(array)):
        for j in range(len(power_sets)):
            power_set =  power_sets[j]
            power_sets.append(power_set + [array[i]])
    
    return power_sets

array = [1,2,3]
power_set_one = get_power_set_one(array, 0)
print(power_set_one)
print('len set one', len(power_set_one))

power_set_two = get_power_set_two(array)
print(power_set_two)
print('len set two', len(power_set_two))