# TITOLO: Ricerca tramite Mappa di Supporto (Two-Pass Hash Map)
# SPIEGAZIONE: Associa ogni numero al suo indice in un dizionario, poi scorre l'array per trovare se il complemento (target - numero) esiste a un indice diverso.
# TIME COMPLEXITY: O(N) - Scorre l'array due volte. La ricerca nel dizionario ha un costo medio di O(1).
# SPACE COMPLEXITY: O(N) - Memorizza tutti gli elementi dell'array all'interno del dizionario.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappa_indici = {}
        for i, num in enumerate(nums):
            mappa_indici[num] = i
            
        for i, num in enumerate(nums):
            complemento = target - num
            if complemento in mappa_indici and mappa_indici[complemento] != i:
                indice_j = mappa_indici[complemento]
                return [i, indice_j] if i < indice_j else [indice_j, i]