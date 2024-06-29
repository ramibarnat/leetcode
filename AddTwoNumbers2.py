def addTwoNumbersWrong(l1,l2):
    # l1 = [2,4,3], l2 = [5,6,4]
    # 342 + 465 = 807
    # Answer = [7,0,8]
    res = []
    carry = 0

    for i in range(max(len(l1),len(l2))):
        num1 = l1[i] if l1[i] else 0
        num2 = l2[i] if l2[i] else 0
        res.append((num1+num2+carry) % 10)
        carry = 1 if num1 + num2 + carry > 9 else 0

    return res

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# def arrToLinkedList(arr):
#     res = head = ListNode(arr[0])
#     for i in range(1,len(arr)):
#         res.next = ListNode(i)
#         res = res.next
#     return head

def addTwoNumbers(l1,l2):
    res = ListNode()
    head = res
    carry = 0

    while l1 or l2 or carry:
        num1 = num2 = 0
        if l1:
            num1 = l1.val
            l1 = l1.next
        if l2:
            num2 = l2.val
            l2 = l2.next
        # carry = 1 if num1 + num2 + carry > 9 else 0
        carry, val = divmod(num1+num2+carry, 10)

        res.next = ListNode(val)
        res = res.next

    return head.next

# l1, l2 = [2,4,3], [5,6,4]

# print(arrToLinkedList(l1))
# print(addTwoNumbers(l1,l2))