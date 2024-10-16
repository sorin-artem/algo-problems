def twoSum(nums, target):
    calculated_values_indexes = {}
    for num_index in range(len(nums)):
        found_value = target - nums[num_index]
        if found_value in calculated_values_indexes:
            return [calculated_values_indexes[found_value], num_index]
        calculated_values_indexes[nums[num_index]] = num_index
    return []


print(twoSum([2, 7, 11, 15], 9))
