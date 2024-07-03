import heapq

def topKFrequentBad(nums,k):
    # [1,1,1,2,2,3]
    
    dic = {}
    in_res = {}
    res = []
    for num in nums:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
        
        if len(res) < k and num not in in_res:
            res.append(num)
            in_res[num] = len(res)-1
        elif num not in in_res and dic[num] > dic[res[len(res)-1]]:
            in_res.pop(res[len(res)-1])
            in_res[num] = len(res)-1
            res[len(res)-1] = num
        
        # if num in in_res:
        #     res.sort(key = lambda x: dic[x], reverse=True)
        if len(res) > 1 and num in in_res:
            if dic[num] > dic[res[0]]:
                res[0], res[in_res[num]] = num, res[0]
                in_res[res[in_res[num]]] = in_res[num]
                in_res[num] = 0
                continue
            for i in reversed(range(0, in_res[num])):
                if dic[res[i]] >= dic[num]:
                    # res[i+1], res[in_res[num]], in_res[num], in_res[res[i+1]] = res[in_res[num]], res[i+1], in_res[res[i+1]], in_res[num]
                    res[i+1], res[in_res[num]] = res[in_res[num]], res[i+1]
                    in_res[res[in_res[num]]] = in_res[num] 
                    in_res[num] = i
                    break
    return res

def topKFrequent(nums,k):
    # cut_off = 1 total = 1, dic = {1:1}, res = {1:{1}}
    # cut_off = 1 total = 1, dic = {1:2}, res = {1:{}, 2:{1}}
    # cut_off = 1 total = 1, dic = {1:3}, res = {1:{}, 2:{}, 3:{1}}
    # cut_off = 1 total = 2 since count >= cutoff and it used to be less, dic = {1:3, 2:1}, res = {1:{2}, 2{2}, 3:{1}}
    # cut_off = 2 total = 2, dic = {1:3, 2:2, 3:1}, res = {1:{3}, 2:{2}, 3:{1}}
    # cut_off was incremented because total was already at k and we attempted to add another value
    # that was greater than or equal to cut_off but wasn't already above the cut_off before
    
    cut_off = 1
    total = 0
    dic = {}
    res = {}
    ans = []
    
    for num in nums:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1

        if dic[num] > 1:
            res[dic[num]-1].remove(num)
        if dic[num] in res:
            res[dic[num]].add(num)
        else:
            res[dic[num]] = set([num])

        if dic[num] == cut_off: # increment total
            total += 1
            if total > k:
                total -= len(res[cut_off])
                cut_off += 1

    for key in res:
        if key >= cut_off:
            for val in res[key]:
                ans.append(val)

    return ans
                


# k = 2
# nums = [1,1,1,2,2,3]
# k = 1
# nums = [1]
k = 3
nums = [-1,1,4,-4,3,5,4,-2,3,-1]
print(topKFrequent(nums,k))

