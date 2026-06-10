# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            tmp = curr.next     # Salviamo il nodo successivo prima di sovrascrivere curr.next
            curr.next = prev    # Invertiamo il puntatore del nodo corrente
            prev = curr         # Spostiamo prev al nodo corrente
            curr = tmp          # Avanziamo al nodo successivo (salvato in tmp)
        
        return prev