# TIME COMPLEXITY: O(N)
# SPACE COMPLEXITY: O(1)

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Trova il centro (slow arriverà alla fine della prima metà)
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Inverti la seconda metà (a partire da slow.next)
        second = slow.next
        slow.next = None  # Tagliamo la lista in due
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Ora 'prev' è la testa della seconda metà invertita
        
        # 3. Fondi le due liste
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
