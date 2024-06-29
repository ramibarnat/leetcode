def search(nums, target):
    if nums[0] == target:
        return 0
    if nums[len(nums)-1] == target:
        return len(nums)-1
    if len(nums) == 1:
        return -1
    left = 0
    right = len(nums)-1
    while right > left+1:
        mid = left + (right-left) // 2
        if target == nums[mid]:
            return mid

        if nums[mid] > nums[right]: # we're on the left side [4,5,|6|,7,1,2,3]
            if nums[mid] > target and target > nums[right]: # [4,5,|6|,7,1,2,3] target = 5
                right = mid
            elif nums[mid] > target and target < nums[right]: # [4,5,|6|,7,1,2,3] target = 2
                left = mid
            elif nums[mid] < target: # [4,5,|6|,7,1,2,3] target = 7
                left = mid
        else: # we're on the right side [4,5,6,7,0,|1|,2,3]
            if nums[mid] > target: # [4,5,6,7,0,|1|,2,3] t = 0
                right = mid
            elif nums[mid] < target and target < nums[right]: # [4,5,6,7,0,|1|,2,3] t = 5
                left = mid
            elif nums[mid] < target and target > nums[right]: # [4,5,6,7,0,|1|,2,3] t = 7
                right = mid

    return -1

arr = [4,5,6,7,0,1,2]
# arr = [1]
# arr = [4,5,6,7,0,1,2]
arr = [4,5,6,7,8,1,2,3]
print(search(arr, 8))