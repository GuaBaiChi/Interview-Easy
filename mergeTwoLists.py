# https://leetcode.com/problems/merge-two-sorted-lists/
# 21. Merge Two Sorted Lists


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        l1 = list1
        l2 = list2
        if not l1:
            return l2
        if not l2:
            return l1

        current = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        if l1:
            current.next = l1
        if l2:
            current.next = l2

        return dummy.next


# driver code
def createLinkedList(lst):
    head = None
    for val in reversed(lst):
        head = ListNode(val, head)
    return head


def toList(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst


l1 = createLinkedList([1, 2, 4])
l2 = createLinkedList([1, 3, 4])
obj = Solution()
print(toList(obj.mergeTwoLists(l1, l2)))
