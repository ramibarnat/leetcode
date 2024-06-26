def findMin(nums):
    
    size = len(nums)
    if size == 1 or nums[size-1] > nums[0]:
        return nums[0]

    if nums[0] > nums[size-1] and nums[size-2] > nums[size-1]:
        return nums[size-1]
    
    start = 0
    end = size - 1
    prev = nums[0] # We don't need this
    while True:
        mid = start + (end-start) // 2
        if nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]:
            return nums[mid]
        
        if nums[mid] > prev:
            start = mid
        else:
            end = mid

        


arr = [5,1,2,3,4]
print(findMin(arr))