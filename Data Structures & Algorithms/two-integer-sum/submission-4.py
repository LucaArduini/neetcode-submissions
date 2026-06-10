# TITOLO: Ricerca tramite Mappa di Supporto (Two-Pass Hash Map)
# SPIEGAZIONE: Associa ogni numero al suo indice in un dizionario, poi scorre l'array per trovare se il complemento (target - numero) esiste a un indice diverso.
# TIME COMPLEXITY: O(N)
# SPACE COMPLEXITY: O(N)

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappa_indici = {}
        # Primo passaggio: memorizza numero -> indice
        for i, num in enumerate(nums):
            mappa_indici[num] = i
            
        # Secondo passaggio: cerca il complemento
        for i, num in enumerate(nums):
            complemento = target - num
            # Verifica che il complemento esista e non sia l'elemento stesso
            if complemento in mappa_indici and mappa_indici[complemento] != i:
                indice_j = mappa_indici[complemento]
                return [i, indice_j] if i < indice_j else [indice_j, i]