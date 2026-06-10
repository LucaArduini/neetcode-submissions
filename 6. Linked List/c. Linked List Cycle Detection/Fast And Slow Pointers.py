# Esiste un algoritmo famoso per il rilevamento dei cicli che non usa memoria extra (spazio O(1)):
# l'Algoritmo di Floyd (Tartaruga e Lepre).

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next          # Si muove di 1
            fast = fast.next.next     # Si muove di 2
            
            if slow == fast:          # Se si incontrano, c'è un ciclo
                return True
                
        return False