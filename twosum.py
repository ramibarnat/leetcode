def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            if num < target:
                if num in dic:
                    dic[num].append(i)
                else:
                    dic[num] = [i]

        for key in dic:
            if target-key in dic:
                  if target-key == key:
                       if len(dic[key]) == 2:
                           return [dic[key][0], dic[key][1]]
                       else:
                            continue
                  
                  return [dic[key][0], dic[target-key][0]]
            
             

print(twoSum([3,2,4], 6))