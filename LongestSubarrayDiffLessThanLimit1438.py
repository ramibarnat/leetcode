# [8,2,6,5,7] limit = 4
# dec = [8]
# inc = [8]
# dec = [8,2]
# inc = [2]
# dec = [6] The reason that we remove 2 from this is because
#           if we encounter a number that is lower than 2, we
#           just want to keep going until we find the largest
#           index that does not going over limit
#           Ex: We encounter 0, even if we still had 5 in dec,
#               it's not like we could start at the index where 5
#               is found. It wuold be important to keep 5 if it came
#               after 6 since then we would need to check it 
# inc = [2,6]
# dec = []
import collections


def longestSubarray(nums,limit):
    decQ = collections.deque()
    incQ = collections.deque()
    res = 1
    left = 0
    for right, num in enumerate(nums):
        while decQ and num > decQ[-1]:
            decQ.pop()
        decQ.append(num)

        while incQ and num < incQ[-1]:
            incQ.pop()
        incQ.append(num)
        
        while decQ[0] - incQ[0] > limit:
            if decQ[0] == nums[left]:
                decQ.popleft()
            if incQ[0] == nums[left]:
                incQ.popleft()
            left += 1

        res = max(res, right-left+1)
        
    return res
            



arr = [8,2,6,5,7]
print(longestSubarray(arr,4))