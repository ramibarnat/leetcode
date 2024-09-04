#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 1, 2, 3, 4, 5, 6
        # 1 -> 6 -> 2
        # 2 -> 5 -> 3
        # 3 -> 4

        # 1 -> 6 -> 2 -> 5 -> 3 -> 4

        # 1, 2, 3, 4
        # 1 -> 4
        # 1 -> 4 -> 2
        # 2 -> 3
        # 2 -> 3 -> 3

        if not head.next or not head.next.next:
            return
        
        arr = []
        temp = head
        while head:
            arr.append(head)
            head = head.next
        
        for i in range((len(arr)-1)//2):
            cur = temp.next # 3
            temp.next = arr[~i] # 2 -> 4
            temp.next.next = cur # 2 -> 4 -> 3
            temp = cur # temp = 3
        
        if len(arr) % 2:
            cur.next = None
        else:
            cur.next.next = None

    def reorderListBetter(self, head: Optional[ListNode]) -> None:
        # We can set all the second half to point to the
        # previous element so that we have something like this:
        # 1 -> 2 -> 3 
        # 6 -> 5 -> 4
        # Then we can easily splice them together:
        # 1 -> 6 -> 2 -> 5 -> 3 -> 4
        pass

# @lc code=end

