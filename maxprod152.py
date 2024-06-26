def maxProduct(nums):
    res = max(nums)
    curMax, curMin = 1, 1
    
    for n in nums:
        tmp = curMax
        curMax = max(n, curMax*n, curMin*n)
        curMin = min(n, tmp*n, curMin*n)
        res = max(curMax,curMin,res)

    return res

def intuitive(nums):
    # solutions will always be the right or left side of a negative value so we can just compute the product going each way and we will get our answer eventually
    pref = 1
    suf = 1
    res = -1000000
    for i in range(len(nums)):
        pref = pref * nums[i]
        suf = suf * nums[len(nums)-i-1]
        res = max(res,pref,suf)
        if nums[i] == 0:
            pref = 1
        if nums[len(nums)-i-1] == 0:
            suf = 1
    return res
        


arr = [-2,0,-1]
print(maxProduct(arr))
print(intuitive(arr))