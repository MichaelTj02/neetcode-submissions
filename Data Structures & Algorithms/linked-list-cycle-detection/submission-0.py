# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        map = {}
        curr = head
        while curr is not None:
            if curr in map:
                return True
            else:
                map.setdefault(curr, 0)
                curr = curr.next
        return False