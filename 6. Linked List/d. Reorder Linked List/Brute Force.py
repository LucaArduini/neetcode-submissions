# TIME COMPLEXITY: O(N)
# SPACE COMPLEXITY: O(N)

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Usiamo una lista invece di un dizionario per avere un ordine sequenziale
        nodes = []
        p = head
        while p:
            nodes.append(p) # Salviamo il riferimento al NODO, non il valore
            p = p.next

        # Se la lista è vuota o ha 1-2 elementi, non serve fare nulla
        if not nodes:
            return

        l, r = 0, len(nodes) - 1
        
        # Costruiamo la nuova catena usando i nodi esistenti
        while l < r:
            # Colleghiamo il nodo sinistro al destro
            nodes[l].next = nodes[r]
            l += 1
            
            # Se siamo arrivati al centro, chiudiamo la lista
            if l >= r:
                break
            
            # Colleghiamo il nodo destro al prossimo sinistro
            nodes[r].next = nodes[l]
            r -= 1
        
        # Assicuriamoci che l'ultimo nodo punti a None per evitare cicli
        nodes[l].next = None