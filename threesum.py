def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # [-4,-1, -1, 0, 1, 2]
    # [i,  j, -1, 0, 1, k] -3
    # [i, -1,  j, 0, 1, k] -3
    # [i, -1, -1, j, 1, k] -2
    # [i, -1, -1, 0, j, k] -1
    # [-4, i,  j, 0, ]

    
    nums.sort()
    target = 0 # we don't really need this but if we wanted to change the target it's good to have
    result = set()

    for i in range(len(nums)):
        j = i + 1
        k = len(nums) - 1
        while k > j:
            sum = nums[i] + nums[j] + nums[k]
            if sum > 0:
                k -= 1
            elif sum < 0:
                j += 1
            else:
                result.add((nums[i], nums[j], nums[k]))
                j += 1
                k -= 1
        

    new_result = []
    for list in result:
        new_result.append([list[0], list[1], list[2]])
    return new_result

print(threeSum(nums = [-1,0,1,2,-1,-4]))