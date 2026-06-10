# TIME COMPLEXITY: O(N)
# SPACE COMPLEXITY: O(N)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()

        p = head
        while p:
            if p not in seen:
                seen.add(p)
                p = p.next
            else:
                return True

        return False