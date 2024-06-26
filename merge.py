def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        
        while j >= 0: # this is a really clever trick because if all of nums2's elements are larger than nums1, then they are all added to the end of the array and we can stop since nums1 is sorted already
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

nums1 = [1,2,3,0,0,0]
nums2 = [4,5,6]
merge(nums1, 3, nums2, 3)
print(nums1)