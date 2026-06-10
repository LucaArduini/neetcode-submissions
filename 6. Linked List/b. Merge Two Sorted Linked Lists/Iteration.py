# TIME COMPLEXITY: O(N+M)       dove N e M sono le lunghezze delle due liste
# SPACE COMPLEXITY: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Creiamo un nodo sentinella (dummy) per gestire facilmente la testa della lista
        dummy = ListNode(-1)    # crea un nuovo oggetto (un'istanza) della classe ListNode con 'val' -1 e 'next' None
        current = dummy
        
        # Finchè entrambe le liste hanno elementi
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            
        # Se una delle due liste finisce, colleghiamo il resto dell'altra
        current.next = list1 if list1 is not None else list2
        
        # La lista vera inizia dopo il nodo dummy
        return dummy.next